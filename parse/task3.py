# Task3: beautiful soup test
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # beautifulsoup은 트리구조. Thus parent, children이 있음
print(soup.prettify())

tag =soup.a
print(tag)
print(tag.name)
print(tag.attrs)   #dictionary로 나옴
print(tag.string)
print(tag['class'])

print("/n")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.title.parent.name) # parent
print(soup.title.parent.title.string)
print(soup.head.contents[0].string) # contents : children as a list

for link in soup.find_all('a'):
    print(link.get('href'))  # 아래꺼랑 같음.
    print(link['href'])

print(soup.get_text())   # 모든 text string값들만

print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all ('a'))
print(soup.find(id='link3'))
print(soup.find(id='link3').string)
