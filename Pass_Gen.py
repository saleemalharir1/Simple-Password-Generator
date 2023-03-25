# # Ask user for password length and character types
# password_length = input("Enter desired password length: ")
# use_lowercase = input("Use lowercase letters? (y/n): ")
# use_uppercase = input("Use uppercase letters? (y/n): ")
# use_numbers = input("Use numbers? (y/n): ")
# use_symbols = input("Use symbols? (y/n): ")

password_length = int(input("Enter Desired Password Length: "))
use_lowercase = input("Use lowercase letters? (y/n): ")
use_uppercase = input("Use uppercase letters? (y/n): ")
use_numbers = input("Use numbers? (y/n): ")
use_symbols = input("Use Sybmols? (y/n): ")
# Define character sets based on user input

import string

lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
number_chars = string.digits
symbol_chars = string.punctuation
# Loop through desired password length and randomly choose characters from selected character sets
import random

password = ""

while True:
    if use_lowercase == "y" and len(password) < password_length:
        password += random.choice(lowercase_chars)
    if use_uppercase == "y" and len(password) < password_length:
        password += random.choice(uppercase_chars)
    if use_numbers == "y" and len(password) < password_length:
        password += random.choice(number_chars)
    if use_symbols == "y" and len(password) < password_length:
        password += random.choice(symbol_chars)
    if len(password) == password_length:
        break

print("Your password is:", password)