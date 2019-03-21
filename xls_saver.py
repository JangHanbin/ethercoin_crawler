from openpyxl import Workbook
from openpyxl import load_workbook


class ExcelSaver:
    def __init__(self,file_name):
        self.file_name = file_name
        self.wb = Workbook()
        self.sheet1 = self.wb.active
        self.sheet1.title = 'etherscan.io'
        self.sheet1.append(['TxHash', 'From', 'To', 'Page', 'TimeStamp'])
        self.wb.save(file_name)

    def save_to_file(self, hashs_queue):
        wb = load_workbook(self.file_name)
        sheet1_append = wb.active

        self.wb.save(filename=self.file_name)

        while True:
            datas = hashs_queue.get()
            # the pages displayed Txhash - from order in hash-tag text-truncate
            # make tuple collection from hashs idx modular
            for hashs, page, times in zip(datas[0::3], datas[1::3], datas[2::3]):
                for tx_hash, tx_from, tx_to in zip(hashs[0::3], hashs[1::3], hashs[2::3]):
                    sheet1_append.append([tx_hash, tx_from,tx_to, page, times])

            if hashs_queue.empty():
                break


        wb.save(self.file_name)

