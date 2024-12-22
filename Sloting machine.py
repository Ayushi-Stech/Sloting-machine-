import random

symbols = ["Star", "Moon", "Sun"]

def Spinning():
    return [random.choice(symbols) for _ in range(3)]

def Result(reels, amount):
    if reels[0] == reels[1] == reels[2]:
        return amount * 10
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return amount * 2
    else:
        return 0

balance = 100
print("Welcome to the Slotting Machine :)")
print("Your Starting balance is rupees 100")

while True:
    print(f"\nYour Current balance is : {balance}")
    amount = int(input("please enter the amount you want to put on the bet or press 0 to end the session"))
    if amount == 0:
        break
    elif amount > balance:
        print("You have Insufficient balance...")
        continue

    reels = Spinning()
    print(f"Reels: {reels}")

    winning = Result(reels, amount)
    balance += winning - amount
    if (winning > 0):
        print(f"Congratulations you got the jackpot and You won rupees {winning}.")
    else:
        print("oops you loss but try again for greater luck next time ")
    print(f"Result: {'Win' if winning else 'Loss'}, Balance: {balance}")

print(f"\nyour current balance is: {balance}. \nThanks for playing come.... \ncome again to get rich :)")
