func fizzbuzz(_ n: Int) -> String {
    switch (n % 3, n % 5) {
    case (0, 0): return "FizzBuzz"
    case (0, _): return "Fizz"
    case (_, 0): return "Buzz"
    default: return String(n)
    }
}

(1...100).map(fizzbuzz).forEach { print($0) }
