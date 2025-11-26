#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 and number % 5 == 0: 
            saida = "FizzBuzz"
        elif number % 3 == 0:
            saida = "Fizz"
        elif number % 5 == 0:
            saida= "Buzz"
        else:
            saida = str(number)
        print(saida, end=" ")
