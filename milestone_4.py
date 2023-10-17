import random

class hangman:
    def __init__(self, word_list, num_lives = 5) -> None:
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

        def check_guess(guess):
            guess = guess.lower()
            if guess in self.word:
                print(f'Good guess! {guess} is in the word.')
                for letter in self.word:
                    if guess == letter:
                        self.word_guessed[self.word.index(guess)] = guess
                self.num_letters -= 1
            else:
                print(f'Sorry, {guess} is not in the word. Try again')
                self.num_lives -=1
                print(f"You have {self.num_lives} lives left.")

        def ask_for_input():
            print("Please guess a letter")
            while True:
                guess = input()
                if not (guess.isalpha() and len(guess) == 1) :
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    check_guess(guess)
                    self.list_of_guesses.append(guess)         


        ask_for_input()
    
