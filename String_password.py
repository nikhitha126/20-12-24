import string
password = input("Enter password: ")

def check_password(password):
    if len(password) <= 10 or len(password) >= 15:
        return "Enter minimum 10 characters"

    if not any(char.isupper() for char in password):
        return "Enter at least one uppercase character in password"
    if not any(char.islower() for char in password):
        return "Enter at least one lowercase character in password"
    if not any(char.isdigit() for char in password):
        return "Enter at least one digit in password"
    special_char = string.punctuation
    if not any(char in special_char for char in password):
        return "Password should contain at least one special character"
    if ' ' in password:
        return "Password should not contain white spaces"
    if password[-1] in ['.', '@']:
        return "Password should not end with '.' or '@'"
    return "Password is valid."

print(check_password(password))
