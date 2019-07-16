
from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver' # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

descriptions = []

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)
page = browser.page_source

# 3개 url을 찾아서 각각다 열어봄
soup = BeautifulSoup(page, "html.parser")
links = soup.find_all('div', {'class': 'W9yFB'}) # find all links to rankings

# pages=[]
for link in links:
    new_url = link.a['href']
    browser.get(new_url)
    # pages.append(browser.page_source)
    soup_ranking = BeautifulSoup(browser.page_source, "html.parser")
    links_detail = soup_ranking.find_all('div', {'class':'wXUyZd'})[1:2]

    for game_link in links_detail:

        browser.get("http://play.google.com" + game_link.a['href'])
        soup_game = BeautifulSoup(browser.page_source, "html.parser")
        game = soup_game.find('div', {'jsname': 'sngebd'}).get_text()  #.string은 <br>tag때문에 None값이 들어옴. Thus, get_text() 사용
        descriptions.append(game)
print(descriptions)
browser.quit()

with open('description.txt', 'a', encoding="utf8") as f:
    for item in descriptions:
        f.write(item)