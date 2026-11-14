:- initialization(main, main).

fizzbuzz(N, Word) :-
    (   0 is N mod 15 -> Word = "FizzBuzz"
    ;   0 is N mod 3 -> Word = "Fizz"
    ;   0 is N mod 5 -> Word = "Buzz"
    ;   number_string(N, Word)
    ).

main :-
    forall(between(1, 100, I), (
        fizzbuzz(I, Word),
        writeln(Word)
    )).
