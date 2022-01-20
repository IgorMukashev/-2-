try:
    number_of_month = int(input("Введите номер месяца числом от 1 до 12: "))
except ValueError:
    print("Неверно введен месяц")
else:
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if number_of_month in winter:
        print('Зима холодно')
    elif number_of_month in spring:
        print( 'Весна все расцветает' )
    elif number_of_month in summer:
            print( 'Лето, солнце, класс' )
    elif number_of_month in autumn:
        print( 'Осень дожди слякоть' )
    else:
        print( 'Время года не определено' )