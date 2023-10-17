import random

class hangman:
    def __init__(self, word_list, num_lives = 5) -> None:
        word = random.choice(word_list)
        word_guessed = len(word) * ['_']
        num_letters = len(set(word))
        num_lives = num_lives
        list_of_guesses = []

        def check_guess(guess):
            guess = guess.lower()
            if guess in word:
                print(f'Good guess! {guess} is in the word.')
                for letter in word:
                    if guess == letter:
                        word_guessed[word.index(guess)] = guess
                num_letters -= 1
                print(word_guessed)
            else:
                print(f'Sorry, {guess} is not in the word. Try again')

        def ask_for_input():
            print("Please guess a letter")
            print(num_letters)
            while True:
                guess = input()
                if not (guess.isalpha() and len(guess) == 1) :
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in list_of_guesses:
                    print("You already tried that letter!")
                else:
                    check_guess(guess)
                    list_of_guesses.append(guess)         


        ask_for_input()
    
c = hangman(["apple"])
