import requests
from bs4 import BeautifulSoup
from pyexcel_ods3 import save_data


computers_url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers"
tablets_url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
url = "https://www.webscraper.io/test-sites/e-commerce/allinone"

allinone_response = requests.get(tablets_url)

soup = BeautifulSoup(allinone_response.content, 'html.parser')

#print(soup.find_all('span', {'class': 'c-instrument'}))

captions = soup.find_all('div', {'class': 'caption'})

#print(caption)
for c in range(len(captions)):
    #print(c.text)
    caption_title = captions[c].find_all('a', {'class': 'title'})
    caption_prix = captions[c].find_all('h4', {'class': 'pull-right price'})
    titre = caption_title[0].text
    prix = caption_prix[0].text
    print(titre, prix)

#data = OrderedDict() # from collections import OrderedDict
#data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})


# 

#prix_eur_btc = cours_eur_btc[0].text
#variation_eur_btc = cours_eur_btc[1].text

#print(f'le bitcoin vaut {prix_eur_btc} euros.')
#print(f"Il a varié de {variation_eur_btc}")

