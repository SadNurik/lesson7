functions = ['all','any','abs','min','eval','reversed',
            'max','slice','round',]
func = input("Введите функцию : ")
if func in functions:
    print('Такая функция есть')
else:
    print('Такой функции нету')