# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy

class WallpaperPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
         image_url = item['image_urls']
         print "imageurl%s"%image_url 
         yield scrapy.Request(image_url)
    def item_completed(self, results, item, info):
          print info
