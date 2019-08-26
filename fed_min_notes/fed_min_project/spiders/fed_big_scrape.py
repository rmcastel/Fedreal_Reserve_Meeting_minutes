# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:20:32 2019

@author: Richy
"""

# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

url_short = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'

# Create the Spider class
class Fed_Meet_Scrape(scrapy.Spider):
  name = "Fed_meet_min_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    meet_rough = response.xpath('.//div[@class="col-xs-12 col-md-4 col-lg-4 fomc-meeting__minutes"]')
    meet_links = meet_rough.xpath('./a[2]/@href')
    links_to_follow = meet_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
      
  def parse_pages(self, response):
    meet_date = response.xpath('.//div[@id="article"]/child::p[1]/child::strong/text()')
    meet_date_ext = meet_date.extract_first().strip()
    meet_notes = response.xpath('.//div[@id="article"]/child::p/text()')
    meet_notes_ext = meet_notes.extract()
    fed_dict[ meet_date_ext] = ' '.join(meet_notes_ext)
      
 
    
###############################################################################
###############################################################################
###############################################################################    
    
    

# =============================================================================
# I have attempted to run this script from the comand line using scrapy crawl
# function I am not able to get the csv file to write out succesfully, a prolbem 
# with characters causing confusion when we write out the csv. I have transformed
# the dictionary to a Pandas DataFrame and could successfully write the csv
# =============================================================================


     
# Initialize the dictionary **outside** of the Spider class
fed_dict = dict()
# Run the Spider
process = CrawlerProcess()
process.crawl(Fed_Meet_Scrape)
process.start()



### Write out csv ###
import pandas as pd
from datetime import date
df = pd.DataFrame.from_dict(fed_dict, orient='index', columns = ['html'])
today = (str(date.today())).replace('-', '_')

df.to_csv('fed_mins_{}.csv'.format(today), encoding='utf-8')