from crawler import Crawler
import time
from multiprocessing import Pool

url = 'https://etherscan.io/txs'

if __name__=='__main__':
    print('Start etherscan_crawler....')
    print('URL : {0}'.format(url))
    pool = Pool(4)
    crawler = Crawler('test.xlsx')

    start_time = time.time()
    # crawler.start(url, range(1,10000+1))
    # pool.map(crawler.start,range(1,10000+1))
    for page_idx in range(1,10000+1):
        crawler.start(url, page_idx)
        if page_idx==10:
            break

    end_time = time.time()
    print('Running time : {0}'.format(end_time- start_time))


