import requests
from bs4 import BeautifulSoup
import datetime



url = "https://soccer365.ru/online/&date=2022-08-20"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
footbal_schedule = soup.find_all('div', class_='name')
match_datatime = soup.find_all('span', class_='size10')