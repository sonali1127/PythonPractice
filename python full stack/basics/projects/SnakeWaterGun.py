import random

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "tie"
    
    if (player1_choice == 0 and player2_choice == 1) or (player1_choice == 1 and player2_choice == 2) or (player1_choice == 2 and player2_choice == 0):
        return "player1"
    else:
        return "player2"

def get_player_choice(player_name):
    while True:
        try:
            choice = int(input(f"{player_name}, enter your choice (0 for Snake, 1 for Water, 2 for Gun): "))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid choice. Please choose 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game(player1_name, player2_name):
    if player2_name == '0':
        player2_choice = random.randint(0, 2)
    else:
        player2_choice = get_player_choice(player2_name)
    
    player1_choice = get_player_choice(player1_name)
    
    choices = {0: "Snake", 1: "Water", 2: "Gun"}
    print(f"{player1_name} chose {choices[player1_choice]}.")
    print(f"{player2_name} chose {choices[player2_choice]}.")
    
    result = determine_winner(player1_choice, player2_choice)
    
    if result == "player1":
        print(f"{player1_name} wins this round!")
    elif result == "player2":
        print(f"{player2_name} wins this round!")
    else:
        print("This round is a tie!")
    
    return result

def main():
    print("Welcome to Snake, Water, Gun Game!")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name (or type '0' for single-player): ")
    
    while True:
        try:
            rounds = int(input("How many times do you want to play the game (1, 2, 5, or 10)? "))
            if rounds in [1, 2, 5, 10]:
                break
            else:
                print("Invalid choice. Please choose 1, 2, 5, or 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    player1_score = 0
    player2_score = 0
    tie_score = 0
    
    for i in range(rounds):
        print(f"\nRound {i + 1}:")
        result = play_game(player1_name, player2_name)
        
        if result == "player1":
            player1_score += 1
        elif result == "player2":
            player2_score += 1
        else:
            tie_score += 1
        
        print(f"Current Scores: {player1_name}: {player1_score}, {player2_name}: {player2_score}, Ties: {tie_score}")
        
        if i < rounds - 1:
            exit_choice = input("Do you want to continue? (Press '0' to exit or any other key to continue): ")
            if exit_choice == '0':
                print("Exiting the game early.")
                break
    
    print("\nFinal Results:")
    print(f"{player1_name}: {player1_score} wins")
    print(f"{player2_name}: {player2_score} wins")
    print(f"Ties: {tie_score}")
    
    if player1_score > player2_score:
        print(f"{player1_name} is the overall winner!")
    elif player2_score > player1_score:
        print(f"{player2_name} is the overall winner!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    main()