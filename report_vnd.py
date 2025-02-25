# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.10"
__author__ ="Nguyen Phuc Binh"
__copyright__ = "Copyright 2023, Nguyen Phuc Binh"
__license__ = "MIT"
__email__ = "nguyenphucbinh67@gmail.com"
__website__ = "https://github.com/NPhucBinh"

import pandas as pd
import requests
import json
from datetime import datetime, timedelta
from .user_agent import random_user


users=random_user()

global header

header={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "DNT":"1",
        "Host":"api-finfo.vndirect.com.vn",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"none",
        "Sec-Fetch-User":"?1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":f"{users}",
       }

global payload
payload={}


def report_f_vnd(symbol,types,year_f,timely):
    symbol, types, timely=symbol.upper(), types.upper(), timely.upper()
    year_f=int(year_f)
    if types == 'BS' or types == 'BALANCESHEET' or types == 'CDKT':
        modelType='1,89,101,411'
    elif types == 'P&L' or types == 'KQKD':
        modelType='2,90,102,412'
    elif types == 'CF' or types == 'LCTT':
        modelType='3,91,103,413'
        
    if timely=='YEAR' or timely=='NAM':
        url_y=f'https://api-finfo.vndirect.com.vn/v4/financial_statements?q=code:{symbol}~reportType:ANNUAL~modelType:{modelType}~fiscalDate:{year_f}-12-31,{year_f-1}-12-31,{year_f-2}-12-31,{year_f-3}-12-31,{year_f-4}-12-31,{year_f-5}-12-31,{year_f-6}-12-31,{year_f-7}-12-31&sort=fiscalDate&size=2000'        
    elif timely=='QUARTER' or timely=='QUY':
        url_y=f'https://api-finfo.vndirect.com.vn/v4/financial_statements?q=code:{symbol}~reportType:QUARTER~modelType:{modelType}~fiscalDate:{year_f}-12-31,{year_f}-09-30,{year_f}-06-30,{year_f}-03-31,{year_f-1}-12-31,{year_f-1}-09-30,{year_f-1}-06-30,{year_f-1}-03-31&sort=fiscalDate&size=2000'       
    
    url_ct=f'https://api-finfo.vndirect.com.vn/v4/financial_models?sort=displayOrder:asc&q=codeList:{symbol}~modelType:{modelType}~note:TT199/2014/TT-BTC,TT334/2016/TT-BTC,TT49/2014/TT-NHNN,TT202/2014/TT-BTC~displayLevel:0,1,2,3&size=999'
    r=requests.request("GET", url_y, headers=header, data=payload)
    df=pd.DataFrame(r.json()['data'])
    pivot_df = df.pivot(index='itemCode', columns='fiscalDate', values='numericValue')
    pivot_df.reset_index(inplace=True)
    pivot_df.columns.name=None
    r2=requests.get(url_ct,headers=header, data=payload)
    df_ct=pd.DataFrame(r2.json()['data'])
    data1=df_ct[['itemVnName','itemCode']].copy()
    data=pd.merge(data1, pivot_df, left_on='itemCode', right_on='itemCode', how='left')
    data.drop('itemCode',axis=1,inplace=True)
    data=data.rename(columns={'itemVnName':symbol.upper()})
    return data

def info_cp(symbol):
    url=f"https://api-finfo.vndirect.com.vn/v4/ratios/latest?filter=ratioCode:MARKETCAP,NMVOLUME_AVG_CR_10D,PRICE_HIGHEST_CR_52W,PRICE_LOWEST_CR_52W,OUTSTANDING_SHARES,FREEFLOAT,BETA,PRICE_TO_EARNINGS,PRICE_TO_BOOK,DIVIDEND_YIELD,BVPS_CR,&where=code:{symbol.upper()}~reportDate:gt:2024-05-09&order=reportDate&fields=ratioCode,value"
    r=requests.get(url,headers=header,data=payload)
    df=pd.DataFrame(r.json()['data'])
    new_order = ['ratioCode', 'value']
    df = df.reindex(columns=new_order)
    return df