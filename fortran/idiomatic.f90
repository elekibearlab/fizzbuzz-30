program main
    implicit none
    integer :: n
    character(8) :: word
    do n = 1, 100
        word = trim(merge('Fizz', '    ', &
            mod(n, 3) == 0)) // &
            trim(merge('Buzz', '    ', mod(n, 5) == 0))
        if (len_trim(word) == 0) write(word, '(i0)') n
        print '(a)', trim(word)
    end do
end program
