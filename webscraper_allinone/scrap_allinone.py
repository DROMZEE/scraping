from bs4 import BeautifulSoup
import datetime
import pandas as pd
import requests

# Data recovery
url_base = "https://www.webscraper.io/test-sites/e-commerce/allinone/"

datalists = [['category', 'item', 'designation', 'price_in_$', 'scraping_date']]

items_to_scrap = items_to_scrap_counter = 0

today = datetime.date.today()

for x in ["computers/laptops", "computers/tablets", "phones"]:

  page = requests.get(f"{url_base}{x}")

  if (page.status_code != 200):
    print(f"Page not fetched correcly. Code {page.status_code}.")
    break
  
  soup = BeautifulSoup(page.content, 'html.parser')

  items_to_scrap_counter = len(soup.find_all('div', 
                                             attrs = {'class': 'caption'}))
  items_to_scrap += items_to_scrap_counter

  data = soup.get_text()

  data = list(filter(None, (data[data.find('$')-1:data.rfind('reviews')]).
                     split(sep='\n')))

  for y in range(0, len(data)+1, 5):
    items_list = []

    if x == "computers/laptops":
      items_list.extend([x, data[y+2].split(',',1)[0], 
                         data[y+2].split(',',1)[1], float(data[y][1:]), today])
    else:
      items_list.extend([x, data[y+1], data[y+2], float(data[y][1:]), today])
    
    datalists.append(items_list)


if page.status_code == 200:

  if len(datalists)-1 == items_to_scrap:
    print(f'{items_to_scrap} items have been scraped.')

  else:
    print('A problem occured. Some items are missing.')

# Dataframe creation
dataframe = pd.DataFrame.from_records(datalists[1:], columns = datalists[0])

# Save the dataframe in Excel format
filename = 'webscraping_webscraper_{}.xlsx'.format(str(today))

dataframe.to_excel(filename, sheet_name = 'WebScraper', index = None, 
                   header=True)