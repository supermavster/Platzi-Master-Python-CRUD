# -*- codign: utf-8 -*-

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b


def run():
    fib1 = fibonacci(20)
    fib_nums = [num for num in fib1]
    print(fib_nums)

    # Es importante recalcar que una vez que se ha agotado un generator ya no podemos utlizarlo y debemos crear una nueva instancia. Por ejemplo,
    double_fib_nums = [num * 2 for num in fib1]  # no va a funcionar
    print(double_fib_nums)

    double_fib_nums = [num * 2 for num in fibonacci(30)]  # sí funciona
    print(double_fib_nums)


if __name__ == "__main__":
    run()
