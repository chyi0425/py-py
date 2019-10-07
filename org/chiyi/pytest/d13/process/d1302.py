from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(fileName):
    print('开始下载%s......' % fileName)
    timeToDownload = randint(5, 10)
    sleep(timeToDownload)
    print('%s下载完成！耗费了%d秒' % (fileName, timeToDownload))

def main():
    start = time()
    p1 = Process(target=download_task,args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task,args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
    main()
