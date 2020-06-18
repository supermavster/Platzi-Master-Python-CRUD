# -*- codign: utf-8 -*-
def run():
    print(testARGS(1, x=7, u=8))


def testARGS(*args, **kwargs):
    for arg in args:
        print(arg)

    for item in kwargs.items():
        print(item)


if __name__ == "__main__":
    run()
