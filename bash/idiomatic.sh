fizzbuzz() {
    local n=$1 word=
    (( n % 3 )) || word+=Fizz
    (( n % 5 )) || word+=Buzz
    printf '%s\n' "${word:-$n}"
}

for n in {1..100}; do
    fizzbuzz "$n"
done
