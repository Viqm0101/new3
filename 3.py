pol = int(input('введите месяц '))
lv = ['зима', 'весна', 'лето', 'осень']
sv = {1:'зима', 2:'весна', 3:'лето', 4:'осень'}

if pol == 12 or pol == 1 or pol == 2:
    print(lv[0])
    print(sv[1])
elif pol == 3 or pol == 4 or pol == 5:
    print(lv[1])
    print(sv[2])
elif pol == 6 or pol == 7 or pol == 8:
    print(lv[2])
    print(sv[3])
elif pol == 9 or pol == 10 or pol == 11:
    print(lv[3])
    print(sv[4])
else:
    print('Вы набрали неправильное число месяца')