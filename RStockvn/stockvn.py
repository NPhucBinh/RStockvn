# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.5"
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
#from . import user_agent
from . import data_cafef as cafef
#import data_cafef as cafef
import datetime as dt

def event_price_cp68(symbol):### HAM XEM LICH SU DIEU CHINH GIA CP
    df=pd.read_html('https://www.cophieu68.vn/event_calc.php?id={}'.format(symbol))
    df=df[1]
    return df

def historical_price_cp68(day,symbol):### HAM XEM LICH SU GIA CP
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

def report_finance_cp68(symbol,reporty,timely): ### H??M L???Y B??O C??O T??I CH??NH T??? COPHIEU68.VN
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

def report_finance_cf(symbol,report,year,timely): ### HAM LAY BAO CAO TAI CHINH TU TRANG CAFEF###
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
    df.drop('T??ng tr?????ng',axis=1,inplace=True)
    return df

def info_company(symbol): ### HAM XEM THONG TIN CO BAN
    url_cp68='https://www.cophieu68.vn/profilesymbol.php?id={}'.format(symbol)
    re=pd.read_html(url_cp68)
    a=re[1].values.tolist()
    h=pd.concat([re[1],re[2]])
    h.columns=(list(a[0]))
    h=h.drop(0)
    return h

def trade_internal(symbol):### HAM GIAO DICH MUA BAN NOI BO
    url='https://www.cophieu68.vn/internal_trade.php?id={}'.format(symbol)
    df=pd.read_html(url)
    a=df[1].iloc[:1].values.tolist()
    df[1].columns=list(a[0])
    df[1].drop(0)
    return df[1]

def exchange_currency(current,cover_current,from_date,to_date): ###HAM LAY TY GIA
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

def baocaonhanh(mcp,loai,time):### B??o C??o Nhanh
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
        df1=df1.set_index('Ch??? ti??u C??n ?????i k??? to??n',drop=True,append=False, inplace=False, verify_integrity=False)
        df1=df1.drop_duplicates()
        df2=df2.set_index('Ch??? ti??u K???t qu??? kinh doanh',drop=True,append=False,inplace=False,verify_integrity=False)
        data=df1.T
        bcf=df2.T
        tltsld=round(data['T??I S???N NG???N H???N']/data['T???NG C???NG T??I S???N'],2)*100
        DA=round(data['N??? PH???I TR???']/data['T???NG C???NG T??I S???N'],2)*100
        DE=round(data['N??? PH???I TR???']/data['V???N CH??? S??? H???U'],2)*100
        tstkn=round((data['T??I S???N NG???N H???N']-data['H??ng t???n kho'])/data['N??? ng???n h???n'])*100
        tllntdt=round(bcf['L???i nhu???n thu???n t??? ho???t ?????ng kinh doanh']/bcf['Doanh thu thu???n v??? b??n h??ng v?? cung c???p d???ch v???'],2)*100
        tsLNSTtDT=round(bcf['L???i nhu???n sau thu??? thu nh???p doanh nghi???p']/bcf['Doanh thu thu???n v??? b??n h??ng v?? cung c???p d???ch v???'],2)*100
        dt4=bcf['Doanh thu thu???n v??? b??n h??ng v?? cung c???p d???ch v???'][1:]
        tka=data['H??ng t???n kho'][:4]
        tkb=data['H??ng t???n kho'][1:]
        vqhtk=round(dt4/((tka.values+tkb.values)/2),2)
        pta=data['C??c kho???n ph???i thu ng???n h???n'][:4]
        ptb=data['C??c kho???n ph???i thu ng???n h???n'][1:]
        vqkpt=round(dt4/((pta.values+ptb.values)/2),2)
        sdtk=round((x/vqhtk))
        sdpt=round((x/vqkpt))
        ttdt=round(bcf['Doanh thu thu???n v??? b??n h??ng v?? cung c???p d???ch v???'].pct_change(),3)*100
        ttln=round(bcf['L???i nhu???n thu???n t??? ho???t ?????ng kinh doanh'].pct_change(),4)*100
        lis=[ttdt,ttln,tltsld,DA,DE,tstkn,tllntdt,tsLNSTtDT,vqhtk,sdtk,vqkpt,sdpt]
        lis2=['t??ng tr?????ng DT thu???n t??? H??KD %','t??ng tr?????ng LN thu???n t??? H??KD %',
              'Tl TSL?? tr??n TTS %','Tl N??? Ph???i Tr??? tr??n TTS DA %', 'Tl N??? Ph???i Tr??? tr??n VCSH DE %','Ts T.kho???n Nhanh',
              'LN thu???n tr??n DT thu???n %','ts LNST tr??n DT thu???n %','V??ng quay H??ng t???n kho','S??? ng??y t???n kho',
              'V??ng quay Kho???n ph???i thu','K??? thu ti???n B??nh qu??n']
        r=[]
        for i in lis:
            n=pd.DataFrame(i)
            r.append(n)
            tu=pd.concat(r,axis=1)
        tu.columns=lis2
        te=tu.T
        te.columns.names=['B??o c??o nhanh m?? c??? phi???u {}'.format(mcp)]
        return te
    elif loai == 'TC':
        print('Hi???n ch??a c?? m???u b??o c??o nhanh cho c??c Ng??nh T??i Ch??nh, s??? b??? sung sau.')
        
###HAM GET DATA VIETSTOCK

def getCPI_vietstock(fromdate,todate): ###HAM GET CPI
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

def solieu_sanxuat_congnghiep(fromdate,todate): #HAMSOLIEUSANXUAT
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

def solieu_banle_vietstock(fromdate,todate):###HAMSOLIEUBANLE
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

def solieu_XNK_vietstock(fromdate,todate):###HAMSOLIEUXNK
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

def solieu_FDI_vietstock(fromdate,todate):###HAMSOLIEUVONFDI
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'50','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    return bangls

def tygia_vietstock(fromdate,todate):###HAMGETTYGIAVIETSTOCK
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

def solieu_tindung_vietstock(fromdate,todate):###HAMGETDATATINDUNG
    asp,rtoken,tken=token()
    fromdate=pd.to_datetime(fromdate)
    todate=pd.to_datetime(todate)
    tungay=str(fromdate.strftime('%Y-%m-%d'))
    denngay=str(todate.strftime('%Y-%m-%d'))
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'2','fromYear':fromdate.year,'toYear':todate.year,
             'from':fromdate.month,'to':todate.month,'normTypeID':'51','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID',], axis=1, inplace=True)
    return bangls

def laisuat_vietstock(fromdate,todate):###HAMGETLAISUAT
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
    return bangls

def solieu_danso_vietstock(fromdate,todate):###HAMGETSOLIEUDANSO
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
def solieu_GDP_vietstock(fromyear,fromQ,toyear,toQ):###HAMGETGDP
    asp,rtoken,tken=token()
    url='https://finance.vietstock.vn/data/reportdatatopbynormtype'
    header={'User-Agent':random_user(),'Cookie': 'language=vi-VN; ASP.NET_SessionId={}; __RequestVerificationToken={}; Theme=Light; _ga=GA1.2.521754408.1675222361; _gid=GA1.2.2063415792.1675222361; AnonymousNotification='.format(asp,rtoken)}
    payload={'type':'3','fromYear':fromyear,'toYear':toyear,'from':fromQ,'to':toQ,'normTypeID':'43','__RequestVerificationToken': '{}'.format(tken)}
    ls=requests.post(url,headers=header,data=payload)
    cov1=dict(ls.json())
    bangls=pd.DataFrame(cov1['data'])
    bangls.drop(['ReportDataID','TermID','TermYear','TernDay','NormID','GroupName','CssStyle','NormTypeID','NormGroupID'], axis=1, inplace=True)
    return bangls

def get_data_history_cafef(symbol,fromdate,todate):
    data=cafef.get_data_history_cafef(symbol,fromdate,todate)
    return data
