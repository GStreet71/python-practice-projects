import string
import secrets

def generate_password(length):
    # Include specified special characters
    special_characters = "!@#$%&*"
    
    # Create a pool of characters including uppercase, lowercase, digits, and special characters
    all_characters = string.ascii_letters + string.digits + special_characters

    # Input validation for password length
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Determine the number of sections based on the requested length
    if length == 8:
        # If the length is exactly 8, generate a single password without sections
        return ''.join(secrets.choice(all_characters) for _ in range(length))
    
    elif length <= 15:
        num_sections = 3
    elif length <= 19:
        num_sections = 4
    else:
        num_sections = 5

    # Calculate the length of the actual password characters (subtract dashes)
    password_length = length - (num_sections - 1)

    # Ensure that each section is at least 3 characters long
    while (password_length // num_sections) < 3 and num_sections > 1:
        num_sections -= 1
        password_length = length - (num_sections - 1)
    
    # Generate the password with the calculated length
    password = ''.join(secrets.choice(all_characters) for _ in range(password_length))

    # Calculate how to split the generated password into sections
    section_length = password_length // num_sections
    sections = []
    start_index = 0
    
    # Create each section
    for i in range(num_sections):
        if i < num_sections - 1:
            sections.append(password[start_index:start_index + section_length])
            start_index += section_length
        else:
            sections.append(password[start_index:])

    # Join the sections with dashes if applicable
    formatted_password = '-'.join(sections)
    return formatted_password

# User input for password length
length = int(input("Enter the total length of the password: "))
print("Generated Password: ", generate_password(length))
