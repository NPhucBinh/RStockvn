# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.10.2"
__author__ ="Nguyen Phuc Binh"
__copyright__ = "Copyright 2023, Nguyen Phuc Binh"
__license__ = "MIT"
__email__ = "nguyenphucbinh67@gmail.com"
__website__ = "https://github.com/NPhucBinh"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from .chrome_driver.chromedriver_setup import *


class browser_lay_lai_suat():
    
    def __init__(self):
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from .user_agent import random_user
        self.useragent=random_user()
        self.url='https://s.cafef.vn/lai-suat-ngan-hang.chn#data'
        self.opt=Options()
        self.opt.add_argument('--headless')
        self.opt.add_argument('--dark-mode-settings')
        self.opt.add_argument("--incognito")
        self.opt.add_argument('--disable-gpu')
        self.opt.add_argument('--no-default-browser-check')
        self.opt.add_argument(f"user-agent={self.useragent}")
        self.br=webdriver.Chrome(options=self.opt)
        self.br.maximize_window()
        self.br.get(self.url)
    
    def getdata(self):
        import pandas as pd
        self.data=pd.read_html(self.br.page_source)[-1]
        return self.data
    
    def close(self):
        self.br.quit()