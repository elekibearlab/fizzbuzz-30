-module(idiomatic).
-export([main/0]).

fizzbuzz(N) ->
    case {N rem 3, N rem 5} of
        {0, 0} -> "FizzBuzz";
        {0, _} -> "Fizz";
        {_, 0} -> "Buzz";
        _ -> integer_to_list(N)
    end.

main() ->
    Words = lists:map(fun fizzbuzz/1, lists:seq(1, 100)),
    lists:foreach(fun(W) -> io:format("~s~n", [W]) end,
        Words).
