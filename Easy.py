class Recipe():
    def __init__(self,name,ingredients,time,instruction):
        self.name = name
        self.ingredients = ingredients
        self.time = time 
        self.instruction = instruction
def start_menu():
    print("Welcome to recipe collection:")
    print('\n')
    name = input("Enter recipe name : ")
    ingredients = input("Enter ingredients (comma separeted!) : ")
    time = input("Enter cooking time : ")
    instruction = input("Enter cooking instruction :  ")
    print("Recipe added successfuly!")
    print("\n")
    print("Displaying recipe.....")
    return Recipe(name,ingredients,time,instruction)

recipe1 = start_menu()

def display():
    print(f"Name : {recipe1.name}\nIngredients : {recipe1.ingredients}\nTime : {recipe1.time}\nInstruction : {recipe1.instruction}")
    print('-'*40)

display()