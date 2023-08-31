# Copyright 2023 Nguyen Phuc Binh @ GitHub
# See LICENSE for details.
__version__ = "2.1.8"
__author__ ="Nguyen Phuc Binh"
__copyright__ = "Copyright 2023, Nguyen Phuc Binh"
__license__ = "MIT"
__email__ = "nguyenphucbinh67@gmail.com"
__website__ = "https://github.com/NPhucBinh"

from . import user_agent
#from . import data_cafef
#from . import cafef_test
from .stockvn import (report_finance_cf,report_finance_cp68,get_data_history_cafef,getCPI_vietstock,solieu_GDP_vietstock
                      ,info_company,trade_internal,laisuat_vietstock,event_price_cp68,exchange_currency,
                      tygia_vietstock,historical_price_cp68,solieu_XNK_vietstock,solieu_tindung_vietstock,solieu_sanxuat_congnghiep
                      ,solieu_banle_vietstock,solieu_danso_vietstock,solieu_FDI_vietstock,baocaonhanh)