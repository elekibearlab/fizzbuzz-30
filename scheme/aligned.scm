(define (fizzbuzz n)
    (if (zero? (modulo n 15))
        "FizzBuzz"
        (if (zero? (modulo n 3))
            "Fizz"
            (if (zero? (modulo n 5))
                "Buzz"
                (number->string n)))))

(define (main)
    (do ((i 1 (+ i 1))) ((> i 100))
        (display (fizzbuzz i))
        (newline)))

(main)
