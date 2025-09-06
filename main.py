import func_calculator as fc
import pygame
import pytest

bender = fc.Calculator()

while True:
    a =       int(input("Enter first value: "))
    command = str(input("Enter the command: [+] [-] [/] [*]"))
    b =       int(input("Enter second value: "))
    result = 0

    if command == '+':
        result = bender.add(a, b)
    elif command == '-':
        result = bender.substract(a, b)
    elif command == '/':
        result = bender.devide(a, b)
    elif command == '*':
        result = bender.multiply(a, b)

    print(f"{a} {command} {b} = {result}")

