#include <stdio.h>

const char *fizzbuzz(int n) {
    static char number[12];
    static const char *words[] = {
        "", "Fizz", "Buzz", "FizzBuzz"
    };
    int kind = (n % 3 == 0) | (n % 5 == 0) << 1;
    if (kind) return words[kind];
    snprintf(number, sizeof number, "%d", n);
    return number;
}

int main(void) {
    for (int n = 1; n <= 100; ++n) {
        puts(fizzbuzz(n));
    }
    return 0;
}
