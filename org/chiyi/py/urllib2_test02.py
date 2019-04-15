# _*_ coding:UTF-8 _*_
import requests
import MySQLdb
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }
    target = 'http://10.1.100.11:9112/measures/filter/1'
    req = requests.get(url=target, headers=headers)
    req.encoding = 'UTF-8'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(bf.prettify())

    t_body = soup.find(name='tbody')

    div_contents = t_body.find_all(name='tr')
    for div_content in div_contents:
        if len(list(div_content.children))!= 17:
            continue
        print(div_content.find(name='a').text)
        m_bugs = div_content.find('span', id='m_bugs').text
        print('-----')
        print(m_bugs)
