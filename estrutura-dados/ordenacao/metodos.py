lista = [1,2,5,6,3,9,8,7,10,55,3,]

def bubble(lista):
    n = len(lista)

    for x in range(n):
        for y in range(n-x-1):
            if lista[y+1] > lista[y]:
                lista[y], lista[y+1] = lista[y+1], lista[y]
    return lista



def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # Lista vazia ou com apenas um elemento já está ordenada
    
    # Escolhe um elemento pivô (geralmente o último elemento)
    pivô = lista[len(lista) - 1]
    
    # Inicializa listas para os elementos menores, iguais e maiores que o pivô
    menores, iguais, maiores = [], [], []
    
    # Divide a lista em três partes com base no pivô
    for elemento in lista:
        if elemento < pivô:
            menores.append(elemento)
        elif elemento == pivô:
            iguais.append(elemento)
        else:
            maiores.append(elemento)
    
    # Recursivamente ordena as partes menores e maiores 
    # Para inverter a ordem basta inverter menores e maiores no return
    return quick_sort(menores) + iguais + quick_sort(maiores)


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        # Move os elementos da lista[0..i-1] que são maiores que a chave
        # para uma posição à frente de sua posição atual
        while j >= 0 and chave > lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave


val = [
    {'nome': 'Fabio', 'sobrenome': 'Souza'},
    {'nome': 'Pedro', 'sobrenome': 'Simao'},
    {'nome': 'Antonio', 'sobrenome': 'jao'},
    {'nome': 'Maria', 'sobrenome': 'silva'},
]

val.sort(key=lambda item: item['nome'])
print(val)
