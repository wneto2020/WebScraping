import requests
from bs4 import BeautifulSoup

lista_final = []

lista_final2 = []

url = "https://cnpj.biz/00814115000110"

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

lista_info = soup.find_all('div', class_="col c9-2")
print(len(lista_info))
if len(lista_info) == 1:
    lista_infop = lista_info[0]
    lista = lista_infop.find_all('p')
    lista2 = lista_infop.find_all('b')

    for lista_dados in lista:
        lista_final.append(lista_dados.next_element)

    for lista_dados2 in lista2:
        lista_final2.append(lista_dados2.next_element)


for x in zip(lista_final,lista_final2):
    print(x)


