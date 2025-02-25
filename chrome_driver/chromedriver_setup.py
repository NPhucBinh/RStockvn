# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.10"
__author__ ="Nguyen Phuc Binh"
__copyright__ = "Copyright 2023, Nguyen Phuc Binh"
__license__ = "MIT"
__email__ = "nguyenphucbinh67@gmail.com"
__website__ = "https://github.com/NPhucBinh"

import os
import chromedriver_autoinstaller
import requests
import platform

def get_chromedriver_path():
    current_dir = os.path.dirname(__file__)
    system_name = platform.system()

    if system_name == 'Windows':
        return os.path.join(current_dir, 'chrome_driver', 'windows', 'chromedriver.exe')
    elif system_name == 'Darwin':  # macOS
        # Kiểm tra kiến trúc của máy tính macOS
        mac_architecture = platform.machine()
        if "arm" in mac_architecture.lower():
            # Sử dụng chromedriver_mac_arm64.zip cho kiến trúc ARM64
            return os.path.join(current_dir, 'chrome_driver', 'macOS_arm', 'chromedriver')
        else:
            # Sử dụng chromedriver_mac64.zip cho kiến trúc x64
            return os.path.join(current_dir, 'chrome_driver', 'macOS', 'chromedriver')

    raise Exception("Unsupported operating system")






import gdown
from datetime import datetime, timedelta
import pandas as pd

def download_data(document_id):
    # Đường dẫn đến thư mục data trong gói package
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    #data_dir = os.path.join(os.path.dirname(__file__), 'data')
    chrome_dir = os.path.join(os.path.dirname(__file__),'')
    # Tạo đường dẫn cho tệp Excel
    linsce_path = os.path.join(data_path, 'linsce.txt')
    # Tải tệp Excel từ Google Drive
    url = f'https://drive.google.com/uc?id={str(document_id)}'
    gdown.download(url, linsce_path, quiet=True)
    # Đọc file lưu biến
    with open(linsce_path, 'r') as linsce:
        bien = linsce.readlines()
    
    name=bien[0].strip()
    day=int(bien[1].strip())
    id_file=bien[2].strip()
    json_data = os.path.join(data_path, name)
    url2 = f'https://drive.google.com/uc?id={id_file}'
    gdown.download(url2, json_data, quiet=True)
    current_time = datetime.now()
    delta = timedelta(days=day)    
    time_end = current_time + delta
    time_end = str(time_end.replace(microsecond=0))
    time_file_path = os.path.join(chrome_dir,'browser.txt')
    with open(time_file_path, 'w') as time_file:
        time_file.write(str(time_end))
    path_data = os.path.join(data_path,'dsnganh.xlsx')
    df=pd.read_json(json_data)
    df.to_excel(path_data)   
    os.remove(linsce_path)
    os.remove(json_data)
    key=generate_key()
    file_key=os.path.join(chrome_dir, 'snimdir.key')
    save_key(key, file_key)
    encrypt_file(time_file_path, key)
    return day



def check_var():
    try:
        data_dir = os.path.join(os.path.dirname(__file__))
        data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
        time_file_path = os.path.join(data_dir,'browser.txt')
        file_key=os.path.join(data_dir,'snimdir.key')
        with open(file_key, 'r') as key_save:
            keys = key_save.read()
        decrypt_file(time_file_path, keys)
        with open(time_file_path, 'r') as time_down:
            time_old = time_down.read()
        current_t_now=datetime.now()
        current_time = str(current_t_now.replace(microsecond=0))
        current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
        path_data = os.path.join(data_path,'dsnganh.xlsx')
        path_nganh = os.path.join(data_path,'ds_ngành_đã_lọc.xlsx')
        path_list = os.path.join(data_path,'list_company.xlsx')
        time_check=datetime.strptime(time_old, "%Y-%m-%d %H:%M:%S")
        if current_time > time_check:
            os.remove(time_file_path)
            os.remove(file_key)
            os.remove(path_data)
            os.remove(path_nganh)
            os.remove(path_list)
        else:
            encrypt_file(time_file_path, keys)
    except FileNotFoundError:
        return None


def remove_file_old():
    try:
        data_dir = os.path.join(os.path.dirname(__file__))
        data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
        path_data = os.path.join(data_path,'dsnganh.xlsx')
        browser_txt_path = os.path.join(data_dir, 'browser.txt')
        if not os.path.exists(browser_txt_path):
            os.remove(path_data)
    except FileNotFoundError:
        return None


from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def save_key(key, key_file):
    with open(key_file, 'wb') as f:
        f.write(key)



def load_key(key_file):
    with open(key_file, 'rb') as f:
        return f.read()



def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)




def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    decrypted_data = fernet.decrypt(data)
    with open(file_path, 'wb') as f:
        f.write(decrypted_data)


