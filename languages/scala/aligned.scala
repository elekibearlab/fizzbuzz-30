object Main {
    def fizzbuzz(n: Int): String = {
        if (n % 15 == 0) "FizzBuzz"
        else if (n % 3 == 0) "Fizz"
        else if (n % 5 == 0) "Buzz"
        else n.toString
    }

    def main(args: Array[String]): Unit = {
        for (i <- 1 to 100) {
            println(fizzbuzz(i))
        }
    }
}
