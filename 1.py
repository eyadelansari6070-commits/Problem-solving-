class Profile:
    def __init__(self,name,email,lang):
        self.name = name
        self.email = email
        self.lang = lang


profile1 = Profile('Eyad',"eyadelansari6070@gmal.com","germany")
profile2 = Profile("Rana","rana@gmail.com","English")
profile3  = Profile("Sara",'sara@gmail.com','japaness')

print(f'Profile1 name is {profile1.name}')
print(f"Profile2 language is {profile2.lang}")
print(f'Profile3 email is {profile3.email}')