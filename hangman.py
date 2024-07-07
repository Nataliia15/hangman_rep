from words import words_list as words
import random
import string

def get_valid_word(words):
    word=random.choice(words)
    while "-" in words or ' 'in words:
        word=random.choice(words)
    return word
def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_lowercase)
    used_letters=set()
    lives=6
    while len(word_letters)>0 and lives>0:
        #used letters
        print("You have ", lives," and you have used these letters: ", " ".join(used_letters))
        #what current word is
        word_list=[letter if letter in used_letters else "-" for letter in word]
        print("Curent word: ", " ".join(word_list))
        user_letter=input("Guess a letter: ")

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)


            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print("Letter is not in the word!")

        elif user_letter in used_letters:
            print("You already guessed that letter. please try again.")
        else:
            print("Invalid character!")

    if lives==0:
        print("Sorry you are died!")
    else:
        print("You guessed the word!")
hangman()