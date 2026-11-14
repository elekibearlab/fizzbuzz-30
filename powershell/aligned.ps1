function Get-FizzBuzz([int] $n) {
    if ($n % 15 -eq 0) {
        return 'FizzBuzz'
    } elseif ($n % 3 -eq 0) {
        return 'Fizz'
    } elseif ($n % 5 -eq 0) {
        return 'Buzz'
    } else {
        return [string] $n
    }
}

for ($i = 1; $i -le 100; $i++) {
    Get-FizzBuzz $i
}
