# Task 5: extract links to game ranks
from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver' # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)
page = browser.page_source

# 3개 url을 찾아서 각각다 열어봄
soup = BeautifulSoup(page, "html.parser")
links = soup.find_all('div', {'class': 'W9yFB'}) # find all links to rankings

for link in links:
    new_url = link.a['href']
    browser.get(new_url)

browser.quit()