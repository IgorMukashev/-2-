number = int(input("Enter month number: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'январь',
                  2: 'февраль',
                  3: 'март',
                  4: 'апрель',
                  5: 'май',
                  6: 'июнь',
                  7: 'июль',
                  8: 'август',
                  9: 'сентябрь',
                  10: 'октябрь',
                  11: 'ноябрь',
                  12: 'December'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Month from list is {month_list[i]}")
            break
    print(f"Month from dict is {month_dict[number]}")
else:
    print("You made a mistake")