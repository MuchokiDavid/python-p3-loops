#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    x= 10
    while (x>0):
        print(x)
        x-=1
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    # code goes here!
    squared = [number **2 for number in int_list]
    return squared
mess = square_integers([1,2,3,4,5])
print(mess)

def fizzbuzz():
    # code goes here!
    numbers = 100
    while(numbers>0):
        if (numbers % 5==0 and numbers % 3 ==0):
            print('FizzBuzz')
        elif (numbers %5== 0):
            print("Buzz")
        elif (numbers % 3 == 0):
            print("Fizz")
        else:
            print (numbers)
        numbers-=1
fizzbuzz()
