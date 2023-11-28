import random

def choose_word():
    words = ["python", "programming", "computer", "game", "challenge"]
    return random.choice(words)

def shuffle_word(word):
    shuffled_word = list(word)
    random.shuffle(shuffled_word)
    return "".join(shuffled_word)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_hint(word, guessed_letters):
    available_hints = [letter for letter in word if letter not in guessed_letters]
    if not available_hints:
        return None
    return random.choice(available_hints)

def main():
    print("Welcome to the Word Guessing Game!")
    secret_word = choose_word()
    shuffled_word = shuffle_word(secret_word)
    guessed_letters = []
    attempts = 6  # You can adjust the number of attempts

    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(shuffled_word, guessed_letters)
        print("Shuffled word:", current_display)

        guess = input("Guess a letter or type 'hint' for a hint: ").lower()

        if guess == 'hint':
            hint = get_hint(secret_word, guessed_letters)
            if hint:
                print(f"Hint: Try the letter '{hint}'.")
            else:
                print("No more hints available.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print("Incorrect guess!")
            attempts -= 1
        else:
            print("Correct guess!")

        if "_" not in display_word(shuffled_word, guessed_letters):
            print("Congratulations! You guessed the word:", secret_word)
            break

    if "_" in display_word(shuffled_word, guessed_letters):
        print("Sorry, you're out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    main()