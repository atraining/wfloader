# import urllib2
#
#
# def get_csv(url):
#     response = urllib2.urlopen(url,timeout=100).read()#.decode('utf-8', 'ignore').read()
#     response = response.replace('\x00','')
#     print response
#
#
#
# if __name__ == "__main__":
#     price_url = 'http://www.wikifolio.com/de/Invest/Download?type=m60&name=MKBODT&dateFrom=01.01.2015&dateTo=06.01.2016'
#     trade_url = 'http://www.wikifolio.com/de/Invest/Download?type=account-statement&name=MKBODT'
#     url = price_url
#     print get_csv(url)
