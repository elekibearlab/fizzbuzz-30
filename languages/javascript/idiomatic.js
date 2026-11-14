const fizzbuzz = (n) =>
    (n % 3 === 0 ? "Fizz" : "")
    + (n % 5 === 0 ? "Buzz" : "")
    || String(n);

function main() {
    Array.from({ length: 100 }, (_, i) => fizzbuzz(i + 1))
        .forEach((word) => console.log(word));
}

main();
