import random

word_list = ['orange', 'banana','watermelon','strawberry','kiwi']
#print(word_list)

#print(random.choice(word_list))
word = random.choice(word_list)
print(word)

print('enter a letter')
guess = input()

if len(guess) == 1 and guess.isalpha():
    print('Good Guess')
else:
    print('Oops! That is not a valid input') 

  

git remote add https://github.com/z3nk0v/hangman/tree/9078562f4cac3f0796e8384b72b75cc03b4a49d9/hangman