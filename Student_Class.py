from datetime import date

class Student:

    def __init__(self,id,name,dob,class):
        self.__studentid = id
        self.__name = name
        self.__dob = dob
        self.__class = classification 
        self.__age = 0
        self.__register = ''

    def return_age(self):
        return self.__age

    def return_registration(self):
        return self.__register

    def register(self):
        if self.__class == 'Senior':
            self.__register = '11/1 thru 11/3'
        elif self.__class == 'junior':
            self.__register = '11/4 thru 11/6'
        elif self.__class == 'Sophomore':
            self.__register = '11/7 thru 11/9'
        elif self.__class == 'Freshman':
            self.__register = '11/10 thru 11/12'
        else:
            self.__register = 'classification not found'

    
    def calc_age(self):
        today = date.today()
        birthdate = self.__dob.split('/')
        birthdate_year = int(birthdate[2])

        age = today.year - birthdate_year
        
