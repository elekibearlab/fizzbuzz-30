defmodule Main do
    def fizzbuzz(n) do
        if rem(n, 15) == 0 do
            "FizzBuzz"
        else
            if rem(n, 3) == 0 do
                "Fizz"
            else
                if rem(n, 5) == 0 do
                    "Buzz"
                else
                    Integer.to_string(n)
                end
            end
        end
    end

    def main do
        for i <- 1..100, do: IO.puts(fizzbuzz(i))
    end
end

Main.main()
