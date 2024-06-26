import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters)for i in range(length))
    return password

def main():
    print("Welcome to Password Generator App!")
    length = int(input("Enter the desired length of the password (at least 20 characters) "))
    password = generate_password(length)
    if password:
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()
