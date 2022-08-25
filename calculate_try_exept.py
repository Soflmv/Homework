print("Привет user, это простой калькулятор =)  \n"
      "Выбери действие которое нужно выполнить: \n"
              "Сложение : +\n"
              "Вычитание: -\n"
              "Умножение: *\n"
              "Деление: /\n"
              "Выйти: q\n"
      )


def addition():
    x = float(input("x = "))
    y = float(input("y = "))
    print('%.2f + %.2f = %.2f' % (x, y, x + y))


def subtraction():
    x = float(input("x = "))
    y = float(input("y = "))
    print('%.2f - %.2f = %.2f' % (x, y, x - y))


def multiplication():
    x = float(input("x = "))
    y = float(input("y = "))
    print('%.2f * %.2f = %.2f' % (x, y, x * y))


def division():
    x = float(input("x = "))
    y = float(input("y = "))
    print('%.2f / %.2f = %.2f' % (x, y, x / y))


while True:
    try:
        input_user = input("Введи действие: ")
        if input_user == "q":
            print("Ты вышел из программы!")
            break
        elif input_user == "+":
            addition()
        elif input_user == "-":
            subtraction()
        elif input_user == "*":
            multiplication()
        elif input_user == "/":
            division()
        else:
            print("Хочешь выполнить еще какое либо действие?\n"
                  "Если нет, 'q' выход из программы!")
    except ZeroDivisionError:
        print("Деление на ноль!!!")
    except ValueError:
        print("Нужно вводить только цифры!")
