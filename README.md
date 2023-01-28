# RStockvn
Financial statements of companies on the Vietnamese stock exchange


# Introduce
Hi, my name is Nguyen Phuc Binh.
The reason that I do RStockvn is to support the collection of basic data for analysis.

The financial statements that RStockvn collects mainly come from websites: 'https://www.cophieu68.vn', 'https://cafef.vn'.

For the exchange rate, RStockvn collects at "exchangerate.host" if you have more interest or support for their project you can visit at:"https://exchangerate.host/#/donate "
Currently, RStockvn has not yet supported the retrieval of information such as interest rates, CPI, GDP and GNP.

Also you can refer to the library:'vnstock', written by Mr. Thinh Vu
# User guide
First you need to import the library by: import RStockvn as rpv or from RStockvn import *

## a.Function to view stock adjusted price history
This function will return the adjusted price history of the ticker, from dividend events.
``
event_price_cp68(symbol)
``
```
event_price_cp68('HSG')
```
## b.Function retrieves financial statements of stock tickers from websites: 'Cophieu68.vn'
To use this function you need to do the following:
``report_finance_cp68(symbol,reporty,timely)``

Here `symbol` is stock ticker, reporty corresponds to the following options: ``'CDKT' - BalanceSheet``,``'KQKD' - Business results``.And `timely` corresponds to the choice: `'Year' - year` or `'quy' - quarter.`
#### Example
```
report_finance_cp68('ACB','cdkt','quy')
```

## c.Function retrieves financial statements of stock tickers from websites: 'Cafef.vn'
``report_finance_cf(symbol,report,year,timely)``
This function is similar to x except with some differences:
'report' will have the following options: `'CDKT' - BalanceSheet`, `'KQKD' - Business results`, `'CFD' - Direct Cash Flows`, `'CF' - Indirect Cash Flows`. `year` corresponds to the reporting datum you want to get. And `timely` corresponds to the choice: `'Year' - year` or `'quy' - quarter.`
#### Example
```
report_finance_cf('nkg','cfd','2022','year')
```

## d.Function used to view company information
``info_company(symbol)``
#### Example
```
info_company('HSG')
```
## e.View insider trading transactions
``trade_internal(symbol)``
#### Example
```
trade_internal('ACB')
```
## f.View exchange rate change history
At the present time when accessing "exchangerate.host" can only get the history of exchange rates within the last 9 months.``exchange_currency(current,cover_current,from_date,to_date)``
#### Example
```
exchange_currency('USD','VND','2022-11-23','2023-01-10')
```
## g.View a quick report on the profit, revenue, ... of a company
For this report I use the financial statements collected from the website 'Cophieu68', because it is similar to the financial statements provided by securities companies such as VNDirect, SSI.``baocaonhanh(mcp,loai,time)``
For this report I use the financial statements collected from the website 'Cophieu68', because it is similar to the financial statements provided by securities companies such as VNDirect, SSI.

Here mcp corresponds to the ticker, 'type' corresponds to the following selection:
``'TM' - Thương mại``
For companies that manufacture, retail, basic materials, consumer goods,...
``'TC' - Finance``
For companies in the financial sector.

Because companies in the financial sector are quite separate in nature.
For example, the banking industry is an industry that uses capital to generate cash flow, so RStock currently does not provide a quick report template for these industries.

About this kind of report I will add later
#### Example
```
baocaonhanh('HSG','TM','QUY')
```
