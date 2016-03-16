# -*- coding:utf-8 -*-
import scrapy
from scholar.items import SpiderItem

class ScholarSpider(scrapy.Spider):
    name = "pnas"
    allowed_domains = ["pnas.org"]
    start_urls = [
        "http://www.pnas.org/search?tmonth=&pubdate_year=2016&submit=yes&submit=Submit&submit=yes&andorexacttitle=and&format=standard&firstpage=&fmonth=&title=&tyear=&hits=4&titleabstract=&volume=&sortspec=relevance&andorexacttitleabs=and&author2=&tocsectionid=all&andorexactfulltext=and&author1=&fyear=&doi=&fulltext="
    ]
    index = 0

    # 文献列表页的回调函数
    def parse(self, response):
        reqst = []
        content = response.xpath('//form[@id="results-gca-form"]')
        searchCount = content.xpath('div/div/span[@class="search-results-count"]')
        piecePerPage = searchCount.xpath('text()').re(r'[0-9]+')[1]
        pages = searchCount.xpath('span/text()').re(r'\d+')[0]
        print "Pieces Per Page:%d" %(long(piecePerPage))
        print "Total Pages:%d" %(long(pages))
        
        # 1.提取当前页每篇文章的url
        # 2.使用每篇文章的url生成request，指定回调函数为parse_pose()
        paper_urls = content.xpath('ol/li/div/div[@class="cit-extra"]/ul/li[@class="first-item"]/a/@href').re(r'\S+.[exabs]+tract')
        for url in paper_urls:
            url = "http://www."+self.allowed_domains[0] + url
            reqst.extend([self.make_requests_from_url(url).replace(callback=self.parse_post)])
            
        # reqst.extend([self.make_requests_from_url(url).replace(callback=self.parse_post) for url in pageResult])
        
        # 如果发送的request总数达到最大就停止'下一页'跟进
        # print "index = %d" %(self.index)
        if(self.index+len(reqst) >= 20):
            return [reqst]
        
        # 1.如果request总数没有达到最大，则提取'下一页'的url
        # 2.如果'下一页'url存在，则使用下一页的url生成request，回调函数为parse()
        next_urls = response.xpath('//a[@title="Next search results"]/@href').extract()
        if( len(next_urls) > 0):
            url = "http://www." + self.allowed_domains[0] + next_urls[0]
            reqst.append(self.make_requests_from_url(url))
        
        # 返回当前页列表中所有文献的request和下一页的request
        return reqst
        
    # 文献页的回调函数
    def parse_post(self, response):
        item = SpiderItem()
        title = response.xpath('//h1[@id="article-title-1"]/text() | //h1[@id="article-title-1"]//*/text()').re(r'\S+\s?')
        title = "".join(title)
        title = title.strip()
        title = title.replace('\n',' ').replace('\r',' ')
        author = response.xpath('//ol[@id="contrib-group-1"]/li/span/a/text()').extract()
        date = response.xpath('//div[@id="sidebar"]/span/span/span[@class="slug-ahead-of-print-date"]/text()').extract()
        mail = response.xpath('//span/span[@class="em-addr"]/text()').extract()
        for i in range(0,len(mail)):
            mail[i] = mail[i].replace('{at}','@')
        
        item['domain'] = self.allowed_domains[0]
        item['title'] = title
        item['author'] = author
        item['date'] = date
        item['mail'] = mail
        item['link'] = response.url
        self.index += 1
        
        return [item]