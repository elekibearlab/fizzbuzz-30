-module(aligned).
-export([main/0]).

fizzbuzz(N) ->
    if
        N rem 15 == 0 -> "FizzBuzz";
        N rem 3 == 0 -> "Fizz";
        N rem 5 == 0 -> "Buzz";
        true -> integer_to_list(N)
    end.

main() ->
    lists:foreach(fun(I) ->
        io:format("~s~n", [fizzbuzz(I)])
    end, lists:seq(1, 100)).
