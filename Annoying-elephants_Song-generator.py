def annoy(n):
    # Base case: if n is less than 1, return an empty string
    if n < 1:
        return ""

    # Recursive case: repeat "annoy " n times
    return "annoy " + annoy(n - 1)


def elephants(n):
    # Base case: if n is less than 1, return an empty string
    if n < 1:
        return ""

    # First line when n == 1
    if n == 1:
        return "One elephant annoys a lot of people.\n"

    # Build the two parts for n > 1
    part1 = f"{n - 1} elephants annoy a lot of people.\n"
    part2 = f"{n} elephants {annoy(n)}much more.\n"

    # When n == 2, skip part1 to match the expected format
    if n == 2:
        return elephants(n - 1) + part2

    # Recursive call assembling the full song
    return elephants(n - 1) + part1 + part2


# Entry point of the script
if __name__ == "__main__":
    print("🎵 Welcome to the Elephant Song Generator! 🎵\n")
    print("This program generates the traditional 'Elephants Annoying' song.")
    print("Enter the number of elephants to generate the song (or 0 to exit).")

    while True:
        try:
            user_input = int(input("Enter the number of elephants (or 0 to exit): "))
            
            if user_input == 0:
                print("\n👋 Goodbye! Thanks for using the Elephant Song Generator.")
                break
            elif user_input < 0:
                print("⚠️ Please enter a number zero or greater.\n")
            else:
                print("\nHere is your song:\n")
                print(elephants(user_input))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")
