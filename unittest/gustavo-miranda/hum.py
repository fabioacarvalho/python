import csv

data = {
    ("NNS_FILIAL", "razao_social", "Filial do Sistema"),
    ("M0_FILIAL", "razao_social", "Nome da Filial"),
    ("M0_CGC", "cnpj", "CNPJ da Filial"),
    ("NNS_COD", "id", "Código da Solicitação"),
    ("NNS_DATA", "data", "Data de Emissão"),
    ("NNS_CLASS", "1", "Tipo de Documento de Entrada Fixado '1' – A CLASSIFICAR"),
    ("NNS_ESPECI", "SPED", "Espécie de Nota Fiscal"),
    ("NNS_XMENNF", "None", "Mensagem para Nota"),
    ("NNS_XTPFRE", "C", "Tipo do Frete Utilizado Fixado 'C' – CIF"),
    ("NNT_XNUM", "id_pedido", "ID Pedido"),
    ("NNT_XTRANSF", "id", "ID Transferencia"),
}

for item in data:
    key, desc, obj = item
    print(f"{key} | {desc} | {obj}\n")

with open("arquivo.csv", mode="w", newline="") as arq:
    rec = csv.writer(arq)
    rec.writerows(data)
