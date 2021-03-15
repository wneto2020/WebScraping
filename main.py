import requests
from bs4 import BeautifulSoup


def scraping(cnpj, caminho_arquivo):
    lista_title = []

    lista_info = []

    url = f"https://cnpj.biz/{cnpj}"

    req = requests.get(url)

    soup = BeautifulSoup(req.content, 'html.parser')

    lista_div = soup.find_all('div', class_="col c9-2")

    if len(lista_div) == 1:

        lista_info_med = lista_div[0]

        lista_p = lista_info_med.find_all('p')

        lista_b = lista_info_med.find_all('b')

        for dados_p in lista_p:
            lista_title.append(dados_p.next_element)

        for dados_b in lista_b:
            lista_info.append(dados_b.next_element)

        with open(caminho_arquivo, 'a') as file:
            file.write(",".join(str(element) for element in lista_info) + "\n")

scraping("00814115000110", "infos_corp.xls")
