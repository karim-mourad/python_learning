import random
from hangman_words import word_list
from hangman_art import logo , hangman_stages

lives = 6

print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word)
word_length = len(chosen_word)
placeholder = ""
for position in range(word_length) :
    
    placeholder += "_ "

print(f"Word to guess {placeholder}")

game_over = False

correct_letters = []


while not game_over :
    print(f"***************************************{lives}/ 6 LIVES LEFT***************************************")
    guess = input("Guess a letter : ").lower()
    
    if guess in correct_letters :
        
        print(f"You've already gussed {guess}")
        
    display = ""
    
    for letter in chosen_word :
        
        if letter == guess :
            
            display += letter + " "
            correct_letters.append(letter)
            
        elif letter in correct_letters :
            
            display += letter + " "
            
        else :
            
            display += "_ "
            
    print(display)
    
    if guess not in chosen_word :
        
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
    print(hangman_stages[6 - lives])
        
    if lives == 0 :
        
        print(f"***************************************IT WAS {chosen_word}!! YOU LOSE!!***************************************")
        game_over = True
        
    if "_ " not in display :
        print("***************************************YOU WIN!!***************************************")
        game_over = True
        
    
    