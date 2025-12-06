# Build and Test
```
make
make run
```

# Custom Arguments:
```
./circularprinter <string> <count> <threadcount> <num>
```

# Notes
- Used condition variable to notify all threads when to wake up and start printing. A variable `threadtoprint` is used to determine which thread wakes and the rest to wait again.
- The question specifically said "threads which start printing..." so I am assuming each thread should call `std::cout` instead of enqueuing data to some queue and printing asynchronously from a different thread.
- Since the order is predetermined and needs to be sequential AND count needs to be called from the thread, there is really not much to do but to synchronize the iostream calls through locks as iostream is not threadsafe.
