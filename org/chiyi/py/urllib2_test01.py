import requests


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = 'https://www.biqukan.com/1_1094/5403177.html'
    html = get_one_page(url)
    print(html)


main()
