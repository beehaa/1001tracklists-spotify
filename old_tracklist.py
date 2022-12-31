import requests
from fake_headers import Headers
from bs4 import BeautifulSoup

URL = r'https://www.1001tracklists.com/tracklist/20nrw2tt/tiesto-club-life-819-tiesto-yearmix-2022-12-09.html'

class Tracklist:
    def __init__(self, url):
        self.url = url 
        self.tracklist_id = self.url.split('tracklist/')[1].split('/')[0]
        self.download()

    def download(self):
        response = requests.get(self.url, headers=Headers().generate())
        soup = BeautifulSoup(response.text, "html.parser")
        with open("output2.html", "w") as file:
            file.write(str(soup))
        self.title = soup.title.text
        self.tracks = []
        track_divs = soup.find_all('div')
        print(track_divs)
