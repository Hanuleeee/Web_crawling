from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver'  # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

descriptions = []

browser = webdriver.Chrome(executable_path=driver_path)  # Chrome driver
browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")

for link in soup.find_all('div', {'class': 'W9yFB'}):
    ranking_url = link.a['href']  # extracting a ranking url

    browser.get(ranking_url)
    soup_ranking = BeautifulSoup(browser.page_source, "html.parser")


# <a href="/store/apps/details?id=com.cassette.aquapark"><div class="WsMG1c nnK0zc">aquapark.io</div></a> 여기서 가져옴.
    for game_link in soup_ranking.find_all('div', {'class': 'WsMG1c nnK0zc'})[0:1]:  # 모든걸 찾아서 하나만 가져와라
        browser.get("http://play.google.com" + game_link.parent['href'])
        soup_game = BeautifulSoup(browser.page_source, "html.parser")

        descriptions.append(soup_game.find('meta', {'itemprop': 'description'})['content'])
        # <meta itemprop="description" content="Reach to the end of the water slide, try to be the first. Bump other players during the race and have fun playing this colorful and sunny water slide game.
        # 물의 끝까지 도달 슬라이드, 첫 번째가되도록하십시오. 경주 중 다른 플레이어와 충돌하고 재미 있고 다채로운이 맑은 물 슬라이드 게임을 즐기십시오.
        # ">    // itemprop값이 description을 갖는 meta tag에서 content값을 가져와라. 그래서 description에 append!
browser.quit()

print(len(descriptions))

with open('description.txt', 'a', encoding="utf8") as f:
    for item in descriptions:
        f.write(item)
