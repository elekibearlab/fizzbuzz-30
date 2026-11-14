object Main extends App {
    def fizzbuzz(n: Int): String = (n % 3, n % 5) match {
        case (0, 0) => "FizzBuzz"
        case (0, _) => "Fizz"
        case (_, 0) => "Buzz"
        case _ => n.toString
    }

    (1 to 100).map(fizzbuzz).foreach(println)
}
