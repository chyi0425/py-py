# coding: utf-8

# urlparse()

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

# <class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
# scheme://netloc/path;parameters?query#fragment

# result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=5', fragment='comment')


result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
print(result)

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5#comment', fragment='')
# 当URL中不包含params和query时，fragment便会被解析为path的一部分。
print(result)

result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result[0], result.netloc, result[2], result.scheme, sep='\n')

# urlunparse()

from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

# urlsplit()

from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[0])

# urlunsplit()

from urllib.parse import urlunsplit
data = ['http','www.baidu.com','index.html','a=6','comment']
print(urlunsplit(data))

# urljoin()

from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))