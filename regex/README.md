# Regex Python

## Metadados

Existem alguns tipos de metadados e abaixo estão alguns e seus significados:

- () grupo ou retrovisores:

```
```

- {} 

```
```

- [] conjunto:

```
```

- *

```
```

- ?

```
```

- ^

```
```

- @


```
```

- | OU:


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


## Funções

_Abaixo estão algumas funções para utilizar e uma breve descrição_