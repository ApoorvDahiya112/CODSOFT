import random

def play_rock_paper_scissors():
    """
    A simple Rock Paper Scissors game where user plays against computer.
    Returns None, but prints the game results.
    """
    # Valid moves
    VALID_MOVES = ["Rock", "Paper", "Scissors"]
    
    # Game rules: key beats value
    RULES = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }
    
    while True:
        # Get user input
        print("\nValid moves:", ", ".join(VALID_MOVES))
        user_choice = input("Enter your move: ").strip().capitalize()
        
        # Input validation
        if not user_choice:
            print("Please enter your move.")
            continue
        if user_choice not in VALID_MOVES:
            print("Invalid input! Please choose from:", ", ".join(VALID_MOVES))
            continue
        
        # Generate computer's choice
        computer_choice = random.choice(VALID_MOVES)
        
        # Display choices
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("\nIt's a tie! Both chose", user_choice)
        elif RULES[user_choice] == computer_choice:
            print(f"\n{user_choice} beats {computer_choice}")
            print("🎉 You win! 🎉")
        else:
            print(f"\n{computer_choice} beats {user_choice}")
            print("Computer wins!")
        
        # Ask to play again
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    play_rock_paper_scissors()