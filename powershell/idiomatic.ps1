function Get-FizzBuzz([int] $n) {
    $word = switch (0) {
        ($n % 3) { 'Fizz' }
        ($n % 5) { 'Buzz' }
    }
    if ($word) { $word -join '' } else { "$n" }
}

1..100 | ForEach-Object { Get-FizzBuzz $_ }
