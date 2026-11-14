#include <stdio.h>

const char *fizzbuzz(int n) {
    static char number[12];
    if (n % 15 == 0) return "FizzBuzz";
    else if (n % 3 == 0) return "Fizz";
    else if (n % 5 == 0) return "Buzz";
    else {
        snprintf(number, sizeof number, "%d", n);
        return number;
    }
}

int main(void) {
    for (int i = 1; i <= 100; i++) {
        puts(fizzbuzz(i));
    }
    return 0;
}
