import re

# Meta caracteres: . ^ $ * ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres


texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
joao.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'Jo.o|Maria', texto))
print(re.findall(r'[Jj]o.o|[Mm]aria|caf.', texto))
print(re.findall(r'[a-z]o.o|[a-z]aria|caf.', texto))

# just case sensitive
print(re.findall(r'[a-zA-Z]o.o|[a-zA-Z]aria|caf.', texto))

# Case sensitive and numbers
print(re.findall(r'[a-zA-Z0-9]o.o|[a-zA-Z0-9]aria|caf.', texto))

# Utilizando a flags:
print(re.findall(r'joao|maria', texto, flags=re.IGNORECASE)) # or flags=re.I


