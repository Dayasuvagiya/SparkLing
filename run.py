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


def user_name():
    """Display menu for user to select one option"""

    while True:
        print("/nMENU:")
        print("1. Discover Your Zodiac Identity Through Your Name!.")
        print("2. Read the importance of your Zodiac sign.")
        print("3. Exit program.")
        
        user_selection=input("Enter your choice (1, 2, or 3)")
    
        if user_selection =="1":


welcome_mess()

user_name()