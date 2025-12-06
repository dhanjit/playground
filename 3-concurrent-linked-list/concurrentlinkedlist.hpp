#include <atomic>
#include <cassert>
#include <iostream>
#include <memory>

namespace cll {  // cll: concurrent linked list
template <typename T>
struct Node {
    T data;  // There can be argument for making it std::atomic<T> but keeping as is because focus is on the linked list and
             // synchronization. Also depends on the use case of how data is modified/accessed.
    std::atomic<Node<T>*> next;
};

template <typename T>
class List {
    std::atomic<Node<T>*> head{nullptr};

   public:
    void push(T data) {
        auto node = new Node<T>{};
        node->data = data;
        auto next = head.load(std::memory_order_relaxed);

        // Compare and Swap to atomically insert.
        do {
            node->next =
                next;  // This is necessary because the 'expected' variable in the compare and swap is not of atomic<Node<T>> but Node<T>.
        } while (!std::atomic_compare_exchange_weak_explicit(&head, &next, node, std::memory_order_release, std::memory_order_relaxed));

        // std::cout << *this << std::endl;
        // std::cout << data << std::endl;
    }

    void push(Node<T>* t, T data) {
        assert(t != nullptr);
        auto node = new Node<T>{};
        node->data = data;
        auto next = t->next.load(std::memory_order_relaxed);
        do {
            node->next = next;
        } while (!std::atomic_compare_exchange_weak_explicit(&t->next, &next, node, std::memory_order_release, std::memory_order_relaxed));

        // std::cout << *this << std::endl;
        // std::cout << data << std::endl;
    }

    Node<T>* gethead(std::memory_order mo = std::memory_order_seq_cst) { return head.load(mo); }
    const Node<T>* gethead(std::memory_order mo = std::memory_order_seq_cst) const { return head.load(mo); }
};

// Helper function to print and test.
template <typename T>
std::ostream& operator<<(std::ostream& os, const List<T>& l) {
    auto node = l.gethead();
    while (node) {
        os << node->data << "->";
        node = node->next.load(std::memory_order_relaxed);  // Causality determines that ordering is maintained.
    }
    os << "null";
    return os;
}
}  // namespace cll
