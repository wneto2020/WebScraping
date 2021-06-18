import requests
from bs4 import BeautifulSoup

def parser(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser').find_all('div', class_="col c9-2")
    return soup


def treatment(list_info: list):
    content = []
    if len(list_info) == 1:
        for data in list_info[0].find_all('b'):
            if data.next_element == "00814115000110" or data.next_element == " ":
                continue
            else:
                content.append(data.next_element)
        return content


def write(path, content):
    with open(path, 'a') as file:
        file.write(",".join(str(element) for element in content) + "\n")


if __name__ == '__main__':
    cnpj = "00814115000110"
    content = treatment(parser(f"https://cnpj.biz/{cnpj}"))
    write("info.xlsx", content)
