import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"
def play_game():
    wins = 0
    losses = 0
    draws = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to stop the game.\n")
    while True:
        player_choice = input("Your choice: ").lower()
        if player_choice == "exit":
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        if result == "player":
            print("You win this round!")
            wins += 1
        elif result == "computer":
            print("Computer wins this round!")
            losses += 1
        else:
            print("It's a draw!")
            draws += 1
        print()
    print("\nGame Over!")
    print(f"Total Wins: {wins}")
    print(f"Total Losses: {losses}")
    print(f"Total Draws: {draws}")
if __name__ == "__main__":
    play_game()
