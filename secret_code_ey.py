import string
import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def sleep():
    time.sleep(2)

def encode():
    clear()
    sleep()
    user_sentence = input("Enter your sentence : ")# Eyad hossam
    user_num = int(input("Enter your secret number : "))

    sentence = []
    sentence.extend(user_sentence)
    new_sentence = []
    letters = (string.ascii_lowercase)
    for letter in sentence:# E
        if letter in letters:#true
            new_sentence.append(letters[(letters.index(letter) + user_num)%len(letters)])
        else:
            new_sentence.append(letter)
    if user_num == string.ascii_letters:
        print('Please enter a number')
        sleep()
        clear()
    result = "".join(new_sentence)
    print(f' your secret code is : {result}')
    sleep()


def decode():
    clear()
    sleep()
    user_sentence = input("Enter your sentence : ")# eyad hossam
    user_num = int(input("Enter your secret number : "))

    sentence = []
    sentence.extend(user_sentence)
    new_sentence = []
    letters = (string.ascii_lowercase)
    for letter in sentence:
        if letter in letters:
            new_sentence.append(letters[(letters.index(letter) - user_num)%len(letters)])
        else:
            new_sentence.append(letter)
    result = "".join(new_sentence)
    print(f'your original code is : {result}')
    sleep()


def secret_code():
    while True:
        print("=====( Welcome to secret code generator )=====")
        print('1) encode')
        print('2) decode ')
        print('3) Exit')
        user_choice = input("please enter (1) , (2) or (3) : ")

        if user_choice == '1':
            encode()
        elif user_choice == '2':
            decode()
        elif user_choice == '3':
            print('closing the program........')
            break
        else:
            clear()
            print('Please enter (1) , (2) or (3)')
            sleep()


secret_code()