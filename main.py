import requests
from bs4 import BeautifulSoup

# url = 'https://www.nfl.com/players/active/a?query=c2ltcGxlLWN1cnNvcjk5'
url = 'https://www.nfl.com/players/active/a?query=a&after=c2ltcGxlLWN1cnNvcjk5'


data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

# links = soup.find_all(class_="img-responsive")
# print(links)

rows = soup.select(".d3-o-media-object img")
print(rows)
links = [img['src'] for img in rows]
print(links)
# players = [row.text for row in rows]
# print(players)

# with open(fname + '.png', 'wb') as f:
#     im = requests.get(link)
#     f.write(im.content)


#
for i, row in enumerate(links):
    fname = str(i)
    with open(fname + '.png','wb') as f:
        im = requests.get(row)
        f.write(im.content)