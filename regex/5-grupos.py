import re
from pprint import pprint as p
"""
 Meta caracteres: ^ $
 [] conjunto de caracteres
 ( ) grupos
"""

# Para acessar os grupos será da segunite forma:
# 1 grupo (): \1
# 2 grupo () (): \1 \2
# 3 grupo () () (): \1 \2 \3
# 3 grupo (()) (): \1 \2 \3

# Obs.: Isso também é conhecido como retrovisores

texto = """
    <p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
"""

print(re.findall(r'<([dpiv]{1,3})>.*?<\/\1>', texto))
# return: ['p', 'p', 'p', 'div']

tags = re.findall(r'(<([dpiv]{1,3})>.*?<\/\2>)', texto)
p(tags)
# return: [('<p>Frase 1</p>', 'p'), ('<p>Frase 2</p>', 'p'), ('<p>Frase 3</p>', 'p'), ('<div>Frase 4</div>', 'div')]

tags2 = re.findall(r'(<([dpiv]{1,3})>(.*?)<\/\2>)', texto)

for tag in tags2:
    um, dois, tres = tag
    print(um)
    print(dois)
    print(tres)

