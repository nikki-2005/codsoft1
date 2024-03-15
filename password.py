import random
import string

def generate_password(length):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt user for desired password length
    length = int(input("Enter the desired length of the password: "))
    
    # Generate and display password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
