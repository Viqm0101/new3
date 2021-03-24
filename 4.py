pol = input('введите слова ')
st = []
i = 1

for lis in range(pol.count(' ') +1):
    st = pol.split()
    if len(str(st)) <= 10:
        print(f" {i} {st[lis]}")
        i += 1
    else:
        print(f"{i} {st[lis] [0:10]}")
        i += 1
