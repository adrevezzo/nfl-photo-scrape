import requests
from bs4 import BeautifulSoup

# url = 'https://www.nfl.com/players/active/a'
url = 'https://www.nfl.com/players/active/a?query=a&after=c2ltcGxlLWN1cnNvcjk5'


data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

rows = soup.find_all(class_="d3-o-media-object")

img_dict = {}

# print(rows[1].find_all('source')[])


for i in range(len(rows)):
    print(i)
    if rows[i].find_all('source'):
        link = (rows[i].find_all('source')[2])['srcset'].split(' ')[4].strip()
        name = rows[i].text.strip()
        img_dict[name] = link


for key,value in img_dict.items():
    fname = key
    with open(fname + '.png','wb') as f:
        im = requests.get(value)
        f.write(im.content)

# print(img_dict)