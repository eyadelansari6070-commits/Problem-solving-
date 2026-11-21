class Member():
    bad_words = ['fuck','shit','dick']

    def __init__(self,first_name,last_name,gender,age):
        self.first_name = first_name
        self.last_name = last_name 
        self.gender = gender
        self.age = age

    def bad(self):
        if self.first_name in Member.bad_words:
            print("This is illigal try differernd name!")

    def show(self):
        if self.gender == 'male':
            return f'Hi MR {self.first_name} your full name is {self.first_name} {self.last_name} your gender is {self.gender} and you have {self.age} years old :'
        elif self.gender == 'female':
            return f'Hi Miss {self.first_name} your full name is {self.first_name} {self.last_name} your gender is {self.gender} and you have {self.age} years old :'
        else:
            return f'Hi {self.first_name} your full name is {self.first_name} {self.last_name} your gender is {self.gender} and you have {self.age} years old :'


user1 = Member('Eyad','Hossam','male',15)
user2 = Member('shit','ibrahim','male',46)
user3 = Member('rodina','malk','female',29)

print(user2.bad())
        


        