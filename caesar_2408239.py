#Nikisha Shrestha
#2408239

import os

from colorama import Fore, init

init(autoreset=True)

def red_input(prompt_text):
    """
    Takes user input with red color prompt.

    Args:
        prompt_text(str): The prompt message to display to the user.

    Returns:
        str: The user input.
    """
    while True:
        print(prompt_text, end='', flush=True)
        user_input = input(f'{Fore.RED}')
        print("\033[0m", end="", flush=True)
        return user_input
    
def welcome():
    """
    Displays the welcome message for the Caesar Cipher program.
    """
    print(f"Welcome to Caesar Cipher")
    print(f"This program encrypts and decrypts text using Caeser Cipher.")
    
def encrypt(message, shift):
    """
    Encrypts the given message using Caesar Cipher.

    Args:
        message(str): The message to encrypt.
        shift(int): The shift value for the Caesar Cipher.

    Returns:
        str: The encrypted message.
    """
    result = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            encrypted_char = chr((ord(char) - ord("A") 
                                  + shift) % 26 + ord("A"))
            result += encrypted_char
        else:
            result += char
    return result
    
def decrypt(message, shift):
    """
    Decrypts the given message using Caesar Cipher.

    Args:
        message(str): The message to decrypt.
        shift(int): The shift value for the Caesar Cipher.

    Returns:
        str: The decrypted message.
    """
    return encrypt(message, -shift)

def get_shift(mode, message):
    """
    Obtains the shift value from the user for encryption or decryption.

    Args:
        mode(str): The mode, either 'e' for encryption or 'd' for 
        decryption.
        message(str): The message for which the shift is obtained.

    Returns:
        int: The shift value.
    """
    while True:
        try:
            shift = int(red_input("What is the shift number: "))
            if 0 <= shift <= 25:
                if mode == "e":
                    print(encrypt(message, shift))
                    break
                elif mode == "d":
                    print(decrypt(message, shift))
                    break
                
                return shift
            
        except (ValueError, TypeError, NameError):
            print("Invalid Shift.")

def is_file(filename):
    """
    Checks if the given filename corresponds to an existing file.

    Args:
        filename(str): The name of the file to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(filename)

def write_message(messages):
    """
    Writes a list of messages to a file named "results.txt".

    Args:
        messages(list): A list of messages to be written to the file.
    """
    output_filename = "results.txt"

    with open(output_filename,"w") as file:
        for message in messages: 
            file.write(message + "\n")

def main():
    """
    Main function to execute the Caesar Cipher program.
    """
    welcome()
    enter_message()
    while True:
        another = red_input("Would you like to encrypt or decrypt another message(y/n)? ").lower()
        if another == "n":
            print("Thanks for using the program, goodbye!")
            break
                
        elif another == "y":
            enter_message()

        else:
            print("Invalid input.")   
        
def message_or_file():
    """
    Determines whether the user wants to encrypt/decrypt from a file 
    or console.

    Returns:
        tuple: A tuple containing mode('e' or 'd'), message, and filename
        (if applicable).
    """
    while True:
        mode = red_input("Would you like to encrypt (e) or decrypt (d)? ")
        if mode not in ["e", "d"]:
                print("Invalid Mode.")
                continue
            
        while True:
            input_source = red_input("Would you like to read from a file (f) or the console (c)? ").lower()
            if input_source == "f":
                while True:
                    filename = red_input("Enter a filename: ")
                    if is_file(filename):
                        process_file(filename, mode)
                        return mode, filename, None
                
                    else:
                        print("Invalid Filename.")
                
            elif input_source == "c":
                message = red_input(f"What message would you like to {mode}? ").upper()
                if mode == "e" or mode == "d":
                    shift = get_shift(mode, message)
                return mode, message, None
            else:
                print("Invalid input. Please enter (f) or (c).")
                              
def enter_message():
    """
    Calls the message_or_file function and returns the result.

    Returns:
        tuple: A tuple containing mode ('e' or 'd') and message.
    """
    while True:
        mode, message, filename = message_or_file()
        return mode, message
        
def process_file(filename, mode):
    """
    Processes a file for encryption or decryption.

    Args:
        filename(str): The name of the file to process.
        mode(str): The mode, either 'e' for encryption or 'd' for 
        decryption.
    """
    output_filename = "results.txt"
    while True:
        try:
            shift = int(red_input("What is the shift number: "))
            if 1<= shift <= 25:
                with open(filename, "r") as file:
                    messages = file.readlines()
                    result = []
            
                    for message in messages:
                        message = message.strip().upper()
                        if mode == "e":
                            result.append(encrypt(message, shift))
                            print(f"Output written to: {Fore.RED}{output_filename}\033[0m")
                        elif mode == "d":
                            result.append(decrypt(message, shift))
                            print(f"Output written to: {Fore.RED}{output_filename}\033[0m")
                write_message(result)
                break
                
        except (ValueError, TypeError, NameError, FileNotFoundError):
            print("Invalid Shift.")

# welcome()
# enter_message()
# result = encrypt("hello world", 4).upper()
# print(result)
# result = decrypt("lipps asvph", 4).upper()
# print(result)
# process_file('messages.txt','e')
# result = is_file('messages.txt')
# print(result)
# message_or_file()
main()



        
        
















        

        
            
        
        
                             
