from bs4 import BeautifulSoup
import urllib.request
import datetime
import requests

date = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%d.%m.%y")

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

download_file_from_google_drive('1N2EoSfbIaW-NZtJ4hMrwAnbaLcteOaLB', '/home/opass081/Projects/%s.doc' % date)
# if __name__ == "__main__":
#     file_id = 'TAKE ID FROM SHAREABLE LINK'
#     destination = 'DESTINATION FILE ON YOUR DISK'
#     download_file_from_google_drive(file_id, destination)

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_zameny(html):
    soup = BeautifulSoup(html, features="html.parser")
    link = soup.find('a', text=date)
    id_from_url = link.split('/d/')
    print(link['href'])

    # link = soup.find(format(datetime.now().date().strftime("%d.%m.%y")))
    # print(link)

# get_zameny(get_html('http://uksivt.ru/zameny'))
