(defun fizzbuzz (n)
    (let ((word (concatenate 'string
                    (if (zerop (mod n 3)) "Fizz" "")
                    (if (zerop (mod n 5)) "Buzz" ""))))
        (if (plusp (length word))
            word
            (write-to-string n))))

(defun main ()
    (loop for n from 1 to 100
        do (write-line (fizzbuzz n))))

(main)
