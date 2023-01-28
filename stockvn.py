import pandas as pd
import requests
import json

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

def report_finance_cp68(symbol,reporty,timely): ### HÀM LẤY BÁO CÁO TÀI CHÍNH TỪ COPHIEU68.VN
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
        col=[0,5,4,3,2,1]
        return data[data.columns[col]]
    elif reporty =="KQKD":
        if timely =="YEAR":
            x= "year=-1"
        elif timely=="QUY":
            x=""
        df=pd.read_html("https://www.cophieu68.vn/financial_income.php?id={}&{}&view=ist".format(symbol,x),header=0)
        data=df[1]
        col=[0,5,4,3,2,1]
        return data[data.columns[col]]

def report_finance_cf(symbol,report,year,typer): ### HAM LAY BAO CAO TAI CHINH TU TRANG CAFEF###
    symbol=symbol.upper()
    report=report.upper()
    year=str(year)
    typer= typer.upper()
    if report =="CDKT":
        x='BSheet'
        if typer=='YEAR':
            y='0'
        elif typer=='QUY':
            y='4'
    elif report=='KQKD':
        x='IncSta'
        if typer=='YEAR':
            y='0'
        elif typer=='QUY':
            y='4'
    elif report=="LCTT":
        x='CashFlowDirect'
        if typer=='YEAR':
            y='0'
        elif typer=='QUY':
            y='4'
    elif report=="LCTTGT":
        x='CashFlow'
        if typer=='YEAR':
            y='0'
        elif typer=='QUY':
            y='4'
    repl=pd.read_html('https://s.cafef.vn/BaoCaoTaiChinh.aspx?symbol={}&type={}&year={}&quarter={}'.format(symbol,x,year,y))
    lst=repl[2].values.tolist()
    df=pd.DataFrame(repl[3])
    df.columns=list(lst[0])
    df.drop('Tăng trưởng',axis=1,inplace=True)
    return df

def INFO_company(symbol): ### HAM XEM THONG TIN CO BAN
    url_cp68='https://www.cophieu68.vn/profilesymbol.php?id={}'.format(symbol)
    re=pd.read_html(url_cp68)
    a=re[1].values.tolist()
    h=pd.concat([re[1],re[2]])
    h.columns=(list(a[0]))
    h=h.drop(0)
    return h

def Trade_internal(symbol):### HAM GIAO DICH MUA BAN NOI BO
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
        a.columns=['{}$/${}'.format(current,cover_current)]
        d=a.sort_index(ascending=False)
    return d

def baocaonhanh(mcp,loai,time):### Báo Cáo Nhanh
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
        
