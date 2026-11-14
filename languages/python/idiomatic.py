def fizzbuzz(n):
    word = "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0)
    return word or str(n)


def main():
    print(*map(fizzbuzz, range(1, 101)), sep="\n")


if __name__ == "__main__":
    main()
