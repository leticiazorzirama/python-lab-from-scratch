def get_user_move(n, m):
    """
    Asks the user how many pieces to remove and validates the move.
    """
    try:
        user_move = int(input("How many pieces will you take? "))
        if user_move > m or user_move <= 0 or user_move > n:
            print("Oops! Invalid move! Try again.")
            return get_user_move(n, m)
        return user_move
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_move(n, m)

def get_computer_move(n, m):
    """
    Determines the computer's move based on the optimal strategy.
    """
    for move in range(1, m + 1):
        if (n - move) % (m + 1) == 0:
            return move
    return min(n, m)

def print_user_status(user_move, n):
    """
    Prints the game status after the user's move.
    """
    print(f"You removed {user_move} piece(s).")
    print(f"{n} piece(s) remaining on the board.")

def print_computer_status(computer_move, n):
    """
    Prints the game status after the computer's move.
    """
    print(f"The computer removed {computer_move} piece(s).")
    if n > 0:
        print(f"{n} piece(s) remaining on the board.")
    else:
        print("Game over! The computer wins!")

def play_again():
    """
    Asks the user if they want to play again.
    Returns True if yes, False otherwise.
    """
    answer = input("Do you want to return to the main menu? (y/n): ").strip().lower()
    if answer == 'y':
        return True
    elif answer == 'n':
        print("Thanks for playing!")
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return play_again()

def single_game():
    """
    Runs a single game of NIM.
    """
    try:
        n = int(input("How many pieces? "))
        m = int(input("Maximum pieces per move? "))
        if n <= 0 or m <= 0:
            print("Values must be greater than zero. Restarting game...")
            return single_game()
    except ValueError:
        print("Invalid input. Please enter integers.")
        return single_game()

    if n % (m + 1) == 0:
        print("You start!")
        user_turn = True
    else:
        print("Computer starts!")
        user_turn = False

    while n > 0:
        if user_turn:
            move = get_user_move(n, m)
            n -= move
            print_user_status(move, n)
        else:
            move = get_computer_move(n, m)
            n -= move
            print_computer_status(move, n)
        user_turn = not user_turn

def championship():
    """
    Runs a championship of 3 games and displays the final score.
    """
    print("**** Round 1 ****")
    single_game()
    print("**** Round 2 ****")
    single_game()
    print("**** Round 3 ****")
    single_game()
    print("**** End of the championship! ****")
    print("Final Score: You 0 x 3 Computer")

def main():
    """
    Entry point for the NIM game. Allows user to select game mode or exit.
    """
    while True:
        print("\nWelcome to the game of NIM! Choose:")
        print("1 - to play a single game")
        print("2 - to play a championship")
        print("3 - to exit the game")

        choice = input("Your choice: ").strip()
        if choice == "1":
            print("You chose a single game!")
            single_game()
            if not play_again():
                break
        elif choice == "2":
            print("You chose a championship!")
            championship()
            if not play_again():
                break
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid option! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
