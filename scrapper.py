import requests
from bs4 import BeautifulSoup
import datetime


date_today = datetime.datetime.today().strftime("%Y-%m-%d")
date_tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

url_without_date = "https://soccer365.ru/online/&date="

url = url_without_date + date_today
url_tomorrow = url_without_date + date_tomorrow

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
footbal_schedule = soup.find_all('div', class_='name')
match_datatime = soup.find_all('span', class_='size10')

response_tomorrow = requests.get(url_tomorrow)
soup_tomorrow = BeautifulSoup(response_tomorrow.text, 'lxml')
footbal_schedule_tomorrow = soup_tomorrow.find_all('div', class_='name')
match_datatime_tomorrow = soup_tomorrow.find_all('span', class_='size10')
