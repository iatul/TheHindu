import scrapy
import logging
import datetime
from db import Query
import time
import timeit
#logger = logging.getLogger(__name__)

class TheHindu(scrapy.Spider):
    name = "hindu"
    allowed_domains = ["thehindu.com"]
    base_url = "http://www.thehindu.com/archive/web/"
    HTTP_OK = 200

    def start_requests(self):
        query = Query()
        query.create()
        query.close()
        start_date = datetime.date( year = 2017, month = 2, day = 1)
        end_date = datetime.date( year = 2017, month = 3, day = 19 ) # datetime.date.today()    
        urls = []
        
        for date in self.daterange( start_date, end_date ):
            self.date = date
            date_formatted = date.strftime('%Y/%m/%d/')
            url = self.base_url + date_formatted
            yield scrapy.Request(url=url, callback=self.parse)  

    def parse(self, response):
        data = []
        if response.status != self.HTTP_OK:
            print('Error:' . response.status )
            return
            
        filename = response.url.split("/")[-2]
        for sel in response.xpath('//ul[@class="archive-list"]/li'):
            link = sel.xpath('a/@href').extract()[0].encode('utf-8')
            text = sel.xpath('a/text()').extract()[0].encode('utf-8')
            text = ''.join([i if ord(i) < 128 and ord(i) !=39 else ' ' for i in text])
            #text =''.join(["/"+i if ord(i) in [34,39] else i  if ord(i) < 128 else ' ' for i in text])

            data.append([text, link])
        print (self.date.strftime('%Y-%m-%d'),len(data))    
        start_time = timeit.default_timer()
        self.insert(data)
        elapsed = timeit.default_timer() - start_time
        print('elapsed time: ', elapsed)
        #time.sleep(1)

    def daterange(self, start_date, end_date ):
        if start_date <= end_date:
            for n in range( ( end_date - start_date ).days + 1 ):
                yield start_date + datetime.timedelta( n )
            else:
                for n in range( ( start_date - end_date ).days + 1 ):
                    yield start_date - datetime.timedelta( n )    


    def insert(self, data):

        sql = """INSERT INTO `hindu`(`title`,
        `link`, `date`)
        VALUES """
        db_date = self.date.strftime('%Y-%m-%d')
        f= open('/home/atul/sql.txt','w')
        for row in data:
            sql += '(\'' + row[0] + '\'' + ', ' + '\'' + row[1] + '\'' + ', ' + '\'' + db_date + '\'),'

        sql = sql.rstrip(',')
            
        #f.write(sql)
        query = Query()
        query.execute(sql)
        query.close()



