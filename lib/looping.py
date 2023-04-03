#!/usr/bin/env python3


def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")
happy_new_year()


def square_integers(lst):
    result = []
    for num in lst:
        if isinstance(num, int):
            result.append(num ** 2)
    return result



def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)