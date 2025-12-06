#include <unistd.h>
#include <iostream>
#include <vector>
#include <memory>

namespace pool {
template <typename T>
class Pool {
    std::size_t growSize;
    std::vector<std::shared_ptr<T>> freelist;

   public:
    using Ptr = std::shared_ptr<T>;

    // preallocate enough space for 'initialCapacity' objects, and if that runs out grow by 'growSize' elements
    Pool(size_t initialCapacity, size_t _growSize) : growSize{_growSize} { grow(initialCapacity); }

    void grow() { grow(growSize); }

    std::size_t freecount() const { return freelist.size(); }

    void grow(std::size_t size) {
        while (size--) freelist.emplace_back(Ptr{reinterpret_cast<T *>(new alignas(alignof(T)) char[sizeof(T)])});
    }

    // Construct a new object of type T (from pre-allocated memory if possible), and return a 'Ptr' to that object.
    // The arguments to allocate are the arguments for T's constructor
    template <typename... Args>
    Ptr allocate(Args&&... args) {
        if (freelist.empty()) grow();
        auto ptr = freelist.back();
        new (ptr.get()) T{std::forward<Args>(args)...};
        freelist.pop_back();
        return ptr;
    }

    void destroy(std::shared_ptr<T>&& elem) { // take ownership using std::move
        Ptr p = elem;
        elem->~T();
        freelist.emplace_back(std::move(p));
    }

    // Garbage collection: free up unusable 'T' objects, and perform any required bookkeeping.
    void gc() {
        for (std::size_t i = 0; i < freelist.size(); i++) {
            for (std::size_t j = 0; j < freelist.size(); j++)
                if (i != j && freelist[i]->pointsTo && freelist[j]->pointsTo && freelist[i]->pointsTo == freelist[j] && freelist[i] == freelist[j]->pointsTo) {
                    // Debug
                    std::cout << "Deleting circular" << std::endl;
                    freelist[i]->pointsTo.reset();
                    freelist[j]->pointsTo.reset();
                }
        }
        freelist.clear();
    }
};
}  // namespace pool
