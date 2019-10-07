from random import randint
from time import time, sleep


def download_task(fileName):
    print('开始下载%s......' % fileName)
    timeToDownload = randint(5, 10)
    sleep(timeToDownload)
    print('%s下载完成！耗费了%d秒' % (fileName, timeToDownload))

def main():
    start = time()
    download_task('python从入门到住院.pdf')
    download_task('Peking hot.avi')
    end = time()
    print('总共耗费了%.2f秒。' % (end-start))

if __name__ == "__main__":
    main()
