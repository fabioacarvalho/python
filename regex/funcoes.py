# Here we'll learn about regex functions

import re

# findall search sub compile

string = 'Este e um teste de busca de string teste'


restring = re.search(r'teste', string)

# aqui vai retonar uma lista com os valores encontrados
restring2 = re.findall(r'teste', string)

print(restring)
print(restring2)

# aqui vai substituir um valor
substituir = re.sub(r'teste', 'ABC', string)
print(substituir)

# Aqui vc defini qtd de substituicao ou seja, mude apenas primeira count=1
substituir2 = re.sub(r'teste', 'ABC', string, count=1)
print(substituir2)

# compile e uma forma interessante de reutilizar a regex
regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))


