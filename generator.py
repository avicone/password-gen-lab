import secrets
import string

def generate_password(length=12, use_special=False, uppercase_only=False):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{}<>~"
    if uppercase_only:
        chars = chars.upper()

    return ''.join(secrets.choice(chars) for _ in range(length))
