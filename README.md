# Package is used to retrieve information related to securities finance.

# Notice: During the update process, some functions have been removed and changed.

# [RStockvn](https://pypi.org/project/RStockvn/)
Financial statements of companies on the Vietnamese stock exchange


# Introduce
Hi, my name is Nguyen Phuc Binh.
The reason that I do [RStockvn](https://pypi.org/project/RStockvn/) is to support the collection of basic data for analysis.

The financial statements that RStockvn collects mainly come from websites: [Cafef](https://cafef.vn).

For the exchange rate, RStockvn collects at ["exchangerate.host"](https://exchangerate.host/#/donate) if you have more interest or support for their project you can visit at:[Exchangerate](https://exchangerate.host/#/donate)
### From update 1.0.3 onwards, you can used rstockvn to get macro data.
The figures CPI, FDI, GDP, ... are taken from websites: [Vietstock](https://finance.vietstock.vn/du-lieu-vi-mo)

If you are on the old version and have errors, please update to the new version of RStockvn by: ``pip install --upgrade RStockvn``

Also you can refer to the library:'vnstock', written by Mr. Thinh Vu

## Thông báo hiện các hàm lấy dữ liệu từ Cophieu68 đã bị xóa khỏi [RStockvn](https://pypi.org/project/RStockvn/) do không còn hoạt động được. Thời gian tới sẽ được cập nhật sau.

# User guide
First you need to install RStockvn by:
``pip install RStockvn`` or ``conda install RStockvn``
To use you need to: ``import RStockvn as rpv`` or ``from RStockvn import *``

## 1. The function gets the list of listed companies

``rpv.list_company()``

Or you want to update list_company

``rpv.update_company()``


## 2. Function to get financial statements from 'vndirect':
`symbol` is the `stock symbol`
`report` is the type of report that needs to get `'BS' or 'BALANCESHEET' or 'CDKT - BalanceSheet`, `'P&L' or 'Business results' - Business results`, ''CF' - Cash Flows'
`year` is the financial year to get
`timely` is the time you want to get by year or quarter

rpv.report_finance_vnd(symbol,report,year,timely)

#### Example
``rpv.report_finance_vnd('vnd','bs','2023','quarter')``

## 3.Function retrieves financial statements of stock tickers from websites: 'Cafef.vn'

``report_finance_cf(symbol,report,year,timely)``
This function is similar to x except with some differences:
'report' will have the following options: `'CDKT' - BalanceSheet`, `'KQKD' - Business results`, `'CFD' - Direct Cash Flows`, `'CF' - Indirect Cash Flows`. `year` corresponds to the reporting datum you want to get. And `timely` corresponds to the choice: `'Year' - year` or `'quy' - quarter.`
#### Example
```
rpv.report_finance_cf('nkg','cfd','2022','year')
```

## 4. Function to retrieve price history of stock codes from vndirect, get_price_historical_vnd(symbol,fromdate,todate):
Where symbol is the stock code symbol, fromdate is the starting date, and todate is the ending time.
#### Example
```
rpv.get_price_historical_vnd('nkg','cfd','2022','year')
```

## 5. Functions to retrieve information about internal shareholder transactions, foreign transactions,...
Since I'm too lazy to explain in detail, I'll list the functions below.
Internal shareholder transactions
```
rpv.get_insider_transaction_history_cafef(symbol,fromdate,todate)
```

Foreign transactions from vndirect
```
rpv.get_foreign_historical_vnd(symbol,fromdate,todate)
```

Foreign transactions
```
rpv.get_foreign_transaction_history_cafef(symbol,fromdate,todate)
```

Proprietary trading of securities companies
```
rpv.get_proprietary_history_cafef(symbol,fromdate,todate)
```

## 6.View exchange rate change history
At the present time when accessing "exchangerate.host" can only get the history of exchange rates within the last 9 months.``exchange_currency(current,cover_current,from_date,to_date)``
#### Example
```
rpv.exchange_currency('USD','VND','2022-11-23','2023-01-10')
```
You can also convert other currencies, such as Japanese Yen and USD
```
rpv.exchange_currency('JPY','USD','2022-11-23','2023-01-10')
```
## 7.View a quick report on the profit, revenue, ... of a company
For this report I use the financial statements collected from the website 'Cophieu68', because it is similar to the financial statements provided by securities companies such as VNDirect, SSI.``baocaonhanh(mcp,loai,time)``

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
rpv.baocaonhanh('HSG','TM','QUY')
```

## 8.Get historical interest rate data (Vietnam)
To get the interest rate data you need to use the function ``laisuat_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.laisuat_vietstock('2022-10-12','2023-02-01')
```
## 9.Get data for CPI (Vietnam)
To get data for CPI you need to use the function ``getCPI_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.getCPI_vietstock('2022-10-01','2023-02-01')
```

## 10.Get data on industrial production (Vietnam)
To get data on industrial production you need to use the function ``solieu_sanxuat_congnghiep(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.solieu_sanxuat_congnghiep('2022-10-01','2023-02-01')
```
## 11.Get data on retail (Vietnam)
To get data on retail you need to use the function ``solieu_banle_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.solieu_banle_vietstock('2022-10-01','2023-02-01')
```

## 12.Get data on import and export (Vietnam)
To get data on import and export you need to use the function ``solieu_XNK_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.solieu_XNK_vietstock('2022-10-01','2023-02-01')
```

## 13.Get data on FDI capital (Vietnam)
To get data on FDI capital you need to use the function ``solieu_FDI_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.solieu_FDI_vietstock('2022-10-01','2023-02-01')
```

## 14.Get data on the exchange rate of USD/VND
To get data on the exchange rate of USD/VND you need to use the function ``tygia_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.tygia_vietstock('2022-10-01','2023-02-01')
```

## 15.Get data on credit in Vietnam
To get data on credit in Vietnam you need to use the function ``solieu_tindung_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.solieu_tindung_vietstock('2022-10-01','2023-02-01')
```

## 16.Get data on population, unemployment rate (Vietnam)
To get data on population, unemployment rate you need to use the function ``solieu_danso_vietstock(fromdate,todate)``, ``fromdate`` is from the date you need to get the ``todate`` to the date you want to get the data.
#### Example
```
rpv.solieu_danso_vietstock('2022-10-01','2023-02-01')
```

## 17.Get GDP index (Vietnam)
To get the GDP index you need to use the ``solieu_GDP_vietstock(fromyear,fromQ,toyear,toQ)`` function. ``fromyear`` ``toyear`` are the year milestones to be taken, ``fromQ``, ``toQ`` is the quarters you choose.
#### Example
You want to get the GDP index from 2nd quarter 2020 to 3rd quarter 2022.
```
rpv.solieu_GDP_vietstock('2020','2','2022','3')
```

## 18.Get price historical data of CafeF
To get historical stock price data from [CafeF](https://cafef.vn) websites you need to use the function ``get_data_history_cafef(symbol,fromdate,todate)``. ``symbol`` is the stock symbol you need to get data from, ``fromdate`` is the start date and ``todate`` is the end date.

#### Example
For example, you want to get the price history of VNINDEX from January 20, 2022 to February 20, 2023
```
rpv.get_price_history_cafef('VNINDEX','20/01/2022','20/02/2023')
```
OR you want to get the price history of symbol stock ``SSI`` from January 20, 2022 to February 20, 2023
```
rpv.get_price_history_cafef('SSI','20/01/2022','20/02/2023')
```

# Epilogue
If you like the idea or want to add more suggestions about RStockvn. 
Please send your comments to email: nguyenphucbinh67@gmail.com, thank you for testing RStockvn
