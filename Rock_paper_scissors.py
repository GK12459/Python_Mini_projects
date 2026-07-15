import random
list_ = ["rock", "paper", "scissor"]
computer_score = player_score = 0

while (computer_score < 5 and player_score < 5):
    print("\n\t--------ROCK PAPER SCISSOR-------")
    print("You have to choose from the options: 'rock' or 'scissor' or 'paper' or 'exit'.")
    print("First to 5 points wins the game.")
    computer_choice = random.choice(list_)
    player_choice = input("\nEnter your choice: ").lower()
    if(player_choice in list_):
        if(computer_choice == player_choice):
            print(f"\nBoth played '{computer_choice}'.")
            print(f"Computer: {computer_score}\t\tYou: {player_score}\n")
        elif(computer_choice == 'rock' and player_choice == 'scissor'):
            computer_score += 1
            print(f"\nComputer played '{computer_choice}' : You played '{player_choice}'")
            print(f"Computer: {computer_score}\t\tYou: {player_score}\n")
        elif(computer_choice == 'paper' and player_choice == 'rock'):
            computer_score += 1
            print(f"\nComputer played '{computer_choice}' : You played '{player_choice}'")
            print(f"Computer: {computer_score}\t\tYou: {player_score}\n")
        elif(computer_choice == 'scissor' and player_choice == 'paper'):
            computer_score += 1
            print(f"\nComputer played '{computer_choice}' : You played '{player_choice}'")
            print(f"Computer: {computer_score}\t\tYou: {player_score}\n")
        else:
            player_score += 1
            print(f"\nComputer played '{computer_choice}' : You played '{player_choice}'")
            print(f"Computer: {computer_score}\t\tYou: {player_score}\n")

        if(computer_score < 5 and player_score < 5):
            try:
                input("Press Enter to proceed!")
            except:
                pass

    elif(player_choice == "exit"):
        print("\nHave you scared to play further?")
        print("I take it as yes!\nBye.\n")
        break
    else:
        print("Invalid input!\n")

if(computer_score == 5):
    print("\nComputer won!\nBetter luck next time!\n")
if(player_score == 5):
    print("\nHurray! You won!\nYou got lucky this time.\n")