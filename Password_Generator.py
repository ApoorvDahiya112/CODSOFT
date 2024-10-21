import string
import random
import time

def generate_password(length):
    """
    Generate a password of specified length ensuring at least one character
    from each category (lowercase, uppercase, digit, symbol)
    """
    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Start with one character from each pool
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random characters
    all_characters = lowercase + uppercase + digits + symbols
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
    
    # Shuffle the password characters
    random.shuffle(password)
    
    # Join and return the password
    return ''.join(password)

if __name__ == "__main__":
    while True:
        try:
            pwd_len = int(input("Enter length of the password (minimum 4): "))
            if pwd_len < 4:
                print("Password length must be at least 4 characters. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    time.sleep(1)
    password = generate_password(pwd_len)
    print(f"\nYour password is: {password}")
    
    
    # Display password strength indicators
    time.sleep(1)
    print("\nPassword strength:")
    time.sleep(1)
    print(f"Length: {len(password)} characters")
    time.sleep(1)
    print(f"Contains lowercase: {any(c.islower() for c in password)}")
    time.sleep(1)
    print(f"Contains uppercase: {any(c.isupper() for c in password)}")
    time.sleep(1)
    print(f"Contains digits: {any(c.isdigit() for c in password)}")
    time.sleep(1)
    print(f"Contains symbols: {any(c in string.punctuation for c in password)}")