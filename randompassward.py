import random
import string

def generate_password(length):
    
    letters = string.ascii_letters      
    digits = string.digits             
    symbols = string.punctuation        

    all_characters = letters + digits + symbols

    
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password



print("=== Random Password Generator ===")
length = int(input("Enter password length: "))

new_password = generate_password(length)
print("Your generated password is:", new_password)