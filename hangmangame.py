import random

def choose_word():
    words = ["srikakulam","kadapa","eluru","krishna","chittoor"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += " "
    return display

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    max_attempts = 8
    attempts = 0

    print("Word related to district in ap")

    while True:
        print("Attempts left:", max_attempts - attempts)
        current_display = display_word(secret_word, guessed_letters)
        print("Current word:", current_display)

        if current_display == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
                attempts += 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

        if attempts == max_attempts:
            print("Sorry, you lost the attempts")
            break

if __name__ == "__main__":
    hangman()
