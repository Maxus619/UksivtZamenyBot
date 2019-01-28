from bs4 import BeautifulSoup
import urllib.request
import datetime
import requests
import win32com.client as win32

# date = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
date = '29.01.2019'

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

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def save_zameny(html):
# def save_zameny(html, date):
    soup = BeautifulSoup(html, features="html.parser")
    link = soup.find('a', text=date)
    id_from_url = link['href'].split('?id=')[-1]
    download_file_from_google_drive(id_from_url, './zameny/%s.doc' % date)

def read_zameny():
# def read_zameny(date):
    word = win32.Dispatch("Word.Application")
    word.Visible = 0
    word.Documents.Open('./zameny/' + date + '.doc')
    doc = word.ActiveDocument
    print(doc.Tables.Count)

read_zameny()
# save_zameny(get_html('http://uksivt.ru/zameny'), date)
