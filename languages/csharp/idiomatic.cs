using System;
using System.Linq;

class Program {
    static string FizzBuzz(int n) {
        var word = (n % 3 == 0 ? "Fizz" : "")
            + (n % 5 == 0 ? "Buzz" : "");
        return word.Length > 0 ? word : n.ToString();
    }

    static void Main() {
        var words = Enumerable.Range(1, 100)
            .Select(FizzBuzz);
        foreach (var word in words) {
            Console.WriteLine(word);
        }
    }
}
