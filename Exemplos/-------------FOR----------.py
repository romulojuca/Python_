#PARA cada VALOR em VALORES:
valores = [0, 9, 4]
for valor in valores:
    print(f'{valor}...')

#PARA cada POSICAO, INDICE em VALORES
for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao} encontrei o valor {valor}')
print('Cheguei ao final da lista')

numeros = list()
for cont in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))
print(numeros)

a = [2, 3, 4, 7]
b = a[:]#CRIA uma COPIA da lista a na variavel b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
