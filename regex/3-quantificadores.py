import re

"""
 Meta caracteres: . ^ $ * ? { } [ ] \ | ( )
 | OU
 . Qualquer caractere (com exceção da quebra de linha)
 [] conjunto de caracteres
 ^ 
 $ 
 * 0 ou n
 ? 0 ou 1
 { } numero de vezes ex: {n} ou {5}
 { } numero de vezes ex: {min, max}
 \ 
 ( ) grupos

"""



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


print(re.findall(r'jo+ão+', texto, flags=re.I))

print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))

print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

texto2 = 'João ama ser amado'

print(re.findall(r'ama[do]*', texto2, flags=re.IGNORECASE))

