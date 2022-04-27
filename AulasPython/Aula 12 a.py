# ESTRUTURA CONDICIONAL ANINHADA.
nome = str(input('Qual é seu nome? ')).strip().upper()
if nome == 'RAFAEL':
    print('Que nome bonito! ')
elif nome == 'JOAO' or nome == 'JORGE' or nome == 'MURILO' or nome == 'VINICIUS':
    print('Seu nome é bem popular no Brasil')
elif nome in 'LISA NATHALIA SUZANY JULIANA':
    print('Belo nome feminino! ')
else:
    print('Seu nome é bem normal. ')
print('Tenha um bom dia, {}!'.format(nome.title()))