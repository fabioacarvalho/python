import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/s?k=macbook+air+m2&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=306DF9LJYP9T9&sprefix=macbook+air+m%2Caps%2C220&ref=nb_sb_noss_2'

# Into google.com and search for "my user agent"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

site = requests.get(url=url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

print(soup)