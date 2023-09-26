import os
import time
from colorama import init, Fore, Style
import sys

# Initialize Colorama for cross-platform terminal color support
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_typewriter(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def animate_loading():
    for _ in range(3):
        for _ in range(4):
            print(".", end='', flush=True)
            time.sleep(0.5)
        print("\b\b\b   \b\b\b", end='', flush=True)
        time.sleep(0.5)

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    try:
        while True:
            clear_screen()
            # Print the styled text using colorama
            print(Fore.MAGENTA + r'''        
 ______  __  ______ __  __  ______  ______ __  __    
/\  ___\/\ \/\  == /\ \_\ \/\  ___\/\  == /\_\_\_\   
\ \ \___\ \ \ \  _-\ \  __ \ \  __\\ \  __\/_/\_\/_  
 \ \_____\ \_\ \_\  \ \_\ \_\ \_____\ \_\ \_/\_\/\_\ 
  \/_____/\/_/\/_/   \/_/\/_/\/_____/\/_/ /_\/_/\/_/                                                                                                                                                                
            ''' + Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT + "CipherX - Advanced Caesar Cipher Encryption and Decryption")
            print(Fore.MAGENTA + Style.RESET_ALL)
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Encrypt a file")
            print("4. Decrypt a file")
            print("5. Exit")
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '1':
                message = input("Enter the message to encrypt: ")
                shift = int(input("Enter the shift value: "))
                print(Fore.YELLOW + "Encrypting..." + Fore.RESET, end=' ')
                animate_loading()
                encrypted_message = encrypt(message, shift)
                print(Fore.GREEN + "Encryption complete:" + Fore.RESET, end=' ')
                animate_typewriter(encrypted_message)
            elif choice == '2':
                encrypted_message = input("Enter the message to decrypt: ")
                shift = int(input("Enter the shift value: "))
                print(Fore.YELLOW + "Decrypting..." + Fore.RESET, end=' ')
                animate_loading()
                decrypted_message = decrypt(encrypted_message, shift)
                print(Fore.GREEN + "Decryption complete:" + Fore.RESET, end=' ')
                animate_typewriter(decrypted_message)
            elif choice == '3':
                file_to_encrypt = input("Enter the name of the file to encrypt: ")
                shift = int(input("Enter the shift value: "))
                try:
                    text_to_encrypt = read_from_file(file_to_encrypt)
                    print(Fore.YELLOW + "Encrypting..." + Fore.RESET, end=' ')
                    animate_loading()
                    encrypted_text = encrypt(text_to_encrypt, shift)
                    output_file = input("Enter the name of the output file: ")
                    save_to_file(output_file, encrypted_text)
                    print(Fore.GREEN + f"File '{file_to_encrypt}' encrypted and saved as '{output_file}'." + Fore.RESET)
                except FileNotFoundError:
                    print(Fore.RED + "File not found." + Fore.RESET)
            elif choice == '4':
                file_to_decrypt = input("Enter the name of the file to decrypt: ")
                shift = int(input("Enter the shift value: "))
                try:
                    text_to_decrypt = read_from_file(file_to_decrypt)
                    print(Fore.YELLOW + "Decrypting..." + Fore.RESET, end=' ')
                    animate_loading()
                    decrypted_text = decrypt(text_to_decrypt, shift)
                    output_file = input("Enter the name of the output file: ")
                    save_to_file(output_file, decrypted_text)
                    print(Fore.GREEN + f"File '{file_to_decrypt}' decrypted and saved as '{output_file}'." + Fore.RESET)
                except FileNotFoundError:
                    print(Fore.RED + "File not found." + Fore.RESET)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print(Fore.RED + "Invalid choice. Please enter 1, 2, 3, 4, or 5." + Fore.RESET)
            input("\nPress Enter to continue...")
    except KeyboardInterrupt:
        print("\nThank you for using CipherX!")

if __name__ == "__main__":
    main()
