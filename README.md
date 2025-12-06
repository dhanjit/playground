# C++ Systems Playground

This repository serves as a companion to the technical blog posts on [dhanjit.me](https://dhanjit.me). It contains the source code for specific systems programming challenges discussed in the articles.

## Projects

### [Lock-Free Linked List](https://dhanjit.me/blog/lock-free-linked-list)

* **Directory:** `3-concurrent-linked-list`
* **Concept:** A lock-free singly linked list implementation using `std::atomic` and Compare-And-Swap (CAS) loops to manage concurrency without mutexes.

### [Garbage Collector](https://dhanjit.me/blog/cpp-garbage-collector)

* **Directory:** `4-garbage-collector`
* **Concept:** A custom memory pool and naive garbage collector implementation in C++ using a `freelist` and reference counting with simple cycle detection.

## Build

Each directory contains a `makefile` for easy compilation.

```bash
cd 3-concurrent-linked-list
make
./testconcurrentlinkedlist
```
