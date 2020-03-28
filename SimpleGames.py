import random


def welcome():
    rows = 7
    coloumns = 8
    for i in range(rows):
        for j in range(coloumns):
            if i == 0 or i == rows - 1 or j == 0 or j == coloumns - 1:
                print('*\t', end="")
            elif (i == 3):
                print('*\t\t', end="")
                print("Welcome\t\t", end="")
                print('*\t', end="")
                print('*\t', end="")
                break
            else:
                print("\t", end="")
        print()
    input("Press any key to Start:\t")


def mainmenu():
    print("\n" * 8)
    print("MENU")
    print("1.Rock Paper Scissors\n2.Cows and Bulls\n3.Exit")
    choice = int(input("Enter Your Choice:\t"))
    if choice == 1:
        RPS()
        print()
    elif choice == 2:
        CAB()
        print()
    elif choice == 3:
        exit(0)
    else:
        print("\nYour choice is invalid\n")
        mainmenu()


def RPS():
    print("\n" * 4)
    print("1.Play\n2.Rules\n3.Return to main menu")
    choice = int(input("Enter Your Choice:\t"))
    if choice == 1:
        RPSGame()
    elif choice == 2:
        RPSRules()
    elif choice == 3:
        mainmenu()
    else:
        print("\nYour choice is invalid\n")
        RPS()


def RPSGame():
    print("\n" * 2)
    print("Welcome to ROCK PAPER AND SCISSORS")
    print("You will be Competing against computer.Player to reach 5 points first will win.")
    print("Enter Your choice")
    print("0 for Rock,1 for Paper,2 for Scissors\n 5 For EXIT!")
    user = 0
    comp = 0
    count = 0
    choicelist = ["Rock", "Paper", "Scissors"]
    while user < 5 and comp < 5 and count < 25:
        count += 1
        userChoice = int(input("Enter your choice"))
        if userChoice == 5:
            print("Thank You")
            return
        computerchoice = random.choice([0, 1, 2])
        if userChoice == 0 and computerchoice == 1:
            comp += 1
        elif userChoice == 0 and computerchoice == 2:
            user += 1
        elif userChoice == 1 and computerchoice == 0:
            user += 1
        elif userChoice == 1 and computerchoice == 2:
            comp += 1
        elif userChoice == 2 and computerchoice == 0:
            comp += 1
        elif userChoice == 2 and computerchoice == 1:
            user += 1

        print("YOU:", choicelist[userChoice])
        print("Computer:", choicelist[computerchoice])
        print("Your Score:", user)
        print("Computer Score:", comp)
    if user > comp:
        print("Congrats!You Win")
    elif comp > user:
        print("You Lost.Better Luck Next Time!")
    else:
        print("Its a DRAW")
    mainmenu()


def RPSRules():
    print(" ROCK breaks SCISSORS,\n SCISSORS cuts PAPER,\n PAPER covers ROCK.")




def CAB():
    print("\n" * 4)
    print("1.Play\n2.Rules\n3.Return to main menu")
    choice = int(input("Enter Your Choice:\t"))
    if choice == 1:
        CABGame()
    elif choice == 2:
        CABRules()
    elif choice == 3:
        mainmenu()
    else:
        print("\nYour choice is invalid\n")
        CAB()

def CABRules():
    print("  On a sheet of paper, the players each write a 4-digit secret number.\n  The digits must be all different. \n  Then, in turn, the players try to guess their opponent's number who gives the number of matches.\n  If the matching digits are in their right positions, they are BULLS, if in different positions, they are COWS.")

def CABGame():
    print("\n" * 2)
    print("Welcome to COWS AND BULLS")
    print("You will be Competing against computer.")
    wordslist=["rate","fail","cake","soul","rich","time","swan","pass","calm","face"]
    rand=random.randrange(0,10)
    word=wordslist[rand]
    count=0
    while(count<15):
        s=input("Enter String:\t")
        if s=="-1":
            print("Thank You!")
            return
        cows=0
        bulls=0

        chars=0
        for c in s:
            if c in word:
                chars+=1
        for i in range(0,4):
            if s[i]==word[i]:
                bulls+=1

        cows=chars-bulls
        print("COWS:",cows,"\tBULLS:",bulls)
        if bulls==4:
            print("Congratulations!YOu win")
            mainmenu()
        count+=1
    print(("Maximum Count limit reached"))
    mainmenu()
welcome()
print("\n" * 50)
mainmenu()
