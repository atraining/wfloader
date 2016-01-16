__author__ = 'user'

import urllib2
from BeautifulSoup import BeautifulSoup
from models import Wikifolio,Wiki_Price
import socket
import time

#http://stackoverflow.com/questions/3027160/how-to-code-a-batch-file-to-automate-django-web-server-start

def get_wikifolios(page_start):
    #tags=aktde,akteur,aktusa,akthot,aktint,etf,fonds,anlagezert,hebel&private=true&assetmanager=true&theme=true&super=true&WithoutLeverageProductsOnly=true&LeverageProductsOnly=true&startValue=0&_=1452342322853&pageSize=300
    page_url_old = "http://www.wikifolio.com/dynamic/de/de/WikifolioSearch/Search/?" \
               "tags=aktde,akteur,aktusa,akthot,aktint,etf,fonds,anlagezert,hebel" \
               "&media=true" \
               "&assetmanager=true" \
               "&theme=true" \
               "&super=true" \
               "&WithoutLeverageProductsOnly=true" \
               "&private=true" \
               "&_=1450355926367" \
               "&startValue="+str(page_start)

    page_url = "http://www.wikifolio.com/dynamic/de/de/WikifolioSearch/Search/?" \
               "tags=aktde,akteur,aktusa,akthot,aktint,etf,fonds,anlagezert,hebel" \
               "&media=true&private=true" \
               "&assetmanager=true" \
               "&theme=true" \
               "&super=true" \
               "&WithoutLeverageProductsOnly=true" \
               "&LeverageProductsOnly=true" \
               "&startValue=%s" \
               "&_=1452342322853" % (str(page_start))
        # schould find 11896 with
        #?tags=aktde,akteur,aktusa,akthot,aktint,etf,fonds,anlagezert,hebel&media=true&private=true&assetmanager=true&theme=true&super=true&WithoutLeverageProductsOnly=true&LeverageProductsOnly=true
    try:
        page = urllib2.urlopen(page_url,timeout=2).read().decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)
        wikis = soup.findAll("a", {"class": "wikifolio-preview-title-link"})
        for wiki in wikis:
            new_wiki, created = Wikifolio.objects.update_or_create(
                wiki_id = str(wiki['href']).replace("/de/de/wikifolio/",""))
            new_wiki.save()
            #if not (wiki['actions'] is None):
            print wiki['href'],created

        page_start +=12

    except urllib2.URLError as e:
        #raise
        msg_info = type(e)
        print msg_info
        time.sleep(5)

    except socket.timeout as e:
        #raise
        msg_info = type(e)
        print  msg_info
        time.sleep(5)

    except socket.error as e:
        msg_info = type(e)
        print  msg_info
        print '[Errno 10054] Eine vorhandene Verbindung wurde vom Remotehost geschlossen'
        time.sleep(10)

    return page_start

class MemorySavingQuerysetIterator(object):
#http://stackoverflow.com/questions/4856882/limiting-memory-use-in-a-large-django-queryset
    def __init__(self,queryset,max_obj_num=100):
        self._base_queryset = queryset
        self._generator = self._setup()
        self.max_obj_num = max_obj_num

    def _setup(self):
        for i in xrange(0,self._base_queryset.count(),self.max_obj_num):
            # By making a copy of of the queryset and using that to actually access
            # the objects we ensure that there are only `max_obj_num` objects in
            # memory at any given time
            smaller_queryset = copy.deepcopy(self._base_queryset)[i:i+self.max_obj_num]
            logger.debug('Grabbing next %s objects from DB' % self.max_obj_num)
            for obj in smaller_queryset.iterator():
                yield obj

    def __iter__(self):
        return self

    def next(self):
        return self._generator.next()


#
# def get_csv(url):
# 	response = urllib2.urlopen(url,timeout=100).read()#.decode('utf-8', 'ignore').read()
# 	response = response.replace('\x00','')
# 	response = response.split('\n')
# 	for res in response[5:(len(response))]: # csv starts at row 6
# 		print res.split(";")[0]
#
#
# if __name__ == "__main__":
#     price_url = 'http://www.wikifolio.com/de/Invest/Download?type=m60&name=MKBODT&dateFrom=25.12.2015&dateTo=06.01.2016'
#     trade_url = 'http://www.wikifolio.com/de/Invest/Download?type=account-statement&name=MKBODT'
#     url = price_url
#     print get_csv(url)
