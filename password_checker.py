password = input("Enter your password: ")

score = 0
feedback = []

# Check length
if len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters.")

# Check uppercase letters
if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add uppercase letters.")

# Check lowercase letters
if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Add lowercase letters.")

# Check numbers
if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add numbers.")

# Check special characters
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

if any(char in special_characters for char in password):
    score += 1
else:
    feedback.append("Add special characters.")

# Display result
if score <= 2:
    print("\nPassword Strength: Weak ❌")
elif score <= 4:
    print("\nPassword Strength: Moderate ⚠️")
else:
    print("\nPassword Strength: Strong ✅")

# Display feedback
if feedback:
    print("\nFeedback:")
    for item in feedback:
        print("-", item)
else:
    print("\nExcellent! Your password meets all security requirements.")