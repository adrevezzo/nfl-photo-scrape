import requests
from bs4 import BeautifulSoup
import os.path

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']

url_ext = ['','c2ltcGxlLWN1cnNvcjk5','c2ltcGxlLWN1cnNvcjE5OQ=='],

for let in alph:
    print(let)

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
                    link = (rows[1].find_all('source'))[0]['srcset'].split(' ')[0].strip()
                    link = link.replace('t_lazy/', '')
                    name = rows[i].text.strip()
                    i=1
                    while name in img_dict:
                       name = f'{name}_v{i}'
                       i += 1

                    img_dict[name] = link

            for player,head_link in img_dict.items():
                fname = player
                # i = 1
                # while os.path.exists(fname+'.png'):
                #     print(f"{player} Exists")
                #     fname = f'{player}_v{i}'
                #     i += 1
                with open(fname + '.png','wb') as f:
                    im = requests.get(head_link)
                    f.write(im.content)


# Debugging Code
# url = f'https://www.nfl.com/players/active/a?query=''&after='''
# data = requests.get(url)
# soup = BeautifulSoup(data.text, 'html.parser')
# rows = soup.find_all(class_="d3-o-media-object")
#
# link = (rows[1].find_all('source'))[0]['srcset'].split(' ')[0].strip()
# link = link.replace('t_lazy/','')
# print(link)
#
# with open('test.png','wb') as f:
#     im = requests.get(link)
#     f.write(im.content)


