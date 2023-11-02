#!/usr/bin/python3
from calculator_1 import add, sub, div, mul

a = 10
b = 5

added = add(a, b)
mult = mul(a, b)
divide = div(a, b)
subtract = sub(a, b)

print(f"{a} + {b} = {added}")
print(f"{a} - {b} = {subtract}")
print(f"{a} * {b} = {mult}")
print(f"{a} / {b} = {divide}")
