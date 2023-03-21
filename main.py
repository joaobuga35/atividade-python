"""
1- Crie uma lista lista_1 dos inteiros de 6 a 20 (ambos inclusos) utilizando range;
2- Imprima o último elemento da lista_1;
3- Altere o segundo elemento de lista_1 para 'Kenzie'. Imprima lista_1;
4- Utilize do fatiamento para imprimir somente os elementos de índice 2, 3 e 4 de lista_1;
5- Adicione o seguinte valor ao final de lista_1: 'Academy'. Imprima lista_1;
6- Remova os items referentes aos valores 'Kenzie' e 'Academy' de lista_1;
7- Crie e imprima uma nova lista ordenada inversamente (lista_2) com base em lista_1, sem ordenar de fato a lista_1. Imprima lista_1 e lista_2;
8- Imprima o tamanho de lista_1 e lista_2;
9- Retire o último item de lista_1 e lista_2. Imprima lista_1 e lista_2;
10- Retire todos os elementos tanto de lista_1 quanto de lista_2, imprima-as;
"""
list_1 = list(range(6, 21))

last_number = list_1[-1]

list_1[1] = 'Kenzie'

fatiamento = list_1[1:4]

list_1.extend(['Academy'])

list_1.remove('Kenzie')

list_1.pop()

list_2 = list_1.copy()
list_2.reverse()

list_1.pop()
list_2.pop()

list_1.clear()
list_2.clear()

print(len(list_1), len(list_2))
