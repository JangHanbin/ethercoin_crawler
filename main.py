from crawler import Crawler
from xls_saver import ExcelSaver
import time
from multiprocessing import Pool, Manager
from time import sleep

url = 'https://etherscan.io/txs'




if __name__=='__main__':
    print('Start etherscan_crawler....')
    print('URL : {0}'.format(url))

    pool = Pool(processes=4)
    manager = Manager()
    hashs_queue = manager.Queue(maxsize=200000)
    crawler = Crawler(url)
    excel_saver = ExcelSaver('test.xlsx')
    start_time = time.time()
    result = pool.apply_async(crawler.start, (hashs_queue, 1))

    # print(result.get().encode(''))
    #
    # excel_saver.save_to_file(hashs_queue)
    end_time = time.time()
    sleep(3)
    if result.get():
        pass
    print('Running time : {0}'.format(end_time- start_time))


