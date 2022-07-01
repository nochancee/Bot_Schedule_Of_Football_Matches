import requests
from bs4 import BeautifulSoup
import datetime


date_today = datetime.datetime.today().strftime("%Y-%m-%d")
url_without_date = "https://soccer365.ru/online/&date="
url = url_without_date + date_today
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
footbal_schedule = soup.find_all('div', class_='name')
match_datatime = soup.find_all('span', class_='size10')