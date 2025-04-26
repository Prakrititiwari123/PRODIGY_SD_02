import random

def guessing_game():
    secret_number = random.randint(1, 100) 
    attempts = 0

    print("\n🎯 Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it? 🤔")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))  
            attempts += 1  

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed it right in {attempts} attempts! 🏆")
                break  

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Run the Game
guessing_game()
