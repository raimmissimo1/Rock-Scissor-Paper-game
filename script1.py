import random

choices = ["rock" , "paper" , "scissor"]
active = True
comp_wins = 0
human_wins = 0

print("                      Welcome to the game !!!                        ")

while active:
    print("------------------------------------------------------------------")
    print("Available choices: Rock , Paper , Scissor")
    user_choice = input("Enter your choice(q to Quit): ").lower()
    comp_choice = random.choice(choices)
    print("Computer choice: ", comp_choice)
    print("-------------------------------------------------------------------")

    if user_choice == "q":
        print(f"Computer won {comp_wins} times!!")
        print(f"Human won {human_wins} times!!")
        print("Thank you for playing")
        break

    elif user_choice == comp_choice:
        print("It is Tie!Try again")
    elif user_choice == "rock"  and comp_choice == "scissor":
        print("You Win!")
        human_wins += 1
    elif user_choice == "rock"  and comp_choice == "paper":
        print("You Lost!")
        comp_wins += 1
    elif user_choice == "paper"  and comp_choice == "scissor":
        print("You Lose!")
        comp_wins += 1
    elif user_choice == "paper"  and comp_choice == "rock":
        print("You Win!")
        human_wins += 1
    elif user_choice == "scissor"   and comp_choice == "rock":
        print("You Lost!")
        comp_wins += 1
    elif user_choice == "scissor"  and comp_choice == "paper":
        print("You Win!")
        human_wins += 1
    else:
        print("Invalid choice")
