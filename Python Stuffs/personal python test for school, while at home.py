#importing libraries 
import random 

usernumber = eval(input("Input a number between 1-100"))

#setting variables
low = 1
high = 100
computerguess = random.randint(low,high)

while usernumber >=1 or usernumber <= 100:
    
    print("I guessed", computerguess, "if it's too high type L, if it's too low type H and if it's correct type C")
    userinput = input()
    if userinput == "H":
        low = computerguess
    if userinput == "L":
        high = computerguess
    if userinput == "C":
        print("Yay! I got it correct!")
        break
    if userinput == "skip":
        break

    computerguess = random.randint(low,high)

