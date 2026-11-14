# steps:
# -1 user enter a string 
# -2 the program must vailed from the first letter that is not repated!
# -3 print the FIRST non repating letter

def non_repating():
    close = False
    user = input("Enter your sentence : ")#leetcode
    letters = []
    letters.extend(user)#leetcode
    for letter in letters:
        if letters.count(letter) >= 2 :
            close = True
        else:
            print("="*40)
            print(f'The first letter that never repeted is : {letter}')
            print(f'and its index is : {letters.index(letter)}')
            break
    if close == True:
        print('None')
        


non_repating()
