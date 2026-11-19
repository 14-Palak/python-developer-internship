
import string
import secrets

print("====================================")
print("       PASSWORD GENERATOR")
print("====================================")

# Character groups
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

all_characters = uppercase + lowercase + numbers + symbols

while True:
    try:
        length = int(input("\nEnter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        count = int(input("How many passwords do you want? "))

        if count <= 0:
            print("Enter a number greater than zero.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

print("\n========== GENERATED PASSWORDS ==========")

for i in range(count):

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    # Fill remaining positions
    for j in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle characters
    secrets.SystemRandom().shuffle(password)

    final_password = "".join(password)

    print(f"Password {i + 1}: {final_password}")

print("\nThank you for using Password Generator!")
