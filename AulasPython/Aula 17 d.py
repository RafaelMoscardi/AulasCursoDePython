lista = []
for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))
for c, v in enumerate(lista):
    print(f'O maior número digitado é: {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor número digitado é: {min(lista)} na posição {lista.index(min(lista))}')