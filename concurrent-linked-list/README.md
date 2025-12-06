# Build and Test
```
make
make test
```

# Notes
- Insertions and traversal is achieved by using `std::atomic_compare_exchange` on the `node->next` and the `new node` (the same applies for `head`).
    - Refer the code comments.
- How is deletion possible?
    - Deletion can be done by using two pointers as such:
    Let's say the below is the linked list.
    ```
    A -> B -> C -> D -> NULL
    ```
    
    We need to delete C. We can maintain a `current` and `prev` pointers to traverse and delete. And use compare and swap in a two step process.
    ```
    A -> B -> C -> D -> NULL
    
    prev=B
    current=C
    ```
    
    One way is to use compare and exchange on B->next and D. 
    However if we do this in one step and a insertion is happening after C, then we will have a race condition. An element on insert will be missed because C got deleted.
    We can do deletion in two steps. 
    - Mark C to be deleted. Ensure during insertion, if C is marked to be deleted then don't insert after C. Try another node.
    - Link B->next to D.
