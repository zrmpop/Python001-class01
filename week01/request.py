import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

header = {'user-Agent': user_agent}

myurl = 'https://maoyan.com/films?showType=3&sortId=1'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')

counter = 0
movieList = []
movieList.append('=== Top 10 Movies List ===')
print('Run Start')
for dd in bs_info.find_all('dd', ):
    for channel_detail in dd.find_all('div', attrs={'class': 'channel-detail'}):
        for atag in channel_detail.find_all('a', ):
            if counter < 10:
                movie_title = atag.text
                movie_link = 'https://maoyan.com' + atag.get('href')
                counter = counter + 1
                movie = movie_title.strip() + ' link: ' + movie_link.strip()
                movieList.append(movie)
            else:
                break

movie1 = pd.DataFrame(data=movieList)
movie1.to_csv('./movieList1.csv', encoding='utf8',
              index=False, header=False)

print('Run End')
