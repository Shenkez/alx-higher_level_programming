#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5

    added = add(a, b)
    mult = mul(a, b)
    divide = div(a, b)
    subtract = sub(a, b)

    print("{} + {} = {}".format(a, b, added))
    print("{} - {} = {}".format(a, b, subtract))
    print("{} * {} = {}".format(a, b, mult))
    print("{} / {} = {}".format(a, b, divide))
