'''
Version: 1.0
Made by: Matheus
Date: 06/03/2023

It's a simple program that generates a random password for the user. 

'''

from getpass import getuser
import secrets
import string

# This function returns a password with a given lenght of characters, optional special characters. 
def generatePassword(char, specialChars=False):
    
    alphabet = string.ascii_letters + string.digits

    if specialChars:
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for i in range(char))

    return password

# This function gets a generic user input and returns the input value as a string.
def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print('Invalid input. Please try again.')

def main():
    name = getuser().capitalize()
    print(f'Welcome to Password Generator, {name}!')

    length = int(get_user_input('How many characters: '))
    include_special_chars = get_user_input('Do you want to use Special Characters? (y/n) ').lower() == 'y'

    password = generatePassword(length, include_special_chars)

    print(f'Your new password is: {password}')

if __name__ == '__main__':
    main()