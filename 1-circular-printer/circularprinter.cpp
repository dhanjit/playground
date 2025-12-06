#include "circularprinter.hpp"

#include <cassert>

int main(int argc, char**argv) {
    std::string s;
    int32_t count, threadcount, num;

    if (argc != 5) {
        std::cin >> s;
        std::cin >> count;
        std::cin >> threadcount;
        std::cin >> num;
    } else {
        s = std::string{argv[1]};
        count = std::stoi(argv[2]);
        threadcount = std::stoi(argv[3]);
        num = std::stoi(argv[4]);
    }
    func(argv[1], std::stoi(argv[2]), std::stoi(argv[3]), std::stoi(argv[4]));
}
