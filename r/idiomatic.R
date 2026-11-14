fizzbuzz <- function(n) {
    word <- paste0(
        c("", "Fizz")[(n %% 3 == 0) + 1],
        c("", "Buzz")[(n %% 5 == 0) + 1]
    )
    if (word == "") as.character(n) else word
}

writeLines(vapply(1:100, fizzbuzz, character(1)))
