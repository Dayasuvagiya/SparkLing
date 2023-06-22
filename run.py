import time
import sys

def welcome_mess():
    """Creates a welcome message"""
    print("######################################")
    print("#                                    #")
    print("#     Let's begin ZodiacJourney      #")
    print("#    ---------------------------     #")
    print("#                                    #")
    print("######################################")
    time.sleep(1)
    print(" ")

    time.sleep(1)
    print("Unlock Your Cosmic Blueprint - Discover Your Zodiac Sign Today!")
    time.sleep(1)
    print("Do you want to know your Zodiac sign?")
    time.sleep(1)
    print("Let's start:)")
    time.sleep(1)
    print("^_^")
    time.sleep(1)


#class User():
 #   """Creates an instance to take user name"""
  #  def __init__(self, name):
   #     self.name=name  

def Zodiac_sign(letter):
    """Define dictionary to show zodiac sign"""
    zodiac_alphabets = {
         'bh':'Sagittarius', 'f':'Sagittarius', 'dh':'Sagittarius', 
         'p':'Virgo', 'tha':'Virgo', 
         'dd':'Cancer', 'h':'Cancer', 
         'g':'Aquarius', 's':'Aquarius', 'sh':'Aquarius', 
         'kh':'Capricorn', 'j':'Capricorn', 
         'd':'Pisces', 'ch':'Pisces', 'z':'Pisces', 'th':'Pisces', 
         'a':'Aries', 'l':'Aries', 'e':'Aries', 'i':'Aries', 'o':'Aries', 
         'k':'Gemini', 'chh':'Gemini', 'gh':'Gemini', 'q':'Gemini', 'c':'Gemini', 
         'm':'Leo', 'tt':'Leo', 
         'r':'Libra', 't':'Libra', 
         'b':'Taurus', 'v':'Taurus', 'u':'Taurus', 'w':'Taurus', 
         'n':'Scorpio', 'y':'Scorpio'
    }
    #User input convert to lowercase
    lower_case = lower_case.lower()

    #If statment to look up zodiac sign of each letter
    for key, value in zodiac_alphabets.items():
        if key == letter:
            print(value)
        else:
            return None



def user_name():
    """Display menu for user to select one option"""

    while True:
        print("MENU:")
        print("1. Discover Your Zodiac Identity Through Your Name!.")
        print("2. Read the importance of your Zodiac sign.")
        print("3. Exit program.")
        # User options for further steps 
        user_selection=input("Enter your choice (1, 2, or 3)/n")
        
        if user_selection == "1":
            name_letter=input("Please enter first letter of your name/n")
            rashi = Zodiac_sign(name_letter)
            print(rashi)

        elif user_selection =="2":
            file = open('requirements.txt') 
            importances=file.read()
            file.close()
            print(importances)
        elif user_selection == "3":
            # Exit
            print("I appreciate your utilization of this program!/n")
            break  
        else:
            # user selection is not valid
            print("The selection is invalid. Please select again.") 


if __name__ == '__main__':
    welcome_mess()
    user_name()