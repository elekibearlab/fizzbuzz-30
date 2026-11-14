<?php
function fizzbuzz(int $n): string {
    return match (true) {
        $n % 15 === 0 => 'FizzBuzz',
        $n % 3 === 0 => 'Fizz',
        $n % 5 === 0 => 'Buzz',
        default => (string) $n,
    };
}

echo implode(PHP_EOL, array_map('fizzbuzz', range(1, 100))),
    PHP_EOL;
