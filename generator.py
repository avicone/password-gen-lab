import secrets
import string

def generate_password(length=12, use_special=False, lowercase_only=False):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{}<>~"
    if lowercase_only:
        chars = chars.lower()

    return ''.join(secrets.choice(chars) for _ in range(length))