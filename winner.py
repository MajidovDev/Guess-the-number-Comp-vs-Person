"""
Final and winner finder function module
"""
def winnerResult(cAttempts, pAttempts):
    if cAttempts > 0 and pAttempts > 0:
        if cAttempts > pAttempts:
            print(f"\n>>>You are the WINNER, you find the number in {pAttempts} attempts and computer in {cAttempts} attempts.")
        elif cAttempts < pAttempts:
            print(f"\n>>>Computer is the WINNER, you find the number in {pAttempts} attempts and computer in {cAttempts} attempts.")
        else:
            print("Draw)")





