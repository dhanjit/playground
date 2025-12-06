# Build and Test
```
make
make test
```

# NOTES
- Took the simpler approach of using sharedptr<T>. 
- Freelist is a stack where free memory (shared ptr) gets inserted.
- Allocation pops a free sharedptr from the freelist stack.
- gc() clears all free ptrs (empties freelist).
- Circular Deletion:
   - done inside gc()
   - Simple O(n^2) loop on the size of the freelist stack (implemented as vector)
   - Detect if `freeptr[i]->pointsTo == freeptr[j] && freeptr[i] == freeptr[j]->pointsTo` and reset both shared_ptr so that reference count doesn't obstruct obj deallocation.
   
   
- There are some performance benefits that could be made, but it generally depends on the use case.
   - It could also be beneficial ot have `growSize*sizeof(T)` chunks of memory allocated instead of one T individually  `growSize` times on every `grow()` call.
   - The above would however not allow us to deallocate all unused in `gc()`.
