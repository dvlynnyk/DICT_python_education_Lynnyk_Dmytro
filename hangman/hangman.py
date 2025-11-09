import random

def validate_letter(letter, guessed):
    """
    Validate a user's input character for correctness.

    Parameters:
        letter (str): User input.
        guessed (set): Set of already guessed letters.

    Returns:
        tuple(bool, str):
            - True and the letter itself if input is valid.
            - False and an error message if invalid.
    """
    if len(letter) != 1:
        return False, "You should input a single letter"
    if not letter.isalpha() or not letter.islower():
        return False, "Please enter a lowercase English letter"
    if letter in guessed:
        return False, "You've already guessed this letter"
    return True, letter

def reveal_letters(secret_word, hidden_word, letter):
    """
    Reveal all occurrences of a guessed letter in the hidden word.

    Parameters:
        secret_word (str): The original word to guess.
        hidden_word (str): The masked version of the word.
        letter (str): The correctly guessed letter.

    Returns:
        str: Updated hidden word with revealed positions.
    """
    result = ""
    for i, ch in enumerate(secret_word):
        result += letter if ch == letter else hidden_word[i]
    return result

def play():
    """
    Run a single game session of Hangman.

    Game rules:
    - Player attempts to guess a randomly chosen word.
    - Player inputs letters one-by-one.
    - Player has 8 incorrect attempts ("lives").
    - Game ends in a win when all letters are revealed, or a loss when lives reach 0.
    """
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)
    hidden = "-" * len(secret_word)
    lives = 8
    guessed = set()

    while lives > 0:
        print(hidden)
        letter = input("Input a letter: > ").lower()

        # Validate input correctness
        ok, result = validate_letter(letter, guessed)
        if not ok:
            print(result)
            continue

        letter = result
        guessed.add(letter)

        # Reveal letters or reduce life
        if letter in secret_word:
            hidden = reveal_letters(secret_word, hidden, letter)

            if hidden == secret_word:
                print(f"You guessed the word {secret_word}!")
                print("You survived!")
                return
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

    print("You lost!")

def main():
    """
    Display the main menu and wait for user command.

    Commands:
        play  - start a new game
        exit  - quit the program
    """
    print("HANGMAN")
    while True:
        action = input('Type "play" to play the game, "exit" to quit: > ').lower()
        if action == "play":
            play()
        elif action == "exit":
            break

if __name__ == "__main__":
    main()