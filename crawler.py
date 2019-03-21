import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import time

class Crawler:

    def __init__(self, url):
        self.url = url
        self.hash_set = set()
        self.start_time = int()
        self.end_time = int()
    def start(self, hashs_queue, idx):
        if idx == 1:
            self.start_time = time()
        res = requests.get(self.url, params={'p': idx})
        if res.status_code == 200:
            html = res.text

            soup = BeautifulSoup(html, 'html.parser')

            hashs=soup.find_all('span', class_='hash-tag text-truncate')
            is_first = True
            for tx_hash, tx_from, tx_to in zip(hashs[0::3], hashs[1::3], hashs[2::3]):
                # for avoid duplicate
                if tx_hash.text in self.hash_set:
                    pass
                else:
                    hashs_queue.put([[tx_hash.text, tx_from.text, tx_to.text], idx, datetime.now() if is_first else ''])
                    self.hash_set.add(tx_hash.text)
                    is_first = False

            if idx == 10000:
                self.end_time=time()

            return True

        elif res.status_code == 404:
            print('There is no page. maybe crawler reached end of the page.')
            return False

        else:
            print('Failed to get pages Plz check network status or server. error code : {0}'.format(res.status_code))
            exit(1)

    def ret_processing_time(self):
        return self.end_time - self.start_time

