# [RStockvn](https://pypi.org/project/RStockvn/)
Financial statements of companies on the Vietnamese stock exchange

#Readme instructions are available in 2 languages, English and Vietnamese.
#Readme hướng dẫn có 2 ngôn ngữ, tiếng anh và tiếng việt.

#Language English

# Introduction
Hello,
I would like to introduce the library [RStockvn](https://pypi.org/project/RStockvn/) which is a library that supports the retrieval of financial reports from companies listed on the Vietnam Stock Exchange.

### From version 1.0.3 onwards, RStockvn can retrieve macro information.
RStockvn can now get macro information such as CPI, GDP, interest rates,... updated according to the website: [Vietstock](https://finance.vietstock.vn/du-lieu-vi-mo)

If you are using an old version and encounter an error, please update RStockvn by: ``pip install --upgrade RStockvn`` or uninstall and reinstall ``pip uninstall RStockvn``

## Notice from version 2.5.0 onwards [RStockvn](https://pypi.org/project/RStockvn/) no longer supports getting data from Cafef.

# Instructions
First you need to install the RStockvn library by:
``pip install RStockvn`` or if using Jupyter ``conda install RStockvn``
Step 2 import the library: ``import RStockvn as rpv``

## Function to get data from the list of companies listed on the Vietnam Stock Exchange

``rpv.list_company()``

If you see that the list is old, you can perform the function below to update the new one

``rpv.update_company()``

## Function to get stock information from 'vndirect':

`symbol` is the stock symbol
Function to get stock information including P/E, P/B, number of outstanding shares, ... as follows: get_info_cp(symbol)

#### Example to get stock information VND
```get_info_cp('vnd')```

## Function to get stock price history from 'vndirect':
`symbol` is the stock symbol
`fromdate` is the start date you need to get
`todate` is the end date
Function to get stock price history as follows: ``get_price_historical_vnd(symbol,fromdate,todate)``

#### Example to get vnd ​​price history from 06/20/2024 to 08/08/2024
```rpv.get_price_historical_vnd('vnd','06/20/2024',08/08/2024)```

## Function to get financial reports of companies listed on the Vietnam Stock Exchange from 'vndirect':
`symbol` is the stock symbol
`report` is the type of report you need to get `'BS' or 'BALANCESHEET' or 'CDKT'` - is the balance sheet, `'P&L' or 'Business results'` - is the business results report, `'CF' - 'Cash Flows'` - is the cash flow report
`year` is the financial year you need to get
`timely` is the type of quarterly or annual report

rpv.report_finance_vnd(symbol,report,year,timely)

#### Example of getting VNDIRECT's balance sheet in 2023 by quarter
```rpv.report_finance_vnd('vnd','bs','2023','quarter')```

## Function to get interest rate according to Vietstock
Function to get interest rate as follows:``laisuat_vietstock(fromdate,todate)``, ``fromdate`` is the start date of interest rate to get ``todate`` is the end date end.

#### Example
```
rpv.laisuat_vietstock('2022-10-12','2023-02-01')
```
## Function to get CPI index according to Vietstock
Function to get CPI index as follows:``getCPI_vietstock(fromdate,todate)``, ``fromdate`` is the start date of the interest rate to be taken ``todate`` is the end date.

#### Example
```
rpv.getCPI_vietstock('2022-10-01','2023-02-01')
```

## Function to get Production Index according to Vietstock
The function to get the production index is as follows:``solieu_sanxuat_congnghiep(fromdate,todate)``, ``fromdate`` is the starting date of the interest rate to be taken, ``todate`` is the ending date.

#### Example
```
rpv.solieu_sanxuat_congnghiep('2022-10-01','2023-02-01')
```
## 6Function to get retail sales data according to Vietstock
Function to get retail sales data as follows: ``solieu_banle_vietstock(fromdate,todate)``, ``fromdate`` is the start date of the interest rate to be taken, ``todate`` is the end date.

#### Example
```
rpv.solieu_banle_vietstock('2022-10-01','2023-02-01')
```

## Function to get import-export data according to Vietstock
The function to get import-export data is as follows: ``solieu_XNK_vietstock(fromdate,todate)``, ``fromdate`` is the starting date of the interest rate to be taken, ``todate`` is the ending date.

#### Example
```
rpv.solieu_XNK_vietstock('2022-10-01','2023-02-01')
```

## Function to get FDI data according to Vietstock
Function to get XNK data as follows:``solieu_FDI_vietstock(fromdate,todate)``, ``fromdate`` is the starting date of the interest rate to be taken, ``todate`` is the ending date.

#### Example
```
rpv.solieu_FDI_vietstock('2022-10-01','2023-02-01')
```

## Function to get USD/VND exchange rate data according to Vietstock
Function to get USD/VND exchange rate as follows:``tygia_vietstock(fromdate,todate)``, ``fromdate`` is the starting date of the interest rate to be taken, ``todate`` is the ending date.

#### Example
```
rpv.tygia_vietstock('2022-10-01','2023-02-01')
```

## Function to get credit data according to Vietstock
Function to get credit data as follows:``solieu_tindung_vietstock(fromdate,todate)``, ``fromdate`` is the starting date of the interest rate to be taken ``todate`` is the ending date.

#### Example
```
rpv.solieu_tindung_vietstock('2022-10-01','2023-02-01')
```

## Function to get credit data according to Vietstock
Function to get credit data as follows:``solieu_GDP_vietstock(fromyear,fromQ,toyear,toQ)``, ``fromyear`` ``toyear`` start and end year, ``fromQ``, ``toQ`` start and end quarter.

#### Example
You want the GDP index from Q2 2020 to Q3 2022.
```
rpv.solieu_GDP_vietstock('2020','2','2022','3')
```

# Conclusion
If you find this project useful, you can support us via the QR code below to help maintain and develop the project.

![QR Code for Donations](./RStockvn/data/donate_qr.jpg)

You can contact via email: nguyenphucbinh67@gmail.com

#Language Vietnamese

# Giới thiệu
Chào bạn, 
Xin giới thiệu thư viện [RStockvn](https://pypi.org/project/RStockvn/) là 1 thư viện hỗ trợ thực hiện lấy các báo cáo tài chính từ các công ty được niêm yết trên sàn Chứng khoán Việt Nam.

### Từ phiên bản 1.0.3 trở đi RStockvn có thể lấy các thông tin vĩ mô.
RStockvn hiện có thể lấy các thông tin vĩ mô như CPI,GDP, lãi suất,... được cập nhật theo trang websites: [Vietstock](https://finance.vietstock.vn/du-lieu-vi-mo)

Nếu bạn đang sử dụng phiên bản cũ và gặp lỗi thì hãy cập nhật RStockvn bằng: ``pip install --upgrade RStockvn`` hoặc gỡ và cài lại ``pip uninstall RStockvn``


## Thông báo từ phiên bản 2.5.0 trở đi [RStockvn](https://pypi.org/project/RStockvn/) không còn hỗ trợ lấy dữ liệu từ Cafef.

# Hướng dẫn
Đầu tiên bạn cần cài thư viện RStockvn bằng:
``pip install RStockvn`` hoặc nếu sử dụng Jupyter ``conda install RStockvn``
Bước 2 import thư viện: ``import RStockvn as rpv`` 

## Hàm lấy dữ liệu danh sách các công ty niêm yết trên sàn Chứng khoán Việt Nam

``rpv.list_company()``

Nếu bạn thấy danh sách đã cũ có thể thực hiện hàm bên dưới để cập nhật mới

``rpv.update_company()``


## Hàm lấy thông tin cổ phiếu từ 'vndirect':
`symbol` là biểu tượng mã cổ phiếu
Hàm lấy thông tin cổ phiếu gồm P/E, P/B, số lượng cổ phiếu đang lưu hành,... như sau: get_info_cp(symbol)

#### Ví dụ lấy thông tin cổ phiếu VND
```get_info_cp('vnd')```


## Hàm lấy lịch sử giá cổ phiếu từ 'vndirect':
`symbol` là biểu tượng mã cổ phiếu
`fromdate` là ngày bắt đầu bạn cần lấy
`todate` là ngày kết thúc
Hàm lấy lịch sử giá cổ phiếu như sau: ``get_price_historical_vnd(symbol,fromdate,todate)``

#### Ví dụ lấy lịch sử giá vnd từ ngày 20/06/2024 đến 08/08/2024
```rpv.get_price_historical_vnd('vnd','20/06/2024',08/08/2024)```

## Hàm lấy báo cáo tài chính các công ty niêm yết trên sàn Chứng khoán Việt Nam từ 'vndirect':
`symbol` là `biểu tượng mã cổ phiếu`
`report` là loại báo cáo bạn cần lấy `'BS' hoặc 'BALANCESHEET' hoặc 'CDKT'` - là báo cáo cân đối kế toán, `'P&L' hoặc 'Business results'` - là báo cáo kết quả kinh doanh, `'CF' - 'Cash Flows'` - là báo cáo lưu chuyển tiền tệ
`year` là năm tài chính bạn cần lấy
`timely` là loại báo cáo theo quý hay theo năm

rpv.report_finance_vnd(symbol,report,year,timely)

#### Ví dụ lấy bctc cân đối kế toán VNDIRECT năm 2023 theo quý
```rpv.report_finance_vnd('vnd','bs','2023','quarter')```

## Hàm lấy lãi suất theo Vietstock
Hàm lấy lãi suất như sau:``laisuat_vietstock(fromdate,todate)``, ``fromdate`` là ngày bắt đầu lãi suất cần lấy ``todate`` là ngày kết thúc.

#### Ví dụ
```
rpv.laisuat_vietstock('2022-10-12','2023-02-01')
```
## Hàm lấy chỉ số CPI theo Vietstock
Hàm lấy chỉ số CPI như sau:``getCPI_vietstock(fromdate,todate)``, ``fromdate`` là ngày bắt đầu lãi suất cần lấy ``todate`` là ngày kết thúc.

#### Ví dụ
```
rpv.getCPI_vietstock('2022-10-01','2023-02-01')
```

## Hàm lấy chỉ số Sản xuất theo Vietstock
Hàm lấy chỉ số sản xuất như sau:``solieu_sanxuat_congnghiep(fromdate,todate)``, ``fromdate`` là ngày bắt đầu lãi suất cần lấy ``todate`` là ngày kết thúc.

#### Ví dụ
```
rpv.solieu_sanxuat_congnghiep('2022-10-01','2023-02-01')
```
## 6Hàm lấy số liệu bán lẻ theo Vietstock
Hàm lấy số liệu bán lẻ như sau: ``solieu_banle_vietstock(fromdate,todate)``, ``fromdate`` là ngày bắt đầu lãi suất cần lấy ``todate`` là ngày kết thúc.

#### Ví dụ
```
rpv.solieu_banle_vietstock('2022-10-01','2023-02-01')
```

## Hàm lấy số liệu XNK theo Vietstock
Hàm lấy số liệu XNK như sau: ``solieu_XNK_vietstock(fromdate,todate)``, ``fromdate`` là ngày bắt đầu lãi suất cần lấy ``todate`` là ngày kết thúc.

#### Ví dụ
```
rpv.solieu_XNK_vietstock('2022-10-01','2023-02-01')
```


## Hàm lấy số liệu FDI theo Vietstock
Hàm lấy số liệu XNK như sau:``solieu_FDI_vietstock(fromdate,todate)``, ``fromdate`` là ngày bắt đầu lãi suất cần lấy ``todate`` là ngày kết thúc.

#### Ví dụ
```
rpv.solieu_FDI_vietstock('2022-10-01','2023-02-01')
```


## Hàm lấy số liệu tỷ giá USD/VND theo Vietstock
Hàm lấy tỷ giá USD/VND như sau:``tygia_vietstock(fromdate,todate)``, ``fromdate`` là ngày bắt đầu lãi suất cần lấy ``todate`` là ngày kết thúc.

#### Ví dụ
```
rpv.tygia_vietstock('2022-10-01','2023-02-01')
```


## Hàm lấy số liệu tín dụng theo Vietstock
Hàm lấy số liệu tín dụng như sau:``solieu_tindung_vietstock(fromdate,todate)``, ``fromdate`` là ngày bắt đầu lãi suất cần lấy ``todate`` là ngày kết thúc.

#### Ví dụ
```
rpv.solieu_tindung_vietstock('2022-10-01','2023-02-01')
```


## Hàm lấy số liệu tín dụng theo Vietstock
Hàm lấy số liệu tín dụng như sau:``solieu_GDP_vietstock(fromyear,fromQ,toyear,toQ)``, ``fromyear`` ``toyear`` năm bắt đầu và năm kết thúc, ``fromQ``, ``toQ`` quý bắt đầu và quý kết thúc.

#### Ví dụ
Bạn muốn chỉ số GDP từ Quý 2 năm 2020 đến Quý 3 năm 2022.
```
rpv.solieu_GDP_vietstock('2020','2','2022','3')
```

# Lời kết
Nếu bạn thấy dự án này hữu ích, bạn có thể ủng hộ chúng tôi qua mã QR dưới đây để giúp duy trì và phát triển dự án.

![QR Code for Donations](./RStockvn/data/donate_qr.jpg)

Bạn có thể liên hệ thông qua email: nguyenphucbinh67@gmail.com
