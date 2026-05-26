import argparse
from generator import generate_password
from utils import print_message

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор паролей")
    parser.add_argument("-l", "--length", type=int, default=12,
                        help="Длина пароля (мин. 4)")
    parser.add_argument("-s", "--special", action="store_true",
                        help="Использовать спецсимволы")
    args = parser.parse_args()

    try:
        pwd = generate_password(length=args.length, use_special=args.special)
        print_message(f"Сгенерирован пароль длиной {len(pwd)}", "success")
        print(f"Пароль: {pwd}")
    except ValueError as e:
        print_message(str(e), "error")
