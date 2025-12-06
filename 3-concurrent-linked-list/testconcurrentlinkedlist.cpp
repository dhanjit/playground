#include "concurrentlinkedlist.hpp"

#include <unistd.h>
#include <set>
#include <sstream>
#include <thread>
#include <vector>

void test_emptyList() {
    cll::List<int> l;
    std::stringstream ss;
    ss << l;
    assert(ss.str() == "null");
}

void test_insertToHead() {
    cll::List<int> l;
    std::stringstream ss;
    l.push(1);
    l.push(2);
    l.push(3);
    ss << l;
    assert(ss.str() == "3->2->1->null");
}

void test_insertElemAfterHead() {
    cll::List<int> l;
    std::stringstream ss;
    l.push(1);
    l.push(l.gethead(), 2);
    l.push(l.gethead(), 3);
    ss << l;
    assert(ss.str() == "1->3->2->null");
}

void test_insertElemAfterDifferentElem() {
    cll::List<int> l;
    std::stringstream ss;
    l.push(1);
    l.push(2);
    l.push(3);
    l.push(l.gethead()->next, 4);
    ss << l;
    assert(ss.str() == "3->2->4->1->null");
}

void test_insertElemAtRear() {
    cll::List<int> l;
    std::stringstream ss;
    l.push(1);
    l.push(2);
    l.push(l.gethead()->next, 3);
    ss << l;
    assert(ss.str() == "2->1->3->null");
}

void test_multiThreadInsertions() {
    cll::List<int> l;
    std::stringstream ss;

    std::vector<std::thread> threads;
    int threadcount = 16;
    int insertionsperthread = 100;
    assert(insertionsperthread % 2 == 0);

    auto threadfunc = [&l, &insertionsperthread](int id) {
        sleep(1);
        const auto offset = id * insertionsperthread;
        for (int i = 0; i < insertionsperthread; i += 2) {
            l.push(offset + i);                   // even. means insert at head
            l.push(l.gethead(), offset + i + 1);  // odd. insert after head
        }
    };

    for (int tid = 0; tid < threadcount; tid++) threads.emplace_back(std::thread{threadfunc, tid});
    for (auto& t : threads) t.join();

    // values for one thread (say thread id 3) would be : (if insertionsperthread == 100)
    // 3*100 + 98 -> 3*100 + 99 -> 3*100+96 -> 3*100+97...
    // All values in the range should exist.
    std::set<int> values;
    auto node = l.gethead();
    while (node) {
        assert(values.count(node->data) == 0);
        values.insert(node->data);
        node = node->next;
    }

    int expectedvalue = 0;
    for (auto v : values) assert(v == expectedvalue++);
}

int main() {
    test_emptyList();
    test_insertToHead();
    test_insertElemAfterHead();
    test_insertElemAfterDifferentElem();
    test_insertElemAtRear();
    test_multiThreadInsertions();

    std::cout << "All passed" << std::endl;
}
