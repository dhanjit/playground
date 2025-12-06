#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include <mutex>
#include <condition_variable>
#include <atomic>

// NOTE: There was no namespace mentioned, so keeping the name of the function 'func' as described in the question.
// NOTE: The question specifically said "threads which start printing..." so I am assuming each thread should call `std::cout` instead of
// enqueuing data to some queue and printing asynchronously from a different thread.

// NOTE: Since the order is predetermined and needs to be sequential AND count needs to be called from the thread, there is really not much to do but to synchronize the iostream calls through locks as iostream is not threadsafe.
void func(const std::string& s, int32_t count, int32_t threadcount, int32_t num) {
    std::vector<std::thread> threads;
    std::atomic<std::size_t> indextoprint = 0;
    std::atomic<int32_t> threadtoprint = 0;
    std::mutex mutex;
    std::condition_variable cv;

    auto threadfunction = [&](int32_t threadnumber) {
        auto lines = num;
        while (lines--) {
            std::unique_lock<std::mutex> lock{mutex};
            // Using the condition variable to wait on the lock, if threadtoprint is for this thread, then wake otherwise go back to wait.
            cv.wait(lock, [&] { return threadnumber == threadtoprint; });

            const auto startindex = indextoprint.load();

            std::cout << "Thread" << threadnumber << ": ";
            for (int32_t i = 0; i < count; i++) {
                std::cout << s[(startindex + i) % s.size()];
            }
            std::cout << '\n';

            indextoprint = (indextoprint + count) % s.size();
            threadtoprint = (threadtoprint % threadcount + 1);
            lock.unlock();
            cv.notify_all();
        }
    };

    for (int32_t i = 0; i < threadcount; i++) {
        threads.emplace_back(std::thread{threadfunction, i + 1});
    }

    threadtoprint++;
    cv.notify_all();

    for (auto& thread: threads) thread.join();
}
