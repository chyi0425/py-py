from urllib.request import urlopen
from math import sqrt
shakespeare = urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')
words = set(shakespeare.read().decode().split())

{w for w in words if len(w)>=5 and w[::-1] in words}