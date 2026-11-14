identification division.
program-id. fizzbuzz-program.
environment division.
configuration section.
repository. function all intrinsic.
data division.
working-storage section.
01 n binary-long.
01 number-text pic ZZZ9.
procedure division.
    perform varying n from 1 by 1 until n > 100
        evaluate true
            when function mod(n, 15) = 0
                display "FizzBuzz"
            when function mod(n, 3) = 0
                display "Fizz"
            when function mod(n, 5) = 0
                display "Buzz"
            when other
                move n to number-text
                display trim(number-text)
        end-evaluate
    end-perform
    stop run.
