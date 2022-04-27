num = [2, 5, 9, 1]
num[2] = 3
num.sort()
print(num)
n = int(input('Que número deseja adicionar na lista? '))
num.append(n)
num.pop(2)
del num[1]
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5.')
print(f'Essa lista tem {len(num)} elementos.')
print(num)