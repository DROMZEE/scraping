from bs4 import BeautifulSoup
import urllib.request

urlpage = 'https://www.perdu.com/'

page = urllib.request.urlopen(urlpage)

soup = BeautifulSoup(page, 'html.parser')

print(soup)