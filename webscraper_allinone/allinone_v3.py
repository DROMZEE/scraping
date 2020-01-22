from bs4 import BeautifulSoup
from pyexcel_ods3 import save_data
import requests

base_url = 'https://www.webscraper.io/test-sites/e-commerce/allinone/'

dic_list = {}

lap_list, tab_list, phone_list = [], [], []

for page in ['computers/laptops', 'computers/tablets/', 'phones/touch']:
    url = base_url + page
    res = requests.get(url)

    if (res.status_code != 200) :
        print(f'Connection failed. Code : {res.status_code}')
        continue

    soup = BeautifulSoup(res.content, 'html.parser')

    title = soup.find_all('a' , {'class': 'title'})
    price = soup.find_all('h4', {'class': 'price'})

    for j in range(len(title)) :

        # Create 3 Sheets : Laptops, Tablets, Phones
        if (url == base_url + 'computers/laptops') :
            lap_list.append((title[j].text, price[j].text))

        if (url == base_url + 'computers/tablets/') :
            tab_list.append((title[j].text, price[j].text))

        if (url == base_url + 'phones/touch') :
            phone_list.append((title[j].text, price[j].text))

dic_list['Laptops'] = lap_list
dic_list['Tablets'] = tab_list
dic_list['Phones']  = phone_list

filename = 'opti_scrap.ods'
save_data(filename, dic_list)

print(f'Your file {filename} has been created !')