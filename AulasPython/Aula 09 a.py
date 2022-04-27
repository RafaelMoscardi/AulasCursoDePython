# FATIAMENTO
frase = 'Curso em Vídeo Python'
print(frase[3:11])

# FATIAMENTO
frase = 'Curso em Vídeo Python'
print(frase[:21])

# FATIAMENTO
frase = 'Curso em Vídeo Python'
print(frase[::2])


# ANALISE COM TRANSFORMAÇÃO 'COUNT' E 'UPPER'
frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))

# ANALISE JUNTO COM TRANSFORMAÇÃO 'LEN' E 'STRIP'
frase = '  Curso em Vídeo Python  '
print(len(frase.strip()))

# TRANSFORMAÇÃO 'REPLACE'
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))

# ANALISE 'IN'
frase = 'Curso em Vídeo Python'
print('Curso' in frase)

# ANALISE COM TRANSFORMAÇÃO 'FIND' E 'LOWER'
frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))

# DIVISÃO
frase = 'Curso em Vídeo Python'
print(frase.split())

# DIVISÃO
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido [2] [3])