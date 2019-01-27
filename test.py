from bs4 import BeautifulSoup
import urllib.request
import datetime

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_zameny(html):
    soup = BeautifulSoup(html, features="html.parser")
    #date = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%d.%m.%y")
    date = '28.01.2019'

    #links = soup.findAll('a', {'rel': 'noopener'})

    #for link in soup.find_all(['a', href=True]):
    link = soup.find('a', text=date)
    print(link['href'])


    # link = soup.find(format(datetime.now().date().strftime("%d.%m.%y")))
    # print(link)

get_zameny(get_html('http://uksivt.ru/zameny'))
