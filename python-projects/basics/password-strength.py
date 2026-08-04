"""
password_strength.py

practicing for loops + string methods from module 3/4.
checks a password for length, uppercase, lowercase,
numbers, and special characters, then rates it.

now asks for a real password instead of just running
through a hardcoded list
"""

def check_password_strength(password):
    length_ok = len(password) >= 8
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    special_chars = "!@#$%^&*()_+-="

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True

    checks_passed = 0
    if length_ok:
        checks_passed = checks_passed + 1
    if has_upper:
        checks_passed = checks_passed + 1
    if has_lower:
        checks_passed = checks_passed + 1
    if has_number:
        checks_passed = checks_passed + 1
    if has_special:
        checks_passed = checks_passed + 1

    if checks_passed == 5:
        strength = "Strong"
    elif checks_passed >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print("Length 8+: " + str(length_ok))
    print("Has uppercase: " + str(has_upper))
    print("Has lowercase: " + str(has_lower))
    print("Has number: " + str(has_number))
    print("Has special char: " + str(has_special))
    print("Strength: " + strength)


# quick test with a few examples first
print("--- test examples ---")
test_passwords = ["password", "Password1", "P@ssw0rd123"]

for pw in test_passwords:
    print("\nPassword: " + pw)
    check_password_strength(pw)

# now let the user check their own
print("\n--- try your own ---")
user_password = input("Enter a password to check: ")
check_password_strength(user_password)
