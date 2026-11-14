defmodule FizzBuzz do
    def word(n) do
        case {rem(n, 3), rem(n, 5)} do
            {0, 0} -> "FizzBuzz"
            {0, _} -> "Fizz"
            {_, 0} -> "Buzz"
            _ -> Integer.to_string(n)
        end
    end
end

1..100
|> Stream.map(&FizzBuzz.word/1)
|> Enum.each(&IO.puts/1)
