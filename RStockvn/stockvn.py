# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.6"
__author__ ="Nguyen Phuc Binh"
__copyright__ = "Copyright 2023, Nguyen Phuc Binh"
__license__ = "MIT"
__email__ = "nguyenphucbinh67@gmail.com"
__website__ = "https://github.com/NPhucBinh"

import pandas as pd
import requests
import requests
import json
from bs4 import BeautifulSoup
from .user_agent import random_user
from .cafef_test import browser_get_data
import datetime as dt

def event_price_cp68(symbol):### HAM XEM LICH SU DIEU CHINH GIA CP 1
    df=pd.read_html('https://www.cophieu68.vn/event_calc.php?id={}'.format(symbol))
    df=df[1]
    return df

def historical_price_cp68(day,symbol):### HAM XEM LICH SU GIA CP 2
    data=[]
    if day==100:
        i=1
        df=pd.read_html('https://www.cophieu68.vn/historyprice.php?currentPage={}&id={}'.format(i,symbol))
        df3=pd.DataFrame(data=df[1])
    elif day==200:
        for i in list(range(1,3)):
            df=pd.read_html('https://www.cophieu68.vn/historyprice.php?currentPage={}&id={}'.format(i,symbol))
            df1=pd.DataFrame(data=df[1])
            data.append(df1)
            df3= pd.concat(data, ignore_index=True)
    elif day==300:
        for i in list(range(1,4)):
            df=pd.read_html('https://www.cophieu68.vn/historyprice.php?currentPage={}&id={}'.format(i,symbol),header=0)
            df1=pd.DataFrame(data=df[1])
            data.append(df1)
            df3= pd.concat(data, ignore_index=True)
    elif day==400:
        for i in list(range(1,5)):
            df=pd.read_html('https://www.cophieu68.vn/historyprice.php?currentPage={}&id={}'.format(i,symbol),header=0)
            df1=pd.DataFrame(data=df[1])
            data.append(df1)
            df3= pd.concat(data, ignore_index=True)
    elif day==500:
        for i in list(range(1,6)):
            df=pd.read_html('https://www.cophieu68.vn/historyprice.php?currentPage={}&id={}'.format(i,symbol),header=0)
            df1=pd.DataFrame(data=df[1])
            data.append(df1)
            df3= pd.concat(data, ignore_index=True)
    elif day=='ALL':
        for i in list(range(1,100)):
            df=pd.read_html('https://www.cophieu68.vn/historyprice.php?currentPage={}&id={}'.format(i,symbol),header=0)
            df1=pd.DataFrame(data=df[1])
            data.append(df1)
            df3= pd.concat(data, ignore_index=True)
    return df3

def report_finance_cp68(symbol,reporty,timely): ### HÀM LẤY BÁO CÁO TÀI CHÍNH TỪ COPHIEU68.VN 3
    symbol=str(symbol.upper())
    timely=str(timely.upper())
    reporty=str(reporty.upper())
    x=[]
    if reporty =="CDKT":
        if timely=="YEAR":
            x="year=-1"
        elif timely=="QUY":
            x=""
        df =pd.read_html('https://www.cophieu68.vn/financial_balance.php?id={}&{}&view=bs'.format(symbol,x),header=0)
        data=df[1]
        cols=data.columns.tolist()
        e=cols[1:]
        e.reverse()
        ls=[]
        ls.append(cols[0])
        ls.extend(e)
        return data[ls]
    elif reporty =="KQKD":
        if timely =="YEAR":
            x= "year=-1"
        elif timely=="QUY":
            x=""
        df=pd.read_html("https://www.cophieu68.vn/financial_income.php?id={}&{}&view=ist".format(symbol,x),header=0)
        data=df[1]
        cols=data.columns.tolist()
        e=cols[1:]
        e.reverse()
        ls=[]
        ls.append(cols[0])
        ls.extend(e)
        return data[ls]

def report_finance_cf(symbol,report,year,timely): ### HAM LAY BAO CAO TAI CHINH TU TRANG CAFEF 4
    symbol=symbol.upper()
    report=report.upper()
    year=int(year)
    timely= timely.upper()
    if report =="CDKT":
        x='BSheet'
        if timely=='YEAR':
            y='0'
        elif timely=='QUY':
            y='4'
    elif report=='KQKD':
        x='IncSta'
        if timely=='YEAR':
            y='0'
        elif timely=='QUY':
            y='4'
    elif report=="CFD":
        x='CashFlowDirect'
        if timely=='YEAR':
            y='0'
        elif timely=='QUY':
            y='4'
    elif report=="CF":
        x='CashFlow'
        if timely=='YEAR':
            y='0'
        elif timely=='QUY':
            y='4'
    repl=pd.read_html('https://s.cafef.vn/BaoCaoTaiChinh.aspx?symbol={}&type={}&year={}&quarter={}'.format(symbol,x,year,y))
    lst=repl[2].values.tolist()
    df=pd.DataFrame(repl[3])
    df.columns=list(lst[0])
    df.drop('Tăng trưởng',axis=1,inplace=True)
    return df

def info_company(symbol): ### HAM XEM THONG TIN CO BAN 5
    url_cp68='https://www.cophieu68.vn/profilesymbol.php?id={}'.format(symbol)
    re=pd.read_html(url_cp68)
    a=re[1].values.tolist()
    h=pd.concat([re[1],re[2]])
    h.columns=(list(a[0]))
    h=h.drop(0)
    return h

def trade_internal(symbol):### HAM GIAO DICH MUA BAN NOI BO 6
    url='https://www.cophieu68.vn/internal_trade.php?id={}'.format(symbol)
    df=pd.read_html(url)
    a=df[1].iloc[:1].values.tolist()
    df[1].columns=list(a[0])
    df[1].drop(0)
    return df[1]

def exchange_currency(current,cover_current,from_date,to_date): ###HAM LAY TY GIA 7
    url = 'https://api.exchangerate.host/timeseries?'
    payload={'base':current,"start_date":from_date,'end_date':to_date}
    response = requests.get(url, params=payload)
    data = response.json()
    dic={}
    lid=[]
    for item in data['rates']:
        de=item
        daa=data['rates'][item][cover_current]
        dic[de]=[daa]
        lid.append(daa)
        a=pd.DataFrame(dic).T
        a=round(a,2)
        a.columns=['{}/{}'.format(current,cover_current)]
        d=a.sort_index(ascending=False)
    return d

def baocaonhanh(mcp,loai,time):### Báo Cáo Nhanh 8
    mcp=mcp.upper()
    loai=loai.upper()
    tim=time.upper()
    if tim =='QUY':
        x=90
    elif tim=='YEAR':
        x=360
    if loai == 'TM':
        df1=report_finance_cp68(mcp,'cdkt',time)
        df2=report_finance_cp68(mcp,'kqkd',time)
        df1=df1.set_index('Chỉ tiêu Cân đối kế toán',drop=True,append=False, inplace=False, verify_integrity=False)
        df1=df1.drop_duplicates()
        df2=df2.set_index('Chỉ tiêu Kết quả kinh doanh',drop=True,append=False,inplace=False,verify_integrity=False)
        data=df1.T
        bcf=df2.T
        tltsld=round(data['TÀI SẢN NGẮN HẠN']/data['TỔNG CỘNG TÀI SẢN'],2)*100
        DA=round(data['NỢ PHẢI TRẢ']/data['TỔNG CỘNG TÀI SẢN'],2)*100
        DE=round(data['NỢ PHẢI TRẢ']/data['VỐN CHỦ SỞ HỮU'],2)*100
        tstkn=round((data['TÀI SẢN NGẮN HẠN']-data['Hàng tồn kho'])/data['Nợ ngắn hạn'])*100
        tllntdt=round(bcf['Lợi nhuận thuần từ hoạt động kinh doanh']/bcf['Doanh thu thuần về bán hàng và cung cấp dịch vụ'],2)*100
        tsLNSTtDT=round(bcf['Lợi nhuận sau thuế thu nhập doanh nghiệp']/bcf['Doanh thu thuần về bán hàng và cung cấp dịch vụ'],2)*100
        dt4=bcf['Doanh thu thuần về bán hàng và cung cấp dịch vụ'][1:]
        tka=data['Hàng tồn kho'][:4]
        tkb=data['Hàng tồn kho'][1:]
        vqhtk=round(dt4/((tka.values+tkb.values)/2),2)
        pta=data['Các khoản phải thu ngắn hạn'][:4]
        ptb=data['Các khoản phải thu ngắn hạn'][1:]
        vqkpt=round(dt4/((pta.values+ptb.values)/2),2)
        sdtk=round((x/vqhtk))
        sdpt=round((x/vqkpt))
        ttdt=round(bcf['Doanh thu thuần về bán hàng và cung cấp dịch vụ'].pct_change(),3)*100
        ttln=round(bcf['Lợi nhuận thuần từ hoạt động kinh doanh'].pct_change(),4)*100
        lis=[ttdt,ttln,tltsld,DA,DE,tstkn,tllntdt,tsLNSTtDT,vqhtk,sdtk,vqkpt,sdpt]
        lis2=['tăng trưởng DT thuần từ HĐKD %','tăng trưởng LN thuần từ HĐKD %',
              'Tl TSLĐ trên TTS %','Tl Nợ Phải Trả trên TTS DA %', 'Tl Nợ Phải Trả trên VCSH DE %','Ts T.khoản Nhanh',
              'LN thuần trên DT thuần %','ts LNST trên DT thuần %','Vòng quay Hàng tồn kho','Số ngày tồn kho',
              'Vòng quay Khoản phải thu','Kỳ thu tiền Bình quân']
        r=[]
        for i in lis:
            n=pd.DataFrame(i)
            r.append(n)
            tu=pd.concat(r,axis=1)
        tu.columns=lis2
        te=tu.T
        te.columns.names=['Báo cáo nhanh mã cổ phiếu {}'.format(mcp)]
        return te
    elif loai == 'TC':
        print('Hiện chưa có mẫu báo cáo nhanh cho các Ngành Tài Chính, sẽ bổ sung sau.')
        
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

def getCPI_vietstock(fromdate,todate): ###HAM GET CPI 10
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,'from':fromdate.month,'to':todate.month,'normTypeID':'52','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    return bangls

def solieu_sanxuat_congnghiep(fromdate,todate): #HAMSOLIEUSANXUAT 11
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
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
    return bangls

def solieu_banle_vietstock(fromdate,todate):###HAMSOLIEUBANLE 12 
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'47','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    return bangls

def solieu_XNK_vietstock(fromdate,todate):###HAMSOLIEUXNK 13
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'48','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    return bangls

def solieu_FDI_vietstock(fromdate,todate):###HAMSOLIEUVONFDI 14
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'50','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    return bangls

def tygia_vietstock(fromdate,todate):###HAMGETTYGIAVIETSTOCK 15
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'1','fromYear':fromdate.year,'toYear':todate.year,'from':tungay,'to':denngay,'normTypeID':'53','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    return bangls

def solieu_tindung_vietstock(fromdate,todate):###HAMGETDATATINDUNG 16
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'51','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    return bangls

def laisuat_vietstock(fromdate,todate):###HAMGETLAISUAT 17
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'1','fromYear':fromdate.year,'toYear':todate.year,'from':tungay,'to':denngay,'normTypeID':'66','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    df_bang=bangls.pivot(index='ReportTime',columns='NormName')
    return df_bang

def solieu_danso_vietstock(fromdate,todate):###HAMGETSOLIEUDANSO 18
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'4','fromYear':fromdate.year,'toYear':todate.year,'from':tungay,'to':denngay,'normTypeID':'55','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    return bangls
def solieu_GDP_vietstock(fromyear,fromQ,toyear,toQ):###HAMGETGDP 19
    asp,rtoken,tken=token()
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'3','fromYear':fromyear,'toYear':toyear,'from':fromQ,'to':toQ,'normTypeID':'43','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    return bangls

def get_data_history_cafef(symbol,fromdate,todate):### 20
    data=browser_get_data(symbol,fromdate,todate).getdata()
    return data
