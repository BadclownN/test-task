def main(input_str):
    input_str = input_str.strip()

    if '+' in input_str:
        operator = '+'
    elif '-' in input_str:
        operator = '-'
    elif '*' in input_str:
        operator = '*'
    elif '/' in input_str:
        operator = '/'
    else:
        raise Exception("Ошибка. Используйте только +, -, *, /.")

    parts = input_str.split(operator)

    if len(parts) != 2:
        raise Exception("Ошибка. Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")

    a_str = parts[0].strip()
    b_str = parts[1].strip()

    if not a_str.isdigit() or not b_str.isdigit():
        raise Exception("Калькулятор работает только с целыми числами.")

    a = int(a_str)
    b = int(b_str)

    if a < 1 or a > 10 or b < 1 or b > 10:
        raise Exception("Числа должны быть от 1 до 10 включительно.")

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a // b  # Целочисленное деление

    return str(result)


if __name__ == "__main__":
    print("Введите выражение.")
    while True:
        user_input = input("Введите выражение: ").strip().lower()
        if user_input == "выход" or user_input == "exit":
            print("Выход из калькулятора.")
            break
        try:
            result = main(user_input)
            print("Результат:", result)
        except Exception as error:
            print("Ошибка:", error)