# -*- codign: utf-8 -*-

PASSWORD = '12345'


def password_required(function):
    def wrapper():
        password = input("Write your password: ")
        if(password == PASSWORD):
            return function()
        else:
            print("Error with your Password :c")
    return wrapper


@password_required
def needs_password():
    print("Correct password!")


def run():
    needs_password()
    # ARGS
    print(testARGS(1, x=7, u=8))


def testARGS(*args, **kwargs):
    for arg in args:
        print(arg)

    for item in kwargs.items():
        print(item)


if __name__ == "__main__":
    run()
