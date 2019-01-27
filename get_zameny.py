from bs4 import BeautifulSoup
import urllib.request
import datetime

date = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%d.%m.%y")

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_zameny(html):
    soup = BeautifulSoup(html, features="html.parser")
    link = soup.find('a', text=date)
    #print(link['href'])
    if link:
        return link['href']
    else:
        return 'Замен нет'

    #location = soup.find('div', class_="location__title-wrap").find('h1', class_="title title_level_1")
    #curr_location = str(location.contents[0]) + "" + str(location.find('span', class_="string-with-sticky-item").contents[0])
    #return str(time) + ". "+ curr_location + " " + str(value_temp)
