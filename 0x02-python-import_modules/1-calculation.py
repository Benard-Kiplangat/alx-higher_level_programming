#!/usr/bin/python3
import calculator_1 as add
a = 10
b = 5
print(f"{a} + {b} = {add.add(a, b)}")
print(f"{a} - {b} = {add.sub(a, b)}")
print(f"{a} * {b} = {add.mul(a, b)}")
print(f"{a} / {b} = {add.div(a, b):.0f}")
