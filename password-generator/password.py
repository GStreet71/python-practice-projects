import string
import secrets

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(secrets.choice(all_characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
print("Generated Password : ", generate_password(length))
