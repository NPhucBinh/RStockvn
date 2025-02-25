# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.10"
__author__ ="Nguyen Phuc Binh"
__copyright__ = "Copyright 2023, Nguyen Phuc Binh"
__license__ = "MIT"
__email__ = "nguyenphucbinh67@gmail.com"
__website__ = "https://github.com/NPhucBinh"

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os
from ..user_agent import random_user
from ..chrome_driver.chromedriver_setup import *

useragent = random_user()
package_path = os.path.dirname(__file__)
data_path = os.path.join(package_path)
path_nganh = os.path.join(package_path, 'dsnganh.xlsx')
list_company_path = os.path.join(package_path, 'list_company.xlsx')
save_list = os.path.join(package_path, 'ds_ngành_đã_lọc.xlsx')

def load_list_company():
    try:
        path_nganh_check = os.path.join(package_path, 'dsnganh.xlsx')
        if not os.path.exists(path_nganh_check):
            return 'Giới hạn thành viên, nếu bạn đã được cấp phép. Sử dụng hàm key_id(Mã id) để kích hoạt'
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument("user-agent={}".format(useragent))
        br = webdriver.Chrome(options=opt)
        br.get('https://24hmoney.vn/companies')
        trang = br.find_element(By.CLASS_NAME, 'change-page').text
        number_page = int(trang[trang.index('/') + 1:].strip())
        br.quit()
        count = int(1)
        list_df = []
        for count in range(1, number_page + 1):
            df = pd.read_html(f'https://24hmoney.vn/companies?industry_code=all&floor_code=all&com_type=all&letter=all&page={count}', encoding='utf8')[0]
            list_df.append(df)
        data = pd.concat(list_df)
        data.to_excel(list_company_path, index=False)
    except FileNotFoundError:
        return 'Giớn hạn thành viên, nếu bạn đã được cấp phép. Sử dụng hàm key_id(Mã id) để kích hoạt'





def update_list_company():
    try:
        path_nganh_check = os.path.join(package_path, 'dsnganh.xlsx')
        if not os.path.exists(path_nganh_check):
            return 'Giới hạn thành viên, nếu bạn đã được cấp phép. Sử dụng hàm key_id(Mã id) để kích hoạt'
        df1 = pd.read_excel(path_nganh_check)
        df1 = df1.applymap(lambda x: x.upper() if isinstance(x, str) else x)
        dfnganh4 = df1.drop_duplicates(subset='Ngành - ICB cấp 4', keep='first')
        dfnganh3 = df1.drop_duplicates(subset='Ngành - ICB cấp 3', keep='first')
        dfnganh2 = df1.drop_duplicates(subset='Ngành - ICB cấp 2', keep='first')
        dfnganh1 = df1.drop_duplicates(subset='Ngành - ICB cấp 1', keep='first')

        def loc_cap3(df):
            i = df['Ngành - ICB cấp 3']
            kq = dfnganh4[dfnganh4['Ngành - ICB cấp 3'] == i]['Ngành - ICB cấp 4'].tolist()
            return {i: kq}

        data_cap3 = dfnganh4.apply(loc_cap3, axis=1)
        def loc_cap2(df):
            i = df['Ngành - ICB cấp 2']
            kq = dfnganh3[dfnganh3['Ngành - ICB cấp 2'] == i]['Ngành - ICB cấp 3'].tolist()
            return {i: kq}

        data_cap2 = dfnganh2.apply(loc_cap2, axis=1)
        def loc_cap1(df):
            i = df['Ngành - ICB cấp 1']
            kq = dfnganh2[dfnganh2['Ngành - ICB cấp 1'] == i]['Ngành - ICB cấp 2'].tolist()
            return {i: kq}

        data_cap1 = dfnganh1.apply(loc_cap1, axis=1)

        if not os.path.exists(list_company_path):
            load_list_company()

        df_company = pd.read_excel(list_company_path)
        df_company = df_company.drop(df_company[df_company['Ngành'] == '-'].index)
        df_company = df_company.applymap(lambda x: x.upper() if isinstance(x, str) else x)
        dict_cap3 = {}
        for d in data_cap3:
            dict_cap3.update(d)

        dict_cap2 = {}
        for d in data_cap2:
            dict_cap2.update(d)
        

        dict_cap1 = {}
        for d in data_cap1:
            dict_cap1.update(d)
        
        dict_cap3['DU LỊCH & GIẢI TRÍ'].append('HÀNG KHÔNG')

        def lay_gia_tri_cap3(category):
            for key, values in dict_cap3.items():
                if category in values:
                    return key

        def lay_gia_tri_cap2(category):
            for key, values in dict_cap2.items():
                if category in values:
                    return key

        def lay_gia_tri_cap1(category):
            for key, values in dict_cap1.items():
                if category in values:
                    return key

        df_company['Ngành'] = df_company['Ngành'].str.upper()
        df_company['Ngành Cấp 3'] = df_company['Ngành'].apply(lay_gia_tri_cap3)
        df_company['Ngành Cấp 2'] = df_company['Ngành Cấp 3'].apply(lay_gia_tri_cap2)
        df_company['Ngành Cấp 1'] = df_company['Ngành Cấp 2'].apply(lay_gia_tri_cap1)
        df_company.to_excel(save_list, index=False)
        print('Đã cập nhật')
        return df_company
    except FileNotFoundError:
        return 'Giớn hạn thành viên, nếu bạn đã được cấp phép. Sử dụng hàm key_id(Mã id) để kích hoạt'


def list_company_24h():
    try:
        try:
            save_list = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ds_ngành_đã_lọc.xlsx')
            data = pd.read_excel(save_list)
        except FileNotFoundError:
            df = update_list_company()
            data = pd.read_excel(save_list)
        return data
    except FileNotFoundError:
        return 'Giớn hạn thành viên, nếu bạn đã được cấp phép. Sử dụng hàm key_id(Mã id) để kích hoạt'

#if __name__ == "__main__":
