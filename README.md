# C++ Systems Programming Challenges

This repository contains a collection of systems programming challenges implemented in C++. It serves as a playground for exploring concurrency, memory management, and tricky C++ behaviors.

## 1. Circular Printer

A thread synchronization exercise using Condition Variables to coordinate printing in a specific order.

## 2. Debug Vector

Demonstrating C++ Iterator Invalidation scenarios and how to safely navigate vector modifications.

## 3. Concurrent Linked List

A lock-free linked list implementation using `std::atomic` and Compare-And-Swap (CAS) loops.

## 4. Garbage Collector

A custom memory pool and garbage collector implementation in C++ using `freelist` and reference counting.

## Build

Each directory contains a `makefile`.

```bash
cd 3-concurrent-linked-list
make
./testconcurrentlinkedlist
```
