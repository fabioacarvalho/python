import requests
from bs4 import BeautifulSoup

url = "https://www.bing.com/search?q=cotacao+dolar+hoje"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}

requisicao = requests.get(url=url, headers=headers)

print(requisicao)
# print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())

print(site.title)

# titulo = site.find("title")
# print(titulo)

# input = site.find_all("input")
# print(input)

pesquisa = site.find("textarea", id="sb_form_q")
print("Value: " + pesquisa["value"])


print("\n --------------------------- \n")

cotacao = site.find("input", id="cc_tdv")
print("Cotação R$ -> $: " + cotacao["value"])