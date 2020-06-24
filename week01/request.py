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
    for channel_detail in dd.find_all('div', attrs={'class': 'movie-item film-channel'}):
        if counter < 10:
            counter += 1
            movie_title = channel_detail.find(
                'span', attrs={'class': 'name'}).text
            movie_link = 'https://maoyan.com' + channel_detail.find(
                'a', attrs={'data-act': 'movie-click'}).get('href')
            hover_tags = channel_detail.find_all(
                'span', attrs={'class': 'hover-tag'})
            movie_cat = hover_tags[0].next_sibling.strip()
            movie_time = hover_tags[2].next_sibling.strip()
            movie = movie_title.strip() + ', category: ' + movie_cat + ', online_time: ' + \
                movie_time + ', link: ' + movie_link.strip()
            movieList.append(movie)
        else:
            break

movie1 = pd.DataFrame(data=movieList)
movie1.to_csv('./movieList1.csv', encoding='utf8',
              index=False, header=False)

print('Run End')
