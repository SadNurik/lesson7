num = set()

for i in range(5):
    try:
        num1 = int(input("Введите число: "))
        num.add(num1)
        if num1 == 0:
            print("Введите натуральное число")
        if num1 < 0:
            print("Число выше 0")
    except ValueError:
        print("Введите число")

print("Самое маленькое число: ", min(num))