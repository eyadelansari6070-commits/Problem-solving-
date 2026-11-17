# Reversed word
def word_reverse():
    user = input("Enter your word : ")
    if user[::-1] == user:
        print(f'This word can be reversed : {user}')
    else:
        print(f'This word cant be reversed : {user} => {user[::-1]}')


word_reverse()
