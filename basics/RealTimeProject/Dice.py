'''
Rolling Dices
============
A simple program that rolls two dices and give out the result

Example
========
$ python3 Dice.py
Rolling the dices...
The values are:
2
6
Roll the dices again?
'''
import random

minVal = 1
maxVal = 6
rollAgain = "yes"
# loop
while rollAgain == "yes" or rollAgain == "y":
    print("Rolling the dices...")
    print("The values are:")
    print(random.randint(minVal, maxVal))
    print(random.randint(minVal, maxVal))
    rollAgain = input("Roll the dices again?")
