extends SceneTree

func fizzbuzz(n: int) -> String:
    match [n % 3, n % 5]:
        [0, 0]: return "FizzBuzz"
        [0, _]: return "Fizz"
        [_, 0]: return "Buzz"
        _: return str(n)

func _init():
    for n in range(1, 101):
        print(fizzbuzz(n))
    quit()
