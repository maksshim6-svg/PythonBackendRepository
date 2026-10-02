import math


def print_menu():
  print("\n=== Продвинутый калькулятор ===")
  print("Доступные операции:")
  print("1. Сложение (+)")
  print("2. Вычитание (-)")
  print("3. Умножение (*)")
  print("4. Деление (/)")
  print("5. Возведение в степень (**)")
  print("6. Квадратный корень (sqrt)")
  print("7. Синус (sin)")
  print("8. Косинус (cos)")
  print("9. Тангенс (tan)")
  print("0. Выход")


def get_number(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Ошибка: введите корректное число!")


def calculator():
  while True:
    print_menu()
    choice = input("\nВыберите номер операции (0-9): ").strip()

    if choice == "0":
      print("Работа калькулятора завершена. До свидания!")
      break

    if choice in ["1", "2", "3", "4", "5"]:
      num1 = get_number("Введите первое число: ")
      num2 = get_number("Введите второе число: ")

      if choice == "1":
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
      elif choice == "2":
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
      elif choice == "3":
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")
      elif choice == "4":
        if num2 == 0:
          print("Ошибка: деление на ноль невозможно!")
        else:
          result = num1 / num2
          print(f"Результат: {num1} / {num2} = {result}")
      elif choice == "5":
        result = num1**num2
        print(f"Результат: {num1} ** {num2} = {result}")

    elif choice in ["6", "7", "8", "9"]:
      num = get_number("Введите число: ")

      if choice == "6":
        if num < 0:
          print("Ошибка: нельзя извлечь корень из отрицательного числа!")
        else:
          result = math.sqrt(num)
          print(f"Результат: sqrt({num}) = {result}")
      elif choice == "7":
        # Перевод градусов в радианы для удобства
        rad = math.radians(num)
        result = math.sin(rad)
        print(f"Результат: sin({num}°) = {result}")
      elif choice == "8":
        rad = math.radians(num)
        result = math.cos(rad)
        print(f"Результат: cos({num}°) = {result}")
      elif choice == "9":
        rad = math.radians(num)
        result = math.tan(rad)
        print(f"Результат: tan({num}°) = {result}")

    else:
      print("Ошибка: выбран несуществующий пункт меню. Попробуйте снова.")


if __name__ == "__main__":
  calculator()
