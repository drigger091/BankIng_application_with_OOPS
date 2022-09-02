#Banking ystem using oop
# Parent class = User
# hold details of an user
# have a function to show user details
#child class = Bank
#stores details about the amint balance
#shows and displays details of the account
#allows deposits ,withdrswals and balance



class User():
    def __init__(self,name ,age ,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("Personal Details")
        print("Name",self.name)
        print("Age",self.name)
        print("Gender",self.gender)
    
    