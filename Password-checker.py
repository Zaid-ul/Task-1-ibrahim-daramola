password = input("Enter your password: ")

# Check password requirements
length = len(password)
has_uppercase = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

# Calculate security points
points = 0

if length >= 8:
    points += 1

if has_uppercase:
    points += 1

if has_number:
    points += 1

if has_symbol:
    points += 1

# Determine password strength
if points <= 1:
    strength = "WEAK"
elif points <= 3:
    strength = "MEDIUM"
else:
    strength = "STRONG"

# Display results
print("\n--- Password Security Report ---")
print("Length:", length)
print("Has uppercase:", has_uppercase)
print("Has number:", has_number)
print("Has symbol:", has_symbol)
print("Security points:", points)
print("Password strength:", strength)