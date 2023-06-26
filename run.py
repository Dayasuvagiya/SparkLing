import time
import colorama
from colorama import Fore, Back, Style
colorama.init()


def welcome_mess():
    # Creates a welcome message
    print(Fore.CYAN + "######################################")
    print("#                                    #")
    print("#     Let's begin ZodiacJourney      #")
    print("#    ---------------------------     #")
    print("#                                    #")
    print("######################################" + Style.RESET_ALL)
    time.sleep(1)
    print(" ")

    time.sleep(1)
    print("Welcome to mesmerizing realm of astrology.")
    time.sleep(1)
    print("Discover the Zodiac sign & numerology value of your name.")
    time.sleep(1)
    print("Let's start...")
    time.sleep(1)
    print(Fore.CYAN + "^_^" + Style.RESET_ALL + "\n")
    time.sleep(1)


def zodiac_sign(letter):
    """Define dictionary to show zodiac sign,
    Convert user input in lowercase,
    loop and if statement shows output"""

    zodiac_alphabets = {
        'bh': 'Sagittarius', 'f': 'Sagittarius', 'dh': 'Sagittarius',
        'p': 'Virgo', 'tha': 'Virgo',
        'dd': 'Cancer', 'h': 'Cancer',
        'g': 'Aquarius', 's': 'Aquarius', 'sh': 'Aquarius',
        'kh': 'Capricorn', 'j': 'Capricorn',
        'd': 'Pisces', 'ch': 'Pisces', 'z': 'Pisces', 'th': 'Pisces',
        'a': 'Aries', 'l': 'Aries', 'e': 'Aries', 'i': 'Aries', 'o': 'Aries',
        'k': 'Gemini', 'chh': 'Gemini', 'gh': 'Gemini',
        'q': 'Gemini', 'c': 'Gemini',
        'm': 'Leo', 'tt': 'Leo',
        'r': 'Libra', 't': 'Libra',
        'b': 'Taurus', 'v': 'Taurus', 'u': 'Taurus', 'w': 'Taurus',
        'n': 'Scorpio', 'y': 'Scorpio', 'x': 'No Zodiac sign for this letter'
    }
    # User input convert to lowercase
    lower_case = letter.lower()
    # Look up zodiac sign of each letter
    for key, value in zodiac_alphabets.items():
        if key == lower_case:
            time.sleep(1)
            return Fore.GREEN + f"Your Zodiac sign is '{value}'" + Style.RESET_ALL

    return Fore.RED + """No data found please enter the correct character,
    For Instance:
    Your name is 'John', enter 'j' or 'J'""" + Style.RESET_ALL


def numerology(nume_letter):
    """Define dictionary to calculate numerology value,
    check the value for a name given by the user,
    User input convert to lowercase"""
    numerology_alphabets = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
        'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5,
        'o': 6, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2, 'u': 3,
        'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    }
    nume_letter = nume_letter.lower()
    if nume_letter in numerology_alphabets:
        return numerology_alphabets[nume_letter]
    else:
        return 0


def addition_nume(user_name):
    """ Addition of name numerology value"""
    numerology_value = 0
    for each_letter in user_name:
        alpha_value = numerology(each_letter)
        if alpha_value == 0:
            return Fore.RED + "Please enter only alphabets" + Style.RESET_ALL
        numerology_value += alpha_value

    # Addition of number based on the letter
    while numerology_value > 9:
        letter_value = 0
        numerology_string = str(numerology_value)
        for number in numerology_string:
            letter_value += int(number)
            numerology_value = letter_value
    time.sleep(1)
    return Fore.GREEN + f"The numerology value of your name is'{numerology_value}'" + Style.RESET_ALL


def user_name():
    """Display main menu for user to select one option,
    According to user choice give the relevant response"""

    while True:
        # Error handle
        try:
            # The main menu, gives user options to select.
            print("MENU:")
            print("1. Discover your Zodiac identity through your name.")
            print("2. Discover numerology value of your name.")
            print("3. Read personality traits based on your Zodiac sign.")
            print("4. Exit program.")
            user_selection = input("Enter your choice (1, 2, 3 or 4)\n")

            if user_selection == "1":
                # Know the Zodiac sign
                name_letter = input("Please enter the first letter of name:\n")
                rashi = zodiac_sign(name_letter)
                print(rashi)
                print('\n')

            elif user_selection == "2":
                # Know numerology value of name
                user_name = input("Enter your full name:")
                if not user_name.isalpha():
                    print("Please input letterts only")
                else:
                    nume_value = addition_nume(user_name)
                    print(nume_value)
                    print('\n')

            elif user_selection == "3":
                # Read personality base on zodiac sign
                file = open('importance.txt')
                importances = file.read()
                file.close()
                print(importances)
                print('\n')

            elif user_selection == "4":
                # Exit
                print(Fore.CYAN + "I appreciate your utilization of this program!" + Style.RESET_ALL)
                break

            else:
                # user selection is not valid
                print(Fore.RED + "invalid choice. Please select again." + Style.RESET_ALL)
                print('\n')

        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)


if __name__ == '__main__':
    welcome_mess()
    user_name()
