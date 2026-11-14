program main
    implicit none
    integer :: i
    do i = 1, 100
        print '(a)', fizzbuzz(i)
    end do
contains
    function fizzbuzz(n) result(word)
        integer, intent(in) :: n
        character(:), allocatable :: word
        character(12) :: number
        if (mod(n, 15) == 0) then
            word = 'FizzBuzz'
        else if (mod(n, 3) == 0) then
            word = 'Fizz'
        else if (mod(n, 5) == 0) then
            word = 'Buzz'
        else
            write(number, '(i0)') n
            word = trim(number)
        end if
    end function
end program
