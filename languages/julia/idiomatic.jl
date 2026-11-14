function fizzbuzz(n)
    word = (n % 3 == 0 ? "Fizz" : "") *
        (n % 5 == 0 ? "Buzz" : "")
    return isempty(word) ? string(n) : word
end

foreach(n -> println(fizzbuzz(n)), 1:100)
