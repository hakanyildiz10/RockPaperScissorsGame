import random
import time
import threading

def print_intro():
    print("Here is Rock, Paper, Scissors Game...")
    print("You are gonnna play against the computer.")
    print("The rules are straightforward:")
    print("Rock beats Scissors")
    print("Scissors beat Paper")
    print("Paper beats Rock")
    print("You will choose one of these options within 7 seconds and the computer will choose one as well.")
    print("Game is consist of 2 rounds.")
    print("If your and computer's round scores are 2-0 and 1-0, you will the game. Vice versa you will lose")
    print("If your and computer's round scores 1-1, it will tie")
    print("Good luck!")

def get_user_choice_with_timeout(timeout=7):
    user_choice = [None]  # Using a list to allow modification inside thread
    start_time = [None]  # Using a list to keep track of start time inside thread

    def get_input():
        start_time[0] = time.time()
        user_choice[0] = input("Enter your choice (rock, paper, scissors): ").lower()

    # Start a thread to get user input
    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    # Wait for the input thread to finish or timeout
    input_thread.join(timeout)
    if user_choice[0] is None:
        print("Time's up! You took too long to respond.")
        return None

    end_time = time.time()
    elapsed_time = end_time - start_time[0]
    print(f"You took {elapsed_time:.2f} seconds to make your choice.")
    
    # Ensure user input is valid
    while user_choice[0] not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose again.")
        user_choice[0] = input("Enter your choice (rock, paper, scissors): ").lower()
        end_time = time.time()  # Reset end time if user inputs invalid choice
        elapsed_time = end_time - start_time[0]
        print(f"You took {elapsed_time:.2f} seconds to make your choice.")
    
    return user_choice[0]

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = get_user_choice_with_timeout()
    if user_choice is None:
        print("You missed the time limit. You lose this round!")
        computer_choice = get_computer_choice()
        return "computer", None  # Default result for timeout
    computer_choice = get_computer_choice()
    print(f"\nYou chose {user_choice}, and the computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("You lose this round!")
    return result, (user_choice, computer_choice)

def play_game():
    print_intro()
    user_score = 0
    computer_score = 0
    round_results = []  # List to store the results of each round

    for round_number in range(1, 3):  # Limiting to 2 rounds
        print(f"\nRound {round_number}")
        result, choices = play_round()
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        round_results.append((round_number, result, choices))
        print(f"Score: You {user_score} - {computer_score} Computer")

    print("\nFinal Game Results:")
    for round_result in round_results:
        round_number, result, choices = round_result
        user_choice, computer_choice = choices if choices else ("N/A", "N/A")
        print(f"Round {round_number}: You chose {user_choice}, Computer chose {computer_choice}. Winner: {result.capitalize()}")

    if user_score > computer_score:
        print("\nYou won the game!")
    elif user_score < computer_score:
        print("\nYou lost the game!")
    else:
        print("\nThe game is a tie!")

def ask_play_again(player):
    if player == "user":
        while True:
            replay = input(f"\n{player.capitalize()}, do you want to play again? (yes/no): ").lower()
            if replay in ["yes", "no"]:
                return replay == "yes"
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    elif player == "computer":
        computer_decision = random.choice(["yes", "no"])
        print(f"\nThe computer chooses to {'continue' if computer_decision == 'yes' else 'stop'} playing.")
        return computer_decision == "yes"

def tas_kagit_makas_HAKAN_YILDIZ():
    while True:
        play_game()
        
        # Ask the user if they want to play again
        user_wants_to_play = ask_play_again("user")
        
        # Ask the computer if it wants to play again
        computer_wants_to_play = ask_play_again("computer")
        
        # If either the user or the computer wants to stop, end the game
        if not user_wants_to_play or not computer_wants_to_play:
            print("Thanks for playing! Goodbye!")
            break

# Call the function to start the game
tas_kagit_makas_HAKAN_YILDIZ()
