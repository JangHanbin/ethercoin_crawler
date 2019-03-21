from openpyxl import Workbook
from openpyxl import load_workbook
from datetime import datetime
class ExcelSaver:
    def __init__(self,file_name):
        self.file_name = file_name
        self.wb = Workbook()
        self.sheet1 = self.wb.active
        self.sheet1.title = 'etherscan.io'
        self.sheet1.append(['TxHash', 'From', 'To', 'Page', 'TimeStamp'])
        self.wb.save(file_name)


    def save_to_file(self, hashes, page):
        wb = load_workbook(self.file_name)
        sheet1_append = wb.active
        max_row = self.sheet1.max_row
        # write every datetime for each page

        self.wb.save(filename=self.file_name)
        is_first = True
        for tx_hash, tx_from, tx_to in zip(hashes[0::3], hashes[1::3], hashes[2::3]):
            sheet1_append.append([tx_hash.text, tx_from.text,tx_to.text, page, datetime.now() if is_first else ''])
            is_first = False
        wb.save(self.file_name)

