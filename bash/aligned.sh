fizzbuzz() {
    local n=$1
    if (( n % 15 == 0 )); then
        printf '%s\n' FizzBuzz
    elif (( n % 3 == 0 )); then
        printf '%s\n' Fizz
    elif (( n % 5 == 0 )); then
        printf '%s\n' Buzz
    else
        printf '%d\n' "$n"
    fi
}

for (( i = 1; i <= 100; i++ )); do
    fizzbuzz "$i"
done
