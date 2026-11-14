(defun fizzbuzz (n)
    (if (zerop (mod n 15))
        "FizzBuzz"
        (if (zerop (mod n 3))
            "Fizz"
            (if (zerop (mod n 5))
                "Buzz"
                (write-to-string n)))))

(defun main ()
    (loop for i from 1 to 100 do
        (write-line (fizzbuzz i))))

(main)
