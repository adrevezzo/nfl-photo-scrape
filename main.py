import requests
from bs4 import BeautifulSoup

# url = 'https://www.nfl.com/players/active/a'
# url = 'https://www.nfl.com/players/active/a?query=a&after=c2ltcGxlLWN1cnNvcjk5'

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']

url_ext = ['','c2ltcGxlLWN1cnNvcjk5','c2ltcGxlLWN1cnNvcjE5OQ=='],



for let in alph:

    for link in url_ext:
        try:
            url = f'https://www.nfl.com/players/active/{let}?query={let}&after={link}'
            data = requests.get(url)

        except:
            continue

        finally:
            soup = BeautifulSoup(data.text, 'html.parser')
            rows = soup.find_all(class_="d3-o-media-object")
            img_dict = {}

            for i in range(len(rows)):
                # print(i)
                if rows[i].find_all('source'):
                    link = (rows[i].find_all('source')[2])['srcset'].split(' ')[4].strip()
                    name = rows[i].text.strip()
                    img_dict[name] = link

            for player,head_link in img_dict.items():
                fname = player
                with open(fname + '.png','wb') as f:
                    im = requests.get(head_link)
                    f.write(im.content)
