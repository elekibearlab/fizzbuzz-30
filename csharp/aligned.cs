using System;

class Program {
    static string FizzBuzz(int n) {
        if (n % 15 == 0) return "FizzBuzz";
        else if (n % 3 == 0) return "Fizz";
        else if (n % 5 == 0) return "Buzz";
        else return n.ToString();
    }

    static void Main() {
        for (int i = 1; i <= 100; i++) {
            Console.WriteLine(FizzBuzz(i));
        }
    }
}
