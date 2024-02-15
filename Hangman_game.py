import random as r
import hangman_stages
word_list = ['Apple', 'apple', 'krishna', 'Ram', 'banana', 'Banana', 'Strawberry', 'Delhi', 'Mumbai', 'India']
word = r.choice(word_list)
lives = 6
display = []
for letters in word:
    display += '_'
print(display)
game_over = False
while not game_over:
    guess_letter = input('Guess a letter that might be present the word gussed by me : ')
    for position in range(len(word)):
        if guess_letter == word[position]:
            display[position] = guess_letter
        elif guess_letter.upper() == word[position]:
            display[position] = guess_letter.upper()
    print(display)
    if guess_letter not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You lose !!')
            print('The correct word was : ', word)
    if '_' not in display:
        game_over = True
        print('You won !!')
    print(hangman_stages.hangman[lives])