# ScholarSpider
This project named 'scholar spider' is helpful to spider some papers' title,authors,e-mails,publication date and the url from the specific sites,
for example,http://www.pnas.org.

##1.Settings
 name  | verison | download
 ------|---------|---------
python | 2.7.6   | https://www.python.org/downloads
scrapy | 1.0.5   | 
OS	   | Windows 7

##2.[Scapy](http://doc.scrapy.org/en/latest/)
Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, 
like data mining, information processing or historical archival.
###2.1 Installation
official tutorial:http://doc.scrapy.org/en/latest/intro/install.html
###2.2 Troubleshoot
with windows platform some errors may trouble you: [Click Here!](http://blog.csdn.net/laishaofa/article/details/50763390)

##3.File Tree
![](http://i.imgur.com/YjPwNG4.png)

file name  |  descrpition |
-----------|----------------------------------
data_pnas.jl | output json file
scrapy.cfg | deploy configuration file
scholar/   | project's Python module, you'll import your code from here
scholar/items.py | project items file
scholar/pipelines.py | project pipelines file
scholar/settings.py| project settings file
scholar/spiders/| a directory where i put my spiders
scholar/spiders/PNAS_Spider.py | my spider file
