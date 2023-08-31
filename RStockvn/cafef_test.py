# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.8"
__author__ ="Nguyen Phuc Binh"
__copyright__ = "Copyright 2023, Nguyen Phuc Binh"
__license__ = "MIT"
__email__ = "nguyenphucbinh67@gmail.com"
__website__ = "https://github.com/NPhucBinh"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import sys
import time

class browser_get_data():
    
    def __init__(self,mck,fromdate,todate):
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        driver_manager = ChromeDriverManager()
        service = driver_manager.install()
        from selenium.webdriver.chrome.options import Options
        from .user_agent import random_user
        self.useragent=random_user()
        self.url='https://s.cafef.vn/lich-su-giao-dich-symbol-vnindex/trang-1-0-tab-1.chn'
        self.opt=Options()
        self.opt.add_argument('--headless')
        self.opt.add_argument('--dark-mode-settings')
        self.opt.add_argument("--incognito")
        self.opt.add_argument('--disable-gpu')
        self.opt.add_argument('--no-default-browser-check')
        self.opt.add_argument("user-agent={}".format(self.useragent))
        self.br=webdriver.Chrome(options=self.opt)
        self.br.maximize_window()
        self.br.get(self.url)
        self.mcp=self.br.find_element(By.ID,'ContentPlaceHolder1_ctl03_txtKeyword')
        self.mcp.clear()
        self.mcp.send_keys(mck)
        self.br.find_element(By.ID,'ContentPlaceHolder1_ctl03_dpkTradeDate1_txtDatePicker').send_keys(str(fromdate))
        self.br.find_element(By.ID,'ContentPlaceHolder1_ctl03_dpkTradeDate2_txtDatePicker').send_keys(str(todate))
        self.br.find_element(By.ID,'ContentPlaceHolder1_ctl03_btSearch').click()
    
    def getdata(self):
        self.lis=[]
        while True:
            time.sleep(0.6)
            try:
                self.br.find_element(By.LINK_TEXT,'>').click()
                df=self.dataframe()
                self.lis.append(df)
            except:
                df=self.dataframe()
                self.lis.append(df)
                break
        data=pd.concat(self.lis)
        data.drop(['Thay đổi (+/-%).1'],axis=1,inplace=True)
        data.rename(columns={'GD khớp lệnh':'KLGD khớp lệnh','GD khớp lệnh.1':'GTGD khớp lệnh','GD thỏa thuận':'KLGD thỏa thuận','GD thỏa thuận.1':'GTGD thỏa thuận'}, inplace=True)
        self.close()
        return data.set_index('Ngày')
    
    def dataframe(self):
        import pandas as pd
        df=pd.read_html(self.br.page_source,encoding='utf-8',header=0)
        data=pd.DataFrame(df[2])
        data=data.drop(index=0)
        return data
    def close(self):
        self.br.quit()