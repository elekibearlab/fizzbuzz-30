#include <iostream>
#include <ranges>
#include <string>

int main() {
    auto fizzbuzz = [](int n) {
        std::string word;
        if (n % 3 == 0) word += "Fizz";
        if (n % 5 == 0) word += "Buzz";
        return word.empty() ? std::to_string(n) : word;
    };
    auto numbers = std::views::iota(1, 101);
    for (auto word : numbers
        | std::views::transform(fizzbuzz)) {
        std::cout << word << '\n';
    }
}
