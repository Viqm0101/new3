
pol = int(input('введите число'))
ls = [5, 4, 3, 3, 1]

while pol != 0:
    for el in range(len(ls)):
        if ls[el] == pol:
            ls.insert(el + 1, pol)
            break
        elif ls[0] < pol:
            ls.insert(0, pol)
        elif ls[-1] > pol:
            ls.append(pol)
        elif ls[el] > pol and ls[el + 1] < pol:
            ls.insert(el + 1, pol)
    print(f'Список - {ls}')
    pol = int(input('ведите новое число'))