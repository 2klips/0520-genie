import requests
from bs4 import BeautifulSoup

def genie(page):
    url = 'https://genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=12&rtm=Y&pg=' + page
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text)

    titles = soup.findAll('a', {'class':'title ellipsis'})
    artists = soup.findAll('a', {'class':'artist ellipsis'})
    numbers = soup.findAll('td', {'class':'number'})

    for t, a, n in zip(titles, artists, numbers):

        title = t.text.strip()
        artist = a.text.strip()
        number = n.text.strip().split('\n')[0]

        print('{0:3d}위 : {1:s} - {2:s}'.format(int(number), artist, title))


genie('1')
