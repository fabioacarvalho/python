# Regex Python
_(Em produção)_

Caso queria saber mais você pode acessar essa documentção __[REGEX PYTHON HOWTO](https://docs.python.org/pt-br/2.7/howto/regex.html#:~:text=Este%20documento%20%C3%A9%20um%20tutorial%20introdut%C3%B3rio%20sobre%20express%C3%B5es,que%20a%20se%C3%A7%C3%A3o%20correspondente%20%C3%A0%20documenta%C3%A7%C3%A3o%20do%20m%C3%B3dulo.)__.

## Metadados

Existem alguns tipos de metadados e abaixo estão alguns e seus significados:

- __[] conjunto:__<br>
Este representa um conjunto de caracteres.


```
import re

texto2 = 'João ama ser amado'

print(re.findall(r'ama[do]*', texto2, flags=re.IGNORECASE))
```

- __() grupo ou retrovisores:__<br>

```
```

> __Para acessar os grupos será da segunite forma:__ <br> - _1 grupo (): \1_ <br> - _2 grupo () (): \1 \2_ <br> - _3 grupo () () (): \1 \2 \3_ <br> - _3 grupo (()) (): \1 \2 \3_ 

<br>


- __{} numero de repetições ou entre x e y:__<br>

Por exemplo o número de um __CPF__ é representado por 11 digitos sendo ele separado por . e - para os últimos 2 digitos.<br>

Exemplo 1:

```
CPF = '147.852.001-55'
print(re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', CPF))
```

<br>

Exemplo 2:<br>

```
import re

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

print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

```

<br>

- __*__<br>

```
```

<br>

- __?__<br>

```
```
<br>


- __^__<br>

```
```

<br>


- __@__<br>


```
```

<br>


- __| OU:__<br>


```
import re

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

print(re.findall(r'jo{1,}ão{1,} | maria', texto, flags=re.I))

```

<br>


## Funções

_Abaixo estão algumas funções para utilizar e uma breve descrição_