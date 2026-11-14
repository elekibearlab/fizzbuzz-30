import java.util.stream.IntStream;

class Main {
    static String fizzbuzz(int n) {
        var word = (n % 3 == 0 ? "Fizz" : "")
            + (n % 5 == 0 ? "Buzz" : "");
        return word.isEmpty()
            ? Integer.toString(n) : word;
    }

    public static void main(String[] args) {
        IntStream.rangeClosed(1, 100)
            .mapToObj(Main::fizzbuzz)
            .forEach(System.out::println);
    }
}
