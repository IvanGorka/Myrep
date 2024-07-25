import func
try:
    x = float(input("Введите первое число: "))
    oper = input("Введите оператор: ")
    y = float(input("Введите второе число: "))

    if oper == '+':
        func.add(x, y)
    elif oper == '*':
        func.mul(x, y)
    elif oper == '/':
        func.div(x, y)
    elif oper == '-':
        func.sub(x, y)
    else:
        print("Неправильный ввод оператора")
except ValueError:
    print("Неправильный ввод данных")
except ZeroDivisionError:
    print("На ноль делить нельзя")