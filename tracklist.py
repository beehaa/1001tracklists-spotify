# from selenium.webdriver.common.by import By
# driver.find_element(by=By.XPATH, value='//<your xpath>')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tracklist:
    # def __init__(self, slowMode=False, debug=False, checkCaptcha=True, timeToWait=3600) -> None:
        # self.timeOutSecs = 10 
        # self.scrollWaitTime = 5 
        # self.numTimesToScroll = 5 
    def __init__(self, url):
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.get(url)
        # try:
        #     WebDriverWait(self.driver, 5).until(EC.title_contains("Feed"))
        # except Exception as e:
        #     print("ERROR: logging error{}".format(e))
        #     print("Please solve captcha and then type 'c' or 'continue'")
        #     self.driver.switch_to.window(self.driver.current_window_handle) 
        self.driver.minimize_window()
        print("Logged into website")


    def quit(self):
        self.driver.quit()

URL = r'https://www.1001tracklists.com/tracklist/20nrw2tt/tiesto-club-life-819-tiesto-yearmix-2022-12-09.html'

tracklist_site_obj = Tracklist(URL)
print("Going to URL..")
# tracklist_site_obj.get_tracks()
tracklist_site_obj.quit()