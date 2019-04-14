# _*_ coding:UTF-8 _*_
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }
    target = 'https://www.xbiquge6.com/0_638/1124120.html'
    req = requests.get(url=target, headers=headers)
    req.encoding = 'UTF-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(bf.prettify())
    div_content = soup.find(name='div', id='content')
    print(div_content.text)
