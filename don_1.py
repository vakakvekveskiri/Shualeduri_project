
import random

def hangman():
    words = ["python", "hangman", "programming", "challenge", "developer", "algorithm"]
    word_to_guess = random.choice(words).lower()  # Randomly select a word
    guessed_word = ["_"] * len(word_to_guess)  # Create a placeholder for the word
    attempts_left = 6  # Number of incorrect attempts allowed
    guessed_letters = []  # Keep track of guessed letters

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect attempts before you lose.")
    print(" ".join(guessed_word))

    while attempts_left > 0:
        guess = input("\nEnter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            # Reveal the guessed letter in the correct positions
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
            print("Good job! That letter is in the word.")
        else:
            attempts_left -= 1
            print(f"Wrong guess. You have {attempts_left} attempts left.")

        # Display the current state of the guessed word
        print(" ".join(guessed_word))

        # Check if the player has guessed the entire word
        if "_" not in guessed_word:
            print(f"\nCongratulations! You guessed the word '{word_to_guess}' correctly.")
            break
    else:
        print(f"\nGame over! The word was '{word_to_guess}'. Better luck next time!")

    return (hangman())



