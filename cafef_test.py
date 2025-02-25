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
import pandas as pd
import sys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .chrome_driver.chromedriver_setup import *

class browser_get_data():
    chrome_driver_path=get_chromedriver_path()
    def __init__(self,mck,fromdate,todate):
        self.mck = mck
        self.fromdate = fromdate
        self.todate = todate
        from .user_agent import random_user
        self.useragent=random_user()
        self.opt=Options()
        self.opt.add_argument('--headless')
        self.opt.add_argument('--dark-mode-settings')
        self.opt.add_argument("--incognito")
        self.opt.add_argument('--disable-gpu')
        self.opt.add_argument('--no-default-browser-check')
        self.opt.add_argument(f"user-agent={self.useragent}")
        self.br=webdriver.Chrome(options=self.opt)
        self.br.maximize_window()

        
    def ham_thuc_thi(self, url):
        self.br.get(url)
        mcp = self.br.find_element(By.ID, 'ContentPlaceHolder1_ctl00_acp_inp_disclosure')
        mcp.clear()
        mcp.send_keys(self.mck)
        WebDriverWait(self.br, 10).until(EC.presence_of_element_located((By.ID, 'date-inp-disclosure')))
        self.br.find_element(By.ID, 'date-inp-disclosure').send_keys(f'{self.fromdate} - {self.todate}')
        
        # JavaScript code ở đây
        apply_button = self.br.find_element(By.CLASS_NAME, 'applyBtn')
        self.br.execute_script("arguments[0].click();", apply_button)
        self.br.find_element(By.ID, 'owner-find').click()
    
    def ham_thuc_thi_2(self, url):
        self.br.get(url)
        mcp = self.br.find_element(By.ID, 'ContentPlaceHolder1_ctl00_acp_inp_disclosure')
        mcp.clear()
        mcp.send_keys(self.mck)
        WebDriverWait(self.br, 35).until(EC.presence_of_element_located((By.ID, 'date-inp-disclosure')))
        self.br.find_element(By.ID, 'date-inp-disclosure').send_keys(f'{self.fromdate} - {self.todate}')
        
        # JavaScript code ở đây
        apply_button = self.br.find_element(By.CLASS_NAME, 'applyBtn')
        self.br.execute_script("arguments[0].click();", apply_button)
        self.br.find_element(By.ID, 'owner-find').click()

    def lich_su_gia(self):
        url = f'https://s.cafef.vn/Lich-su-giao-dich-{self.mck}-1.chn'
        self.ham_thuc_thi(url)
        self.number_page = self.number_of_pages()
        self.data = self.getdata()
        self.data.rename(columns={'Giá (nghìn VNĐ)': 'Giá Đóng cửa', 'Giá (nghìn VNĐ).1': 'Giá Điều chỉnh',
                             'GD khớp lệnh': 'KLGD khớp lệnh', 'GD khớp lệnh.1': 'GTGD khớp lệnh',
                             'GD thỏa thuận': 'KLGD thỏa thuận', 'GD thỏa thuận.1': 'GTGD thỏa thuận',
                             'Giá (nghìn VNĐ).2': 'Giá Mở cửa', 'Giá (nghìn VNĐ).3': 'Giá Cao nhất',
                             'Giá (nghìn VNĐ).4': 'Giá thấp nhất','SLCP sau GD':'SL Cổ Phiếu sau GD'}, inplace=True)
        return self.data.reset_index(drop=True)

    def co_dong_noi_bo(self):
        url = f'https://s.cafef.vn/Lich-su-giao-dich-{self.mck}-6.chn'
        self.ham_thuc_thi(url)
        self.number_page = self.number_of_pages()
        self.data = self.getdata()
        self.data.rename(columns={'Người liên quan': 'Tên (Người liên quan)', 'Người liên quan.1': 'Chức vụ (Người liên quan)',
                                  'SLCP trước GD': 'SL Cổ Phiếu trước GD', 'Đăng ký': 'Đăng ký Mua',
                                  'Đăng ký.1': 'Đăng ký Bán', 'Đăng ký.2': 'Ngày ĐK thực hiện',
                                  'Đăng ký.3': 'Ngày ĐK kết thúc', 'Kết quả': 'Kết quả Mua',
                                  'Kết quả.1': 'Kết quả Bán','Kết quả.2':'Ngày TH'}, inplace=True)
        return self.data#.reset_index(drop=True)
    
    def giao_dich_khoi_ngoai(self):
        url = f'https://s.cafef.vn/lich-su-giao-dich-{self.mck}-3.chn#data'
        self.ham_thuc_thi(url)
        self.number_page = self.number_of_pages()
        self.data = self.getdata()
        self.data.rename(columns={'Giao dịch ròng':'KL Giao dịch ròng','Giao dịch ròng.1':'GT Giao dịch ròng (tỷVNĐ)',
                                 'Mua':'KL Mua','Mua.1':'GT Mua (tỷVNĐ)','Bán':'KL Bán','Bán.1':'GT Bán (tỷVNĐ)'}, inplace=True)
        return self.data       
    

    def thong_ke_dat_lenh(self):
        url = f'https://s.cafef.vn/lich-su-giao-dich-{self.mck}-2.chn#data'
        self.ham_thuc_thi(url)
        self.number_page = self.number_of_pages()
        self.data = self.getdata()
        self.data.rename(columns={'Mua':'Lệnh Mua','Mua.1':'KL Mua','Mua.2':'KLTB 1 Lệnh','Bán':"Lệnh Bán",
                                 'Bán.1':'KL Bán','Bán.2':'KLTB 1 Lệnh'}, inplace=True)
        return self.data.reset_index(drop=True)


    def giao_dich_tu_doanh(self):
        url = f'https://s.cafef.vn/lich-su-giao-dich-{self.mck}-4.chn#data'
        self.ham_thuc_thi_2(url)
        self.number_page = self.number_of_pages()
        self.df, self.data = self.getdata2()
        self.data.rename(columns={'Giao dịch ròng':'KL Giao dịch ròng','Giao dịch ròng.1':'GT Giao dịch ròng (tỷVNĐ)',
                                  'Mua':'KL Mua','Mua.1':'GT Mua (tỷVNĐ)','Bán':'KL Bán','Bán.1':'GT Bán (tỷVNĐ)'}, inplace=True)
        return self.df, self.data        

    def number_of_pages(self):
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        try:
            # Wait for the pagination elements to be present
            WebDriverWait(self.br, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'pagination-item')))
            
            pagination_items = self.br.find_elements(By.CLASS_NAME, 'pagination-item')
            
            # Extract page numbers as integers
            page_numbers = [int(item.text.strip()) for item in pagination_items if item.text.strip().isdigit()]
        except:
            WebDriverWait(self.br, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'pagination-item')))
            
            pagination_items = self.br.find_elements(By.CLASS_NAME, 'pagination-item')
            
            # Extract page numbers as integers
            page_numbers = [int(item.text.strip()) for item in pagination_items if item.text.strip().isdigit()]
        return max(page_numbers)


    def getdata(self):
        self.lis=[]
        self.end_page=self.number_of_pages()
        self.count=0
        while self.count!=self.end_page:
            time.sleep(0.6)
            self.br.find_element(By.ID,'paging-right').click()
            df=self.dataframe()
            self.lis.append(df)
            self.count+=1
        data=pd.concat(self.lis)
        return data

    def getdata2(self):
        self.lis=[]
        self.end_page=self.number_of_pages()
        self.count=0
        while self.count!=self.end_page:
            time.sleep(0.6)
            self.br.find_element(By.ID,'paging-right').click()
            df,df2=self.dataframe_2()
            self.lis.append(df2)
            self.count+=1
        data=pd.concat(self.lis)
        return df,data

    def dataframe(self):
        import pandas as pd
        df=pd.read_html(self.br.page_source,encoding='utf-8',header=0)
        data=pd.DataFrame(df[1])
        data=data.drop(index=0)
        return data

    def dataframe_2(self):
        import pandas as pd
        df=pd.read_html(self.br.page_source,encoding='utf-8',header=0)
        data=pd.DataFrame(df[1])
        data2=pd.DataFrame(df[2])
        data2=data2.drop(index=0)
        return data, data2
    
    
    def close(self):
        self.br.quit()