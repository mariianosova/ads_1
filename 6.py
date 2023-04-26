import random

word_list = ["код", "яблоко", "банан", "имя", "вешалка", "информатика", "функция", "вулкан", "утюг", "мышь"]
chosen_word = random.choice(word_list)
display = "_" * len(chosen_word)

remaining_guesses = 10

guessed_letters = []

def update_display(chosen_word, display, letter):
    new_display = ""
    for i in range(len(chosen_word)):
        if chosen_word[i] == letter:
            new_display += letter
        else:
            new_display += display[i]
    return new_display

while remaining_guesses > 0:
    print(display)
    print("угадайте букву")
    guess = input().lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("введите одну букву")
        continue
    
    if guess in guessed_letters:
        print("вы уже угадали эту букву")
        continue
    guessed_letters.append(guess)
    
    if guess in chosen_word:
        display = update_display(chosen_word, display, guess)
        if display == chosen_word:
            print(display)
            print("вы выиграли!")
            break
    else:
        remaining_guesses -= 1
        print("такой буквы нет в слове. осталось", remaining_guesses, "попыток")
    
if remaining_guesses == 0:
    print("вы проиграли! загаданное слово было", chosen_word)
