identification division.
program-id. fizzbuzz-program.
environment division.
configuration section.
repository. function all intrinsic.
data division.
working-storage section.
01 i binary-long.
01 word pic x(12).
01 number-text pic ZZZ9.
procedure division.
    perform varying i from 1 by 1 until i > 100
        perform fizzbuzz
        display trim(word)
    end-perform
    stop run.
fizzbuzz.
    if function mod(i, 15) = 0
        move "FizzBuzz" to word
    else
        if function mod(i, 3) = 0
            move "Fizz" to word
        else
            if function mod(i, 5) = 0
                move "Buzz" to word
            else
                move i to number-text
                move trim(number-text) to word
            end-if
        end-if
    end-if.
