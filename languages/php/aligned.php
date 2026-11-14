<?php
function fizzbuzz(int $n): string {
    if ($n % 15 === 0) return "FizzBuzz";
    elseif ($n % 3 === 0) return "Fizz";
    elseif ($n % 5 === 0) return "Buzz";
    else return (string) $n;
}

function main(): void {
    for ($i = 1; $i <= 100; $i++) {
        echo fizzbuzz($i), PHP_EOL;
    }
}

main();
