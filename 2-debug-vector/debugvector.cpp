#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    int index = 0;
    for (int i = 0; i < 1000; i++) v.push_back(index++);
    for (auto it = v.begin(); it != v.end(); it++)
        if (*it % 3 == 0) {
            // NOTE: Iterator gets invalidated due to the erase and push back operations. push back invalidates iterators if vector size becomes greater than capacity, i.e a reallocation. 
            const auto pos = it - v.begin();
            v.erase(it);
            v.push_back(index++);
            v.push_back(index++);
            it = v.begin() + pos;
        }

    for (auto num : v) std::cout << num << '\n';
}
