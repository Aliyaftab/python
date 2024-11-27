import string
import random

# Characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("@&$#!")

def generate_random_passwords():
    # Get user's nickname
    nickname = input("Enter your nickname: ")

    # Length of password from the user
    length = int(input("Enter password length: "))
    # Number of characters types
    #alphabets_count = int(input("Enter alphabets count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_characters_count = int(input("Enter special characters count in password: "))

    # Counting nickname letters towards the password length
    length -= len(nickname)

    # Total count of characters
    characters_count =   digits_count + special_characters_count

    # Check if the total character count is greater than the password length
    if characters_count > length:
        print("Characters total count is greater than the password length")
    else:
        # Initializing the password
        password = []

        # Picking random alphabets
      #  for _ in range(alphabets_count):
        #    password.append(random.choice(alphabets))

        # Picking random digits
        for _ in range(digits_count):
            password.append(random.choice(digits))

        # Picking random special characters
        for _ in range(special_characters_count):
            password.append(random.choice(special_characters))

        # If the total characters count is less than the password length
        # add random characters to make it equal to the length
        #if characters_count < length:
         #   random.shuffle(characters)
           # for _ in range(length - characters_count):
             #   password.append(random.choice(characters))

        # Shuffling the resultant password
        random.shuffle(password)

        # Combining nickname and password and converting the list to string
        final_password = nickname + "".join(password)

        # Printing the final password
        print("Your password:", final_password)

# Invoking the function
generate_random_passwords()
