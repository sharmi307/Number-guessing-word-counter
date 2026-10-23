
import random
import string

def number_guessing_game():
    print("\n=== NUMBER GUESSING GAME ===")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number (1-100): "))

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You won in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def word_counter():
    print("\n=== WORD COUNTER ===")
    text = input("Enter your text: ")

    words = text.split()
    characters = len(text)
    characters_without_spaces = len(text.replace(" ", ""))
    sentences = sum(
        1 for char in text if char in ".!?"
    )
    paragraphs = len([
        p for p in text.split("\n") if p.strip()
    ])

    print("\n--- TEXT ANALYSIS ---")
    print("Words:", len(words))
    print("Characters (including spaces):", characters)
    print("Characters (excluding spaces):",
          characters_without_spaces)
    print("Sentences:", sentences)
    print("Paragraphs:", paragraphs)


def main():
    while True:
        print("\n===== PYTHON MINI PROJECTS =====")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
