import requests
from bs4 import BeautifulSoup

bitcoin_response = requests.get('https://www.boursorama.com/bourse/devises/cryptomonnaies-bitcoin-euro-BTC-EUR/')

soup = BeautifulSoup(bitcoin_response.content, 'html.parser')

#print(soup.find_all('span', {'class': 'c-instrument'}))

faceplate__info = soup.find_all('div', {'class': 'c-faceplate__info'})

cours_eur_btc = faceplate__info[0].find_all('span', {'class': 'c-instrument'})

prix_eur_btc = cours_eur_btc[0].text
variation_eur_btc = cours_eur_btc[1].text

print(f'le bitcoin vaut {prix_eur_btc} euros.')
print(f"Il a varié de {variation_eur_btc}")