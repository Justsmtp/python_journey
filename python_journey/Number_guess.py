import random

print("🎲 Welcome to the Number Guessing Game!")

play_again = "yes"

while play_again.lower() == "yes":
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0

    print("\nI'm thinking of a number between 1 and 10. Can you guess it?")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            match guess:
                case n if n == secret_number:
                    print(f"🎉 Congratulations, you guessed it in {attempts} tries!")
                case n if n > secret_number:
                    print("Oops, your guess is a bit high. Try again!")
                case n if n < secret_number:
                    print("Nope, your guess is a bit low. Give it another shot!")
        except ValueError:
            print("Please enter a valid number.")

    play_again = input("\nPlay again? (yes/no): ")

print("\nThanks for playing! Goodbye! 👋")
