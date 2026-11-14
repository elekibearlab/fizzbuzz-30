:- initialization(main, main).

fizzbuzz(N, "FizzBuzz") :- 0 is N mod 15, !.
fizzbuzz(N, "Fizz") :- 0 is N mod 3, !.
fizzbuzz(N, "Buzz") :- 0 is N mod 5, !.
fizzbuzz(N, Word) :- number_string(N, Word).

main :-
    numlist(1, 100, Numbers),
    maplist(fizzbuzz, Numbers, Words),
    maplist(writeln, Words).
