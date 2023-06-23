import time


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
    print("Let's start")
    time.sleep(1)
    print("^_^\n")
    time.sleep(1)
  

def zodiac_sign(letter):
    """Define dictionary to show zodiac sign,
    Convert user input in lower case,
    loop and if statment to show output"""

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
         'n':'Scorpio', 'y':'Scorpio', 'x':'No Zodiac sign for this letter'
    }
    #User input convert to lowercase
    lower_case = letter.lower() 
    # Look up zodiac sign of each letter
    for key, value in zodiac_alphabets.items():
        if key == lower_case:
            return f"Your Zodiac sign is '{value}'"
        
    return """No data found please enter correct character,
    For Instance: 
    Your name is 'John', enter 'j' or 'J'"""
 

def user_name():
    """Display menu for user to select one option,
    According to user choice give the relevant response"""

    while True:
        print("MENU:")
        print("1. Discover your Zodiac identity through your name.")
        print("2. Read the importance of the Zodiac sign.")
        print("3. Exit program.")
        # User options for further steps 
        user_selection=input("Enter your choice (1, 2, or 3)\n")

        if user_selection == "1":
            name_letter=input("Please enter the first letter of your name.\n")
            rashi = zodiac_sign(name_letter)
            print(rashi)
            print('\n')

        elif user_selection =="2":
            #Read importance of zodiac sign
            file = open('importance.txt') 
            importances=file.read()
            file.close()
            print(importances)
            print('\n')
        elif user_selection == "3":
            # Exit
            print("I appreciate your utilization of this program!")
            break  
        else:
            # user selection is not valid
            print("The selection is invalid. Please select again.") 
            print('\n')

if __name__ == '__main__':
    welcome_mess()
    user_name()