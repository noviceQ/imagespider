# -*- coding: utf-8 -*-
import scrapy
from wallpaper.items import WallpaperItem
from scrapy.http import Request
class PaperspiderSpider(scrapy.Spider):
    name = "paperspider"
    page = 0
    pagecount = 3
    url = "http://www.wallpaperseveryday.com/popular"
    downloadImageUrl = "http://download.wallpaperseveryday.com/getimage.php"
    allowed_domains = ["wallpaperseveryday.com"]
    start_urls = [
    		"http://www.wallpaperseveryday.com/popular?p=1"
	]
  
    def parse(self, response):
	for sel in response.xpath("//img[@class='hover_img anim']"):
		src = sel.xpath("@src").extract()
		picid = sel.xpath("@picid").extract()
		picname = sel.xpath("@alt").extract()
		print"pic name = +++%s"%picname
		picnamelist = picname[-1].split(": ")[-1].split(" ")
	  	picrealname = "+".join(picnamelist)
		picpdownloadurl = "%s?id=%s&name=%s"%(self.downloadImageUrl,picid[-1],picrealname)
		paper = WallpaperItem()
		paper['src'] = picpdownloadurl
		paper['image_urls']=picpdownloadurl
		yield paper
	self.page += 1;
	if self.page == self.pagecount:
		return
	else:
		nextUrl = '%s%d'%(self.url + "?p=",self.page)
		print 'url--->%s' % nextUrl
		yield Request(nextUrl,callback = self.parse)
		
