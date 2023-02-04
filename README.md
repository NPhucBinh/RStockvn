# RStockvn
Financial statements of companies on the Vietnamese stock exchange


# Introduce
Hi, my name is Nguyen Phuc Binh.
The reason that I do RStockvn is to support the collection of basic data for analysis.

The financial statements that RStockvn collects mainly come from websites: [Cổ phiếu 68](https://www.cophieu68.vn), [Cafef](https://cafef.vn).

For the exchange rate, RStockvn collects at "exchangerate.host" if you have more interest or support for their project you can visit at:[Exchangerate](https://exchangerate.host/#/donate )
### From update 1.0.3 onwards, you can used rstockvn to get macro data.
The figures CPI, FDI, GDP, ... are taken from websites: [Vietstock](https://finance.vietstock.vn/du-lieu-vi-mo)

Also you can refer to the library:'vnstock', written by Mr. Thinh Vu
# User guide
First you need to install RStockvn by:
``pip install RStockvn`` or ``conda install RStockvn``
To use you need to: ``import RStockvn as rpv`` or ``from RStockvn import *``

## 1.Function to view stock adjusted price history
This function will return the adjusted price history of the ticker, from dividend events.
``
event_price_cp68(symbol)
``
```
event_price_cp68('HSG')
```
## 2.Function retrieves financial statements of stock tickers from websites: 'Cophieu68.vn'
To use this function you need to do the following:
``report_finance_cp68(symbol,reporty,timely)``

Here `symbol` is stock ticker, reporty corresponds to the following options: ``'CDKT' - BalanceSheet``,``'KQKD' - Business results``.And `timely` corresponds to the choice: `'Year' - year` or `'quy' - quarter.`
#### Example
```
report_finance_cp68('ACB','cdkt','quy')
```

## 3.Function retrieves financial statements of stock tickers from websites: 'Cafef.vn'
``report_finance_cf(symbol,report,year,timely)``
This function is similar to x except with some differences:
'report' will have the following options: `'CDKT' - BalanceSheet`, `'KQKD' - Business results`, `'CFD' - Direct Cash Flows`, `'CF' - Indirect Cash Flows`. `year` corresponds to the reporting datum you want to get. And `timely` corresponds to the choice: `'Year' - year` or `'quy' - quarter.`
#### Example
```
report_finance_cf('nkg','cfd','2022','year')
```

## 4.Function used to view company information
``info_company(symbol)``
#### Example
```
info_company('HSG')
```
## 5.View insider trading transactions
``trade_internal(symbol)``
#### Example
```
trade_internal('ACB')
```
## 6.View exchange rate change history
At the present time when accessing "exchangerate.host" can only get the history of exchange rates within the last 9 months.``exchange_currency(current,cover_current,from_date,to_date)``
#### Example
```
exchange_currency('USD','VND','2022-11-23','2023-01-10')
```
## 7.View a quick report on the profit, revenue, ... of a company
For this report I use the financial statements collected from the website 'Cophieu68', because it is similar to the financial statements provided by securities companies such as VNDirect, SSI.``baocaonhanh(mcp,loai,time)``
For this report I use the financial statements collected from the website 'Cophieu68', because it is similar to the financial statements provided by securities companies such as VNDirect, SSI.

Here mcp corresponds to the ticker, 'type' corresponds to the following selection:
``'TM' - Thương mại``
For companies that manufacture, retail, basic materials, consumer goods,...
``'TC' - Finance``
For companies in the financial sector.

Because companies in the financial sector are quite separate in nature.
For example, the banking industry is an industry that uses capital to generate cash flow, so RStockvn currently does not provide a quick report template for these industriedsđ

About this kind of report I will add later
#### Example
```
baocaonhanh('HSG','TM','QUY')
```

## 8.Get historical interest rate data (Vietnam)
To get the interest rate data you need to use the function ``laisuat_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
laisuat_vietstock('2022-10-12','2023-02-01')
```
## 9.Get data for CPI (Vietnam)
To get data for CPI you need to use the function ``getCPI_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
getCPI_vietstock('2022-10-01','2023-02-01')
```

## 10.Get data on industrial production (Vietnam)
To get data on industrial production you need to use the function ``solieu_sanxuat_congnghiep(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
solieu_sanxuat_congnghiep('2022-10-01','2023-02-01')
```
## 11.Get data on retail (Vietnam)
To get data on retail you need to use the function ``solieu_banle_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
solieu_banle_vietstock('2022-10-01','2023-02-01')
```

## 12.Get data on import and export (Vietnam)
To get data on import and export you need to use the function ``solieu_XNK_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
solieu_XNK_vietstock('2022-10-01','2023-02-01')
```

## 13.Get data on FDI capital (Vietnam)
To get data on FDI capital you need to use the function ``solieu_FDI_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
solieu_FDI_vietstock('2022-10-01','2023-02-01')
```

## 14.Get data on the exchange rate of USD/VND
To get data on the exchange rate of USD/VND you need to use the function ``tygia_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
tygia_vietstock('2022-10-01','2023-02-01')
```

## 15.Get data on credit in Vietnam
To get data on credit in Vietnam you need to use the function ``solieu_tindung_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
solieu_tindung_vietstock('2022-10-01','2023-02-01')
```

## 16.Get data on population, unemployment rate (Vietnam)
To get data on population, unemployment rate you need to use the function ``solieu_danso_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
solieu_danso_vietstock('2022-10-01','2023-02-01')
```

## 17.Get GDP index (Vietnam)
To get the GDP index you need to use the ``solieu_GDP_vietstock(fromyear,fromQ,toyear,toQ)`` function. ``fromyear`` ``toyear`` are the year milestones to be taken, ``fromQ``, ``toQ`` is the quarters you choose.
#### Example
You want to get the GDP index from 2nd quarter 2020 to 3rd quarter 2022.
```
solieu_GDP_vietstock('2020','2','2022','3')
```

## 18.Get VNINDEX price historical data
To get VNINDEX price historical data, you need to use the function ``get_data_vnidex(number_page)``, ``number_page`` is the number of pages you need to load, each page will return VNINDEX's latest 20-day transaction data.
When using the get_data_vnindex() function, if you get an error [IndexError](https://github.com/NPhucBinh/RStockvn/blob/main/RStockvn/img/IndexError_list_index_out_of_range.PNG), don't worry. You just need to restart the get_data_vnindex() function again, the cause of this error is that the "User-Agent" on initial launch failed to get the cookies of the websites.
The return data of this function is taken from websites [Cafef](https://cafef.vn).

#### Example
For example, if you want to get the historical price of VNINDEX in the last 40 trading days, then ``number_page`` is ``2``, 60 days, ``number_page`` is ``3``.
```
get_data_vnidex(2)
```

## Explore more:``historical_price_cp68(day,symbol)``
The function looks at the price history of a stock code with the corresponding time of ``100``,``200``,``300``,``400``,``500`` and ``ALL``

#### Example
```
historical_price_cp68(100,'HSG')
```
# Epilogue
If you like the idea or want to add more suggestions about RStockvn. 
Please send your comments to email: nguyenphucbinh67@gmail.com, thank you for testing RStockvn
