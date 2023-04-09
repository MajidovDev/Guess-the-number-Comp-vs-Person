"""Computer's Turn module that calculates computer's guessing attempts"""
import random as r


def computersTurn():
    start = int(input('Enter the start point of range: ')) #gets the input from user for start point of range
    stop = int(input('Enter the stop point of range: ')) #gets the input from user for stop point of range
    print(f"- You have imagined a number between the range {start} and {stop}, Computer will try to guess.")
    stop+=1
    times = 0
    while True:
        computer = r.choice(range(start,stop))
        times += 1
        print(f"\n>>>Computer's guess is {computer}.")
        confirm = input("If Computer found your imaginary number enter 'won'\n"
              "if Computer's guess less than your number enter '+'\n"
              "if Computer's guess greater than your number enter '-' \n>>>")
        if confirm == 'won':
            if times==1:
                print("\n>>>Yeah, Computer has found your imaginary number in one attempt! ")
            else:
                print(f"\n>>>Yeah, Computer has found your imaginary number in {times} attempts! ")
            return times
        elif confirm == '-':
            print("\n>>>Computer entered the greater number than person imagined :) , Computer will try again... ")
            stop = computer
        elif confirm == '+':
            print("\n>>>Computer entered the lower number than person imagined :) , Computer will try again... ")
            start = computer+1
        
    