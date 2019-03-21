from crawler import Crawler
from xls_saver import ExcelSaver
from multiprocessing import Pool, Manager


URL = 'https://etherscan.io/txs'
END_OF_PAGE = 50
if __name__=='__main__':
    print('Start etherscan_crawler....')
    print('URL : {0}'.format(URL))
    #
    pool = Pool(processes=8)
    manager = Manager()
    hashs_queue = manager.Queue(maxsize=200000)
    crawler = Crawler(URL)
    excel_saver = ExcelSaver('test.xlsx')

    crawler.end_of_page=END_OF_PAGE
    for i in range(1, END_OF_PAGE+1):
        result = pool.apply_async(crawler.start, (hashs_queue, i))

    # for result in results:
    if result.get():
        excel_saver.save_to_file(hashs_queue)

    print('Running time : {0}'.format(crawler.ret_processing_time()))


