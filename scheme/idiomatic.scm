(define (fizzbuzz n)
    (cond
        ((zero? (modulo n 15)) "FizzBuzz")
        ((zero? (modulo n 3)) "Fizz")
        ((zero? (modulo n 5)) "Buzz")
        (else (number->string n))))

(let loop ((n 1))
    (when (<= n 100)
        (display (fizzbuzz n))
        (newline)
        (loop (+ n 1))))
