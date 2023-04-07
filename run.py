import random
from words import word_list


# First steps to invite in the game:

def get_word():
    """
    Adds new words into the game
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    Tells whether the word/letters are correct or incorrect
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\n Welcome to Hangman game \n")
    name = input("Enter your name: ")
    print("Hello " + name + "! Best of Luck!")
    print("The game is about to start!\n")
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, char in enumerate(word) if char == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    """
    Descirbes all the steps in hangman
    """
    stages = {
        0: """
                ___________
               | /        |
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        |
               |/        ( )
               |          |
               |         /
               |
            """,
        2: """
                ___________
               | /        |
               |/        ( )
               |          |
               |
               |
            """,
        3: """
                ___________
               | /        |
               |/        ( )
               |
               |
               |
            """,
        4: """
                ___________
               | /        |
               |/
               |
               |
               |
            """,
        5: """
                ___________
               | /
               |/
               |
               |
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
    return stages[tries]


def main():
    """
    Takes up new words for the next game
    """
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
