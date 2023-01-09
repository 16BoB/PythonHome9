import requests
from bs4 import BeautifulSoup as bs
url = "https://pogoda.mail.ru/prognoz/moskva/"
response = requests.get(url).text
soup = bs(response, 'html.parser')
temperature = soup.find('div', class_="information__content__temperature").get_text(strip=True)
print(f'Температура в Москве: {temperature}')
