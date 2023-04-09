"""
Project Name: find the imaginary number
Author: Sherzod Majidov
Date: 14.12.2022
"""
from intro import introduction as intro
from player import playersTurn as pTurn
from computer import computersTurn as cTurn
from winner import winnerResult as winRes
intro()
pAttempts = pTurn()
continues = input("If you want that computer also find you imaginary number enter (yes/no): ")

if continues == 'yes':
    cAttempts = cTurn()
else:
    print("GAME FINISHED")
if continues == 'yes':
    winRes(cAttempts, pAttempts)



    




