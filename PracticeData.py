import requests
from bs4 import BeautifulSoup

def parser(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser').find_all('div', class_="col c9-2")
    return soup

def treatment(list_info: list):
    list_final = []
    list_final2 = []
    
    if len(list_info) == 1:
        for data in list_info[0].find_all('p'):
            list_final.append(data.next_element)

        for data2 in list_info[0].find_all('b'):
            if data2.next_element == "00814115000110" or data2.next_element == " ":
                continue
            else:
                list_final2.append(data2.next_element)
        return list_final, list_final2

if __name__ == '__main__':
    cnpj = "00814115000110"
    list_final, list_final2 = treatment(parser(f"https://cnpj.biz/{cnpj}"))

    for i in range(len(list_final2)):
        print(list_final[i], list_final2[i])


