import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")#Take user input
    possible_action = ["rock", "paper", "scissors"]
    #using random function
    computer_action = random.choice(possible_action)
    print(f"\nYou chose {user_action}, computer chose {computer_action}")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. Its a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win")
        else:
            print("Paper covers rock! You lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes paper. You lose")
    play_again = input("Play again? (y/n)")
    if play_again != "y":
        break