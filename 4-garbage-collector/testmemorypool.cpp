#include <cassert>
#include <set>
#include "memorypool.hpp"


int objid = 0;
std::vector<int> constructorder;
std::vector<int>destructorder;
std::vector<void*> allocorder;
std::set<void *> allocset;
std::vector<void*> deallocorder;
std::set<void *> deallocset;


void setup() {
    objid = 0;

    constructorder.clear();
    destructorder.clear();

    allocorder.clear();
    deallocorder.clear();

    allocset.clear();
    deallocset.clear();
}

struct AnObject {
    pool::Pool<AnObject>::Ptr pointsTo;
    int id;

    AnObject() : id {++objid} { constructorder.push_back(id); }

    ~AnObject() { destructorder.push_back(id); }

    void operator delete(void* p) {
        deallocorder.push_back(p);
        deallocset.insert(p);
        free(p);
    }
};

void test_alloc() {
    setup();
    pool::Pool<AnObject> pool{3, 4};
    auto ptr = pool.allocate();
    assert(ptr && ptr->id == 1);
}

void test_capacity() {
    setup();
    pool::Pool<AnObject> pool{3, 4};
    auto ptr = pool.allocate();
    assert(pool.freecount() == 2);
}

void test_exceedInitCapacity() {
    setup();
    pool::Pool<AnObject> pool{3, 10};
    auto ptr1 = pool.allocate();
    auto ptr2 = pool.allocate();
    auto ptr3 = pool.allocate();
    assert(pool.freecount() == 0);
    auto ptr4 = pool.allocate();
    assert(pool.freecount() == 9);
}

void test_gc() {
    setup();
    pool::Pool<AnObject> pool{3, 4};
    auto ptr1 = pool.allocate();
    auto ptr2 = pool.allocate();
    auto ptr3 = pool.allocate();
    auto p1 = ptr1.get();
    auto p2 = ptr2.get();
    auto p3 = ptr3.get();
    pool.destroy(std::move(ptr1));
    pool.destroy(std::move(ptr2));
    pool.destroy(std::move(ptr3));
    pool.gc();
    assert(pool.freecount() == 0);
}

void test_destroy() {
    setup();
    pool::Pool<AnObject> pool{3, 4};
    auto ptr1 = pool.allocate();
    auto ptr2 = pool.allocate();
    auto ptr3 = pool.allocate();
    pool.destroy(std::move(ptr1));
    pool.destroy(std::move(ptr2));
    pool.destroy(std::move(ptr3));
    assert(pool.freecount() == 3);
}

void test_deletecircular() {
    setup();
    pool::Pool<AnObject> pool{10, 3};
    auto ptr1 = pool.allocate();
    auto ptr2 = pool.allocate();

    ptr1->pointsTo = ptr2;
    ptr2->pointsTo = ptr1;

    assert(ptr1.use_count() == 2);
    assert(ptr2.use_count() == 2);

    auto ptr1copy = ptr1;
    auto ptr2copy = ptr2;

    assert(ptr1.use_count() == 3);
    assert(ptr2.use_count() == 3);

    pool.destroy(std::move(ptr1));
    pool.destroy(std::move(ptr2));
    pool.gc();

    assert(pool.freecount() == 0);

    // Ideally this count will be zero, but we need to check if reference count is actually being deleted!! It reduces from 2->0 but here for testing it will reduce from 3->1;
    assert(ptr1.use_count() == 1);
    assert(ptr2.use_count() == 1);

}

int main() {
    test_alloc();
    test_capacity();
    test_exceedInitCapacity();
    test_gc();
    test_destroy();
    test_deletecircular();
    std::cout << "All Passed" << std::endl;
}
