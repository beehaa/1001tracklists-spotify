
# import selenium
# print(selenium.__version__)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from selenium.common.exceptions import NoSuchElementException

class Tracklist:
    def __init__(self, url):
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--disable-setuid-sandbox')
        # self.chrome_options.add_argument('--dns-prefetch-disable')
        # self.chrome_options.add_argument("--disable-dev-shm-usage")
        # self.chrome_options.add_argument('--disable-gpu')
        # self.chrome_options.add_argument("--window-size=1200x900")
        # self.chrome_options.add_argument('--hide-scrollbars')
        # self.chrome_options.add_argument('--enable-logging')
        # self.chrome_options.add_argument('--log-level=0')
        # self.chrome_options.add_argument('--v=99')
        # self.chrome_options.add_argument('--single-process')
        # self.chrome_options.add_argument('--ignore-certificate-errors')
        # self.chrome_options.add_argument("--disable-extensions")
        # self.chrome_options.add_argument("enable-automation")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)

        # t = time.time()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
        except TimeoutException:
            self.driver.execute_script("window.stop();")
        # print('Time consuming:', time.time() - t)

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'tlpItem')))
        tracks = self.driver.find_elements(by=By.CLASS_NAME, value='tlpItem')
        
        self.title_xpath = '//*[@id="tlTab"]/meta[1]'
        self.playlist_title = self.driver.find_element(by=By.XPATH, value=self.title_xpath).get_attribute("content")

        self.tracknames = []
        self.spotify_links = [] 
        self.tracks_dict = {}

        for i in range(len(tracks)):
            try: 
                title = None 
                link = None 
                id = tracks[i].get_attribute('data-id')

                title = self.driver.find_element(by=By.XPATH, value=f'//*[@id="tlp{i}_content"]/meta[1]').get_attribute("content")
                
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="tlp_{id}"]/div[3]/i[3]')))
                spotify_button = self.driver.find_element(by=By.XPATH, value=f'//*[@id="tlp_{id}"]/div[3]/i[3]')
                self.driver.execute_script("arguments[0].click();", spotify_button)

                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="tlp_{id}_player"]/div/div/iframe')))
                link = self.driver.find_element(by=By.XPATH, value=f'//*[@id="tlp_{id}_player"]/div/div/iframe').get_attribute("src")

                if title and link:
                    self.tracknames.append(title)
                    self.spotify_links.append(link)
                    self.tracks_dict[title] = link
            except NoSuchElementException:
                print(f"NoSuchElementException: cannot find {i}")
            except TimeoutException:
                print(f"TimeoutException: cannot find {i}")
        
        print(f"Found {len(self.tracknames)}/{len(tracks)} tracks.")
    
    def get_track_list(self):
        return self.tracknames 

    def get_clean_spotify_links(self):
        spot_ids = ["spotify:track:"+i.split('track/')[1] for i in self.spotify_links]
        return spot_ids

    def get_dict(self):
        return self.tracks_dict

    def quit(self):
        self.driver.quit()

    def get_title(self):
        if len(self.playlist_title)==0:
            return 'New Playlist'
        return self.playlist_title

