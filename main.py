import random

#Start of the game
print("Want to play Rock, Paper, Scissors??")
print("Best 2 out of 3!")
print("1")
print("2")
print("3")
print("Shoot!")

#Global Variables
p = "paper"
s = "scissors"
r = "rock"
win = "Damn it! You win!"
lose = "Yes! I win!!"

#Computing variables

score = 0
ai_score = 0


#Actual Game function
while score < 3 and ai_score < 3:
    alist = ["rock", "paper", "scissors"]
    computer = random.choice(tuple(alist))

    player = input()
    print(computer)
    if player == "rock":
        if computer == "scissors":
            print(win)
            score += 1
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
        elif computer == "paper":
            print(lose)
            ai_score += 1
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
        elif score == 3:
            print("Player Wins!")
            break
        else:
            print("It's a Tie!!")
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
    elif player == "scissors":
        if computer == "paper":
            print(win)
            score += 1
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
        elif computer == "rock":
            print(lose)
            ai_score += 1
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
        elif score == 3:
            print("Player Wins!")
            break
        else:
            print("It's a Tie!!")
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
    elif player == "paper":
        if computer == "rock":
            print(win)
            score += 1
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
        elif computer == "scissors":
            print(lose)
            ai_score += 1
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
        elif score == 3:
            print("Player Wins!")
            break
        else:
            print("It's a Tie!!")
            print("Player Score: " + str(score) + " || " + "Computer Score: " + str(ai_score))
    else:
        print("Error")





