duplicados = [1,2,3,4,5,6,7,8,9,4,3,10,11,5,5,5,3,2,1,9,5,7,6,2,33]


def remove_duplicate(lista):
    numeros = set()
    for i in range(len(duplicados)):
        for item in lista:
            if lista[i] == item:
                numeros.add(item)
    
    return numeros


