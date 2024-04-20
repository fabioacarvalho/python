import re

texto = """
    <p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
"""
# Capturar o que possui dentro das tags:
# Aqui o comportamento vai ser capturar tudo que pode ser fechado ou (guloso): 
print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))

# Para evitar isso podemos usar o ? para ele se comportar de forma non greedy:
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))
