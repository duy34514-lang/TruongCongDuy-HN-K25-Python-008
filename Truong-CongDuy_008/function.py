def check_string(text):
    while True:
        value = input(f"{text}: ").strip()

        if value == "":
            print("Không được để trống")
            continue

        return value


def check_int(text, left=None, right=None):
    while True:
        try:
            value = int(input(f"{text}: "))

            if left is not None and value < left:
                print("Giá trị không hợp lệ")
                continue

            if right is not None and value > right:
                print("Giá trị không hợp lệ")
                continue

            return value

        except ValueError:
            print("Vui lòng nhập số")


def check_float(text, left=None, right=None):
    while True:
        try:
            value = float(input(f"{text}: "))

            if left is not None and value < left:
                print("Giá trị không hợp lệ")
                continue

            if right is not None and value > right:
                print("Giá trị không hợp lệ")
                continue

            return value

        except ValueError:
            print("Vui lòng nhập số")
