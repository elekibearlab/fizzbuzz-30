def fizzbuzz(n)
    word = "#{'Fizz' if n % 3 == 0}#{'Buzz' if n % 5 == 0}"
    word.empty? ? n.to_s : word
end

def main
    puts((1..100).map { |n| fizzbuzz(n) })
end

main
