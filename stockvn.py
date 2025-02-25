# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.10.1"
__author__ ="Nguyen Phuc Binh"
__copyright__ = "Copyright 2023, Nguyen Phuc Binh"
__license__ = "MIT"
__email__ = "nguyenphucbinh67@gmail.com"
__website__ = "https://github.com/NPhucBinh"

import pandas as pd
import requests
import json
import os
from bs4 import BeautifulSoup
from .user_agent import random_user
from .cafef_test import browser_get_data
import datetime as dt
from .report_vnd import report_f_vnd, info_cp
from .data.ds_company import *
import time
from .ls_cafef import browser_lay_lai_suat
from .chrome_driver.chromedriver_setup import *



def get_info_cp(symbol):
    df=info_cp(symbol)
    return df

def momentum_ck(symbol):
    today=dt.datetime.now()
    fromday=today-dt.timedelta(days=8)
    endday=today-dt.timedelta(days=1)
    ed=str(endday.strftime('%d/%m/%Y'))
    fd=str(fromday.strftime('%d/%m/%Y'))
    df=get_price_historical_vnd(symbol,fd,ed)
    MOM=round((float(df['close'][0:1])/float(df['close'][-1:]))*100,3)
    return f"Chỉ số Momentum của {symbol.upper()} ngày {df['date'][0]} là {MOM}"


def get_foreign_historical_vnd(symbol,fromdate,todate):
    fromdate, todate = pd.to_datetime(fromdate, dayfirst=True), pd.to_datetime(todate, dayfirst=True)
    fdate, tdate=fromdate.strftime('%Y-%m-%d'), todate.strftime('%Y-%m-%d')
    url=f'https://finfo-api.vndirect.com.vn/v4/foreigns?sort=tradingDate&q=code:{symbol.upper()}~tradingDate:gte:{fdate}~tradingDate:lte:{tdate}&size=1000000&page=1' 
    head={"User-Agent":'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201'}
    payload={}
    r=requests.get(url,headers=head,data=payload)
    df=pd.DataFrame(r.json()['data'])
    return df
    

def get_price_historical_vnd(symbol,fromdate,todate):
    fromdate, todate = pd.to_datetime(fromdate, dayfirst=True), pd.to_datetime(todate, dayfirst=True)
    fdate, tdate=fromdate.strftime('%Y-%m-%d'), todate.strftime('%Y-%m-%d')
    url=f'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&q=code:{symbol.upper()}~date:gte:{fdate}~date:lte:{tdate}&size=100000&page=1' 
    head={"User-Agent":random_user()}
    payload={}
    r=requests.get(url,headers=head,data=payload)
    df=pd.DataFrame(r.json()['data'])
    data=df[['code','date','open','high','low','close','nmVolume','nmValue','ptVolume', 'ptValue','change','pctChange']].copy()

    data.rename(columns={'nmVolume':'KLGD Khớp lệnh','nmValue':'GTGD Khớp lệnh','ptVolume':'KLGD Thỏa thuận','ptValue':'GTGD Thỏa thuận','change':'tăng/giảm','pctChange':'% tăng/giảm'}, inplace=True)
    return data

def key_id(document_id):
    day=download_data(str(document_id))
    return f'Đã kích hoạt {day} ngày'



def get_data_result_order(symbol,fromdate,todate):
    
    data=browser_get_data(symbol,fromdate,todate).thong_ke_dat_lenh()
    return data

def get_price_history_cafef(symbol,fromdate,todate):
    
    data=browser_get_data(symbol,fromdate,todate).lich_su_gia()
    return data


def get_insider_transaction_history_cafef(symbol,fromdate,todate):### 20
    
    data=browser_get_data(symbol,fromdate,todate).co_dong_noi_bo()
    return data


def get_foreign_transaction_history_cafef(symbol,fromdate,todate):### 20
    
    data=browser_get_data(symbol,fromdate,todate).giao_dich_khoi_ngoai()
    return data


def get_proprietary_history_cafef(symbol,fromdate,todate):### 20
    
    data=browser_get_data(symbol,fromdate,todate).giao_dich_tu_doanh()
    return data



def lai_suat_cafef():
    data=browser_lay_lai_suat().getdata()
    return data


def list_company():
    data=list_company_24h()
    return data


def update_company():
    package_path = os.path.dirname(__file__)
    data_path = os.path.join(package_path, 'data')
    path_nganh = os.path.join(data_path, 'dsnganh.xlsx')
    save_list = os.path.join(data_path, 'ds_ngành_đã_lọc.xlsx')
    load_list_company()
    update_list_company()
    data=pd.read_excel(save_list)
    return data



def report_finance_vnd(symbol,types,year_f,timely): #Lấy báo cáo tài chính từ vndirect
    symbol, types, timely=symbol.upper(), types.upper(), timely.upper()
    data=report_f_vnd(symbol,types,year_f,timely)
    return data


    
def report_finance_cf(symbol,report,year,timely): ### HAM LAY BAO CAO TAI CHINH TU TRANG CAFEF 4
    symbol=symbol.upper()
    report=report.upper()
    year=int(year)
    timely= timely.upper()
    if report =="CDKT" or report =='BS' or report =='BALANCESHEET':
        x='BSheet'
        if timely=='YEAR':
            y='0'
        elif timely=='QUY' or timely=='QUARTER':
            y='4'
    elif report=='KQKD' or report =='P&L':
        x='IncSta'
        if timely=='YEAR':
            y='0'
        elif timely=='QUY' or timely=='QUARTER':
            y='4'
    elif report=="CFD":
        x='CashFlowDirect'
        if timely=='YEAR':
            y='0'
        elif timely=='QUY' or timely=='QUARTER':
            y='4'
    elif report=="CF":
        x='CashFlow'
        if timely=='YEAR':
            y='0'
        elif timely=='QUY' or timely=='QUARTER':
            y='4'
    repl=pd.read_html('https://s.cafef.vn/BaoCaoTaiChinh.aspx?symbol={}&type={}&year={}&quarter={}'.format(symbol,x,year,y))
    lst=repl[-2].values.tolist()
    df=pd.DataFrame(repl[-1])
    df.columns=list(lst[0])
    df.drop('Tăng trưởng',axis=1,inplace=True)
    return df


        
###HAM GET DATA VIETSTOCK 
def token():
    urltoken='https://finance.vietstock.vn/du-lieu-vi-mo/53-64/ty-gia-lai-xuat.htm#'
    head={'User-Agent':random_user()}
    loadlan1=requests.get(urltoken,headers=head)
    soup=BeautifulSoup(loadlan1.content,'html.parser')
    stoken=soup.body.input
    stoken=str(stoken)
    listtoken=stoken.split()
    xre=[]
    for i in listtoken[1:]:
        i=i.replace('=',':')
        i=i.replace('"','')
        xre.append(i)
    token=str(xre[2])
    token=token.replace('value:','')
    token=token.replace('/>','')
    dic=dict(loadlan1.cookies.get_dict())
    revtoken=dic['__RequestVerificationToken']
    revasp=dic['ASP.NET_SessionId']
    return revasp, revtoken, token

global asp,rtoken,tken,header

asp,rtoken,tken=token()

header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}


def getCPI_vietstock(fromdate,todate): ###HAM GET CPI 10
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,'from':fromdate.month,'to':todate.month,'normTypeID':'52','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.reset_index(inplace=True)
    df_bang.columns.name=None
    return df_bang

def solieu_sanxuat_congnghiep(fromdate,todate): #HAMSOLIEUSANXUAT 11
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'46','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID','FromSource'], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.reset_index(inplace=True)
    df_bang.columns.name=None
    return df_bang

def solieu_banle_vietstock(fromdate,todate):###HAMSOLIEUBANLE 12 
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'47','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.reset_index(inplace=True)
    df_bang.columns.name=None
    return df_bang

def solieu_XNK_vietstock(fromdate,todate):###HAMSOLIEUXNK 13
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'48','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.reset_index(inplace=True)
    df_bang.columns.name=None
    return df_bang

def solieu_FDI_vietstock(fromdate,todate):###HAMSOLIEUVONFDI 14
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'50','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.reset_index(inplace=True)
    df_bang.columns.name=None
    return df_bang

def tygia_vietstock(fromdate,todate):###HAMGETTYGIAVIETSTOCK 15
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'1','fromYear':fromdate.year,'toYear':todate.year,'from':tungay,'to':denngay,'normTypeID':'53','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.index = pd.to_datetime(df_bang.index, dayfirst=True)
    df_bang.sort_index(ascending=False, inplace=True)
    df_bang.columns.name=None
    columns_to_convert = df_bang.columns.to_list()
    for column in columns_to_convert:
        if column in df_bang.columns:
            df_bang[column] = pd.to_numeric(df_bang[column], errors='coerce')
    return df_bang

def solieu_tindung_vietstock(fromdate,todate):###HAMGETDATATINDUNG 16
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'51','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.reset_index(inplace=True)
    df_bang.columns.name=None
    return df_bang

def laisuat_vietstock(fromdate,todate):###HAMGETLAISUAT 17
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'1','fromYear':fromdate.year,'toYear':todate.year,'from':tungay,'to':denngay,'normTypeID':'66','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])[['NormName','UnitCode','FromSource','NormValue','ReportTime']]
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.index = pd.to_datetime(df_bang.index, dayfirst=True)
    df_bang.sort_index(ascending=False, inplace=True)
    columns_to_convert = df_bang.columns.to_list()
    for column in columns_to_convert:
        if column in df_bang.columns:
            df_bang[column] = pd.to_numeric(df_bang[column], errors='coerce')/100
    df_bang.columns.name=None
    return df_bang

def solieu_danso_vietstock(fromdate,todate):###HAMGETSOLIEUDANSO 18
    fromdate=pd.to_datetime(fromdate, dayfirst=True)
    todate=pd.to_datetime(todate, dayfirst=True)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'4','fromYear':fromdate.year,'toYear':todate.year,'from':tungay,'to':denngay,'normTypeID':'55','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName',values='NormValue')
    df_bang.reset_index(inplace=True)
    df_bang.columns.name=None
    return df_bang

def solieu_GDP_vietstock(fromyear,fromQ,toyear,toQ):###HAMGETGDP 19
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    payload={'type':'3','fromYear':fromyear,'toYear':toyear,'from':fromQ,'to':toQ,'normTypeID':'43','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    return bangls