"""PLayer's turn function module that player enters the guess"""
import random as r


def playersTurn():
    start = int(input('Enter the start point of range: ')) #gets the input from user for start point of range
    stop = int(input('Enter the stop point of range: ')) #gets the input from user for stop point of range
    print(f"- I have imagined a number between the range {start} and {stop}, try to guess.")
    computer = r.choice(range(start,stop))
    times = 0
    while True:
        person = int(input("Enter your guess: "))
        times+=1
        if person == computer:
            if times==1:
                print("\n>>>Congratulations, you have found Computer's imaginary number in one attempt! ")
            else:
                print(f"\n>>>Congratulations, you have found Computer's imaginary number in {times} attempts! ")
            return times
        elif person > computer:
            print("\n>>>You entered the greater number than Computer imagined :) , please try again... ")
        else:
            print("\n>>>You entered the lower number than Computer imagined :) , please try again... ")
            