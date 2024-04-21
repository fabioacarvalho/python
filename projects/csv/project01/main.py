import csv
import os

# Obtém o diretório do script Python
script_dir = os.path.dirname(__file__)
# Caminho completo para o arquivo "advertising.csv"
file_path = os.path.join(script_dir, "advertising.csv")


with open(file_path, "r") as file:
    infos = csv.reader(file, delimiter=",")
    for idx, item in enumerate(infos):
        print(f"{idx} - {item}")
