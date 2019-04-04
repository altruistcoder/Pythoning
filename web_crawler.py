import requests
from bs4 import BeautifulSoup


def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    links = soup.findAll('a')

    urls = [link['href'] for link in links if link.has_attr('href') and link['href'].startswith('http')]

    '''
    urls = []

    for link in links:
        try:
            urls.append(link['href'])
        except:
            pass
    '''
    return urls


def spider(url, limit=100):
    pagesToVisit = [url]
    pagesVisited = []

    while len(pagesVisited) < limit and pagesToVisit != []:
        new_links = []
        url = pagesToVisit.pop(0)
        pagesVisited.append(url)
        print("Visiting "+url)
        try:
            new_links = get_links(url)
        except:
            pass
        for link in new_links:
            if link not in pagesVisited and link not in pagesToVisit:
                pagesToVisit.append(link)
    print(len(pagesVisited))
    print(pagesVisited)


if __name__ == "__main__":
    name = input("Enter the URL of an initial website: ")
    limit = int(input("Enter the limit: "))
    spider(name, limit)
