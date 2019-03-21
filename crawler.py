import requests
from bs4 import BeautifulSoup
from multiprocessing import Queue
from xls_saver import ExcelSaver


class Crawler:

    def __init__(self, file_name):
        self.excel_saver = ExcelSaver(file_name)
        self.hashs_queue = Queue()

    def start(self, url, idx):

        res = requests.get(url,params={'p': idx})
        if res.status_code ==200:
            # ContentPlaceHolder1_mainrow > div > div > table > tbody > tr > td > span > a
            html = res.text

            soup = BeautifulSoup(html, 'html.parser')

            hashes=soup.find_all('span', class_='hash-tag text-truncate')
            # self.hashs_queue.put(hashes)
            # the pages displayed Txhash - from order in hash-tag text-truncate
            # make tuple collection from hashs idx modular
            # print(hashes)
            self.excel_saver.save_to_file(hashes, idx)
            return True

        elif res.status_code == 404:
            print('There is no page. maybe crawler reached end of the page.')
            return False

        else:
            print('Failed to get pages Plz check network status or server. error code : {0}'.format(res.status_code))
            exit(1)


