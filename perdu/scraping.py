import requests
from bs4 import BeautifulSoup

perdu_response = requests.get('http://perdu.com')
#print(perdu_response)
#print(perdu_response.content)

soup = BeautifulSoup(perdu_response.content, 'html.parser')

#print(f'Titre de la page: {soup.title.text}')
print(f'Titre de la page: {soup.title.contents[0]}')