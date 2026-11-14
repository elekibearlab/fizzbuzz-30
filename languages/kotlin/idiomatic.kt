fun fizzbuzz(n: Int) = when {
    n % 15 == 0 -> "FizzBuzz"
    n % 3 == 0 -> "Fizz"
    n % 5 == 0 -> "Buzz"
    else -> n.toString()
}

fun main() = (1..100)
    .map(::fizzbuzz)
    .forEach(::println)
