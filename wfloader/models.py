from django.db import models
import urllib2
from BeautifulSoup import BeautifulSoup
import datetime
import dateutil.parser
import pytz
import socket
import time
import multiprocessing
import copy_reg
import types
nProcess = 7
import sys
from random import shuffle
#london = pytz.timezone('Europe/London')

# pickle to use class function async
def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)

# Create your models here.

# class Wikifolio
# print "[%s.%s] [Error] UnicodeEncodeError:%s %s" % (__name__, sys._getframe().f_code.co_name, e, page_name.encode('utf-8'))

class Asset(models.Model):
    wkn         = models.CharField(max_length=255, blank=True,null=True)
    isin        = models.CharField(max_length=255, blank=True,unique=True)
    ticker      = models.CharField(max_length=255, blank=True,null=True)
    #permalink 			= models.URLField(blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.isin)

class AssetCategory(models.Model):
    asset_category = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return "%s" % (self.asset_category)


class Price(models.Model):
    asset       = models.ForeignKey(Asset,blank=True,default=u'')
    price       = models.FloatField(blank=True,null=True,default=u'')
    date        = models.DateTimeField(blank=True,null=True,default=u'')

    def __unicode__(self):
        return "%s" % (self.asset.wkn)


class Investor(models.Model):
    nick_name = models.CharField(max_length=255,blank=True,null=True)
    first_name  = models.CharField(max_length=255,blank=True,null=True)
    last_name   = models.CharField(max_length=255,blank=True,null=True)
    desc     = models.TextField(null=True, blank=True)
    more_info = models.CharField(max_length=255,blank=True,null=True)

    risk_one  = models.CharField(max_length=255,blank=True,null=True)
    risk_two  = models.CharField(max_length=255,blank=True,null=True)
    risk_three  = models.CharField(max_length=255,blank=True,null=True)
    risk_four  = models.CharField(max_length=255,blank=True,null=True)
    risk_five  = models.CharField(max_length=255,blank=True,null=True)

    # add custom admin filter
    got_meta  = models.BooleanField(blank=False,default=False)

    #shuffle(results)


    def get_meta(self):
        if self.got_meta == True:
            print '[Download_Wiki_Investor]available Investor Nick Name: %s' % (self.nick_name)
            return  0

        self.got_meta = False
        self.save()
        # http://www.wikifolio.com/de/profile/nickleeson79

        try:
            print '[Download_Wiki_Investor] Wiki %s ID: %s' % (self.nick_name)
            #http://www.wikifolio.com/de/de/profil/assetcontroller
            page_url = "http://www.wikifolio.com/de/de/profil/"+self.nick_name
            f = urllib2.urlopen(page_url,timeout=2)#.decode('utf-8', 'ignore')
            page = f.read()
            f.close()

            soup = BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)
            self.more_info = "###Profile Page available###"
            ## if url can be found, WF still excists
            # therefore update end to today

        except socket.error as e:
            msg_info = type(e)
            print  msg_info
            print '[Errno 10054] Eine vorhandene Verbindung wurde vom Remotehost geschlossen'
            time.sleep(10)
            return 0

        except:
            self.more_info = "###Homepage not available####"
            self.save()
            return 0

        try:
            # div class legitimized-user-name
            full_name = soup.find("span",{"class":"trader-nickname"}).text
            self.first_name = full_name.split(" ")[0]
            self.last_name = full_name.split(" ")[1]
        except AttributeError:
            self.first_name = ""
            self.last_name = ""
        except (IndexError,KeyError):
            self.first_name = None
            self.last_name = None

        try:
            self.desc = soup.find("div",{"class":"trader-profile-desc"}).text
        except (IndexError,KeyError):
            self.desc = None

        try:
            risk_info = soup.findAll("div",{"class":"col-xs-12 col-md-8"})[0].findAll('div')[1]
            #print risk_info
        except (IndexError,KeyError):
            risk_info = None

        try:
            self.risk_one = risk_info[0].text.replace('&nbsp;',' ')
        except (IndexError,KeyError):
            self.risk_one = None

        try:
            self.risk_two = risk_info[1].text.replace('&nbsp;',' ')
        except (IndexError,KeyError):
            self.risk_two = None
        try:
            self.risk_three = risk_info[2].text.replace('&nbsp;',' ')
        except (IndexError,KeyError):
            self.risk_three = None

        try:
            self.risk_four = risk_info[3].text.replace('&nbsp;',' ')
        except (IndexError,KeyError):
            self.risk_four = None
        try:
            self.risk_five = risk_info[4].text.replace('&nbsp;',' ')
        except (IndexError,KeyError):
            self.risk_five = None

        self.got_meta = True
        self.save()

    def __unicode__(self):
        return "%s " % (self.nick_name)

class Wikifolio(models.Model):
    """
    Basic Wikifolio as created by :model:`wfloader.Investor`.
    """

    wiki_id = models.CharField(max_length=200, blank=False, unique=True)
    isin = models.CharField(max_length=200,null=True, blank=True)
    wkn = models.CharField(max_length=200,null=True, blank=True)
    owner       = models.ForeignKey(Investor,blank=True,null=True)
    #manager = models.CharField(max_length=200,null=True, blank=True) ## Foreign Key
    wikiname        = models.CharField(max_length=255,blank=True,null=True)
    longdesc     = models.TextField(null=True, blank=True)
    full_html     = models.TextField(null=True, blank=True)
    universe = models.TextField(null=True, blank=True)
    created = models.DateTimeField(blank=True,null=True)
    end     = models.DateTimeField(blank=True,null=True)
    bid = models.FloatField(blank=True,null=True)
    ask = models.FloatField(blank=True,null=True)
    aum = models.FloatField(blank=True,null=True)
    emission = models.DateTimeField(blank=True,null=True)
    general_fee = models.FloatField(blank=True,null=True)
    perf_fee = models.FloatField(blank=True,null=True)
    analysis_instrument = models.CharField(max_length=255,blank=True,null=True)
    # volume only available on trading days
    #volume = models.FloatField(blank=True,null=True)

    # Boolean
    investable  = models.BooleanField(blank=False,default=False)
    maybe_lerveraged = models.BooleanField(blank=False,default=False)
    real_money_pf = models.BooleanField(blank=False,default=False)
    updated_prices_on = models.DateTimeField(blank=True,null=True)

    # Function called
    got_meta  = models.BooleanField(blank=False,default=False)
    got_comments  = models.BooleanField(blank=False,default=False)
    got_price  = models.BooleanField(blank=False,default=False)
    got_trades  = models.BooleanField(blank=False,default=False)

    # Universe
    assetcategory = models.ManyToManyField(AssetCategory,through='AssetUniverse')



    # New Features
    # add admin filter with, has price, has trades, has comments, has meta


    # missing date fields for update
    # updated price

    def get_meta(self):
        """
        Initializes :model:`wfloader.Wikifolio` to retrieve all infos which are
        on the Wikifolio page e.g. http://www.wikifolio.com/de/de/wikifolio/aktien-deutschland-02.
        """

        if self.got_meta == True:
            print '[Download_Wiki_Meta] already available Wiki %s ID: %s' % (self.wikiname,self.wiki_id)
            return 0

        self.got_meta = False
        self.save()

        try:
            print '[Download_Wiki_Meta] Wiki %s ID: %s' % (self.wikiname,self.wiki_id)
            page_url = "http://www.wikifolio.com/de/de/wikifolio/"+self.wiki_id
            page = urllib2.urlopen(page_url,timeout=4).read()#.decode('utf-8', 'ignore')
            soup = BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)
            self.full_html = soup.prettify()
            ## if url can be found, WF still excists
            # therefore update end to today
            self.end = datetime.datetime.today().replace(tzinfo=pytz.utc)
        except socket.error as e:
            msg_info = type(e)
            print  msg_info
            print '[Errno 10054] Eine vorhandene Verbindung wurde vom Remotehost geschlossen'
            #raise
            time.sleep(10)
            return 0
        except:
            full_html = None
            self.wikiname = "###Homepage not available####"
            self.save()
            return 0


        try:
            test_if_in_html = soup.findAll("i",{"title":"Investierbar"})[0]
            #print (test_if_in_html)
            self.investable = True
        except (IndexError,AttributeError):
            self.investable = False

        try:
            test_if_in_html = soup.findAll("i",{"title":"Kann Hebelprodukte enthalten"})[0]
            #print (test_if_in_html)
            self.maybe_lerveraged = True
        except (IndexError,AttributeError):
            self.maybe_lerveraged = False

        try:
            test_if_in_html = soup.findAll("i",{"title":"Real-Money-wikifolio"})[0]
            #print (test_if_in_html)
            self.real_money_pf = True
        except (IndexError,AttributeError):
            self.real_money_pf = False

        try:
            self.isin = soup.find("input",{"id":"wikifolio-isin"})['value']
        except (IndexError,KeyError):
            self.isin = None

        try:
            self.wkn= soup.find("input",{"id":"wikifolio-wkn"})['value']
        except (IndexError,KeyError):
            self.wkn = None

        try:
            a_area = soup.findAll("a",{"class":"area"})
            #/de/de/profil/Bullenbrief
            for a_link in a_area:
                if a_link['href'][:14] == '/de/de/profil/':
                    self.manager_link = a_link['href']
                    manager_name = self.manager_link.replace('/de/de/profil/','')
            new_manger, created = Investor.objects.update_or_create(
                nick_name = manager_name)
            #################
            # get manager meta
            ##################
            new_manger.get_meta()
            new_manger.save()
            self.owner = new_manger
        except IndexError:
            self.manager = None

        try:
            self.wikiname = soup.find("input",{"id":"wikifolio-shortdesc"})['value']
        except (IndexError,KeyError):
            self.wikiname = None

        try:
            info_table = soup.find("div",{"class":"col-xs-12 col-sm-6 js-wikifolio-data"})
            div_infos = info_table.findAll("div",{"class":"detail-row"})
            created_text =  div_infos[0].find('i').previousSibling\
                .replace('\n','')\
                .replace(' ','')\
                .replace('\r','')
            #print creation_date
            #http://stackoverflow.com/questions/8636760/parsing-a-datetime-string-into-a-django-datetimefield
            created_datetime = datetime.datetime.strptime(created_text, "%d.%m.%Y") #dateutil.parser.parse('%s 00:00:00-00' % created_text)
            self.created= created_datetime.replace(tzinfo=pytz.utc)
            self.updated_prices_on = created_datetime.replace(tzinfo=pytz.utc)
        except (IndexError,ValueError): # remove value error as created_text
        # u'03.01.2014' is correctly formatted
            self.created = None
            self.updated_prices_on = None

        try:
            self.longdesc = soup.findAll("p",{"class":"preformatted"})[0].text
        except IndexError:
            self.longdesc = None

        ###
        # Posprocessing Universe
        ##

        try:
            universe = soup.findAll("div",{"id":"collapseSix"})#[0]
            self.universe = universe
            universe = universe[0]
            #print universe
            #print '#############################'
            self.analysis_instrument = universe.findAll("div",{"class":"class-box"})[1].text
            #print '#############################'
            asset_categories =  universe.findAll("div",{"class":"class-box"})[3]
            for span in asset_categories.findAll("span"):

                try:
                    asset_category =  span.text.replace(',','').replace(' ','')

                    asset_category,created = AssetCategory.objects.update_or_create(
                        asset_category = asset_category
                    )

                    try:
                        #print span['class']
                        available_for_investing = False
                    except:
                        available_for_investing = True
                        #print 'no class'

                    asset_universe, created = AssetUniverse.objects.update_or_create(
                        asset_category = asset_category,
                        wikifolio = self,
                        available_to_wikifolio = available_for_investing
                    )

                except:
                    print 'no AssetCategory added'


        except IndexError:
            self.universe = None


        ###
        # end Posprocessing Universe
        ##

        try:
            self.bid= float(soup.findAll("h4",{"class":"wikifolio-detail-performance-header"})[0].
                            text.replace('.', '').replace(',', '.'))
        except (IndexError,ValueError): # ValueError cannot convert N/A to float
            self.bid = None

        try:
            self.ask = float(soup.findAll("h4",{"class":"wikifolio-detail-performance-header"})[1].
                             text.replace('.', '').replace(',', '.'))
        except (IndexError,ValueError): # ValueError cannot convert N/A to float
            self.ask = None

        try:
            self.aum = float(soup.findAll("h4",{"class":"wikifolio-detail-performance-header"})[2].
                             text.replace('.', '').replace(',', '.').replace(u'\u20ac',''))
        except (IndexError,ValueError): # ValueError cannot convert N/A to float
           self.aum = None

        try:
            ls = soup.findAll("div",{"class":"wikifolio-detail-rows-container"})[0]
            first_row = ls.find("div",{"class":"detail-row-first"})
            ls_info_available = True
        except (IndexError,AttributeError):
            ls_info_available = False

        if ls_info_available:
            try:
                emission_text = first_row.span.find('i').previousSibling\
                    .replace('\n','')\
                    .replace(' ','')\
                    .replace('\r','')
                #http://stackoverflow.com/questions/8636760/parsing-a-datetime-string-into-a-django-datetimefield
                emission_datetime = datetime.datetime.strptime(emission_text, "%d.%m.%Y") #dateutil.parser.parse('%s 00:00:00-00' % emission_text)
                self.emission= emission_datetime.replace(tzinfo=pytz.utc)
            except (IndexError,ValueError):
                self.emission = None
            except AttributeError as e:
                print 'emmission_text->NoneType object has no attribute span'

            try:
                # get comission
                href_text = "/de/de/wie-investieren/anleger-wissen/zertifikat-investieren/wikifolio-gebuehren"
                fees = ls.findAll("a",{"href":href_text})
            except:
                print 'no fees: '+self.wiki_id

            try:
                self.general_fee = float(fees[0].text
                                         .replace('.', '').replace(',', '.').replace('%',''))/100
            except (IndexError,ValueError): # ValueError cannot convert N/A to float
                self.general_fee = None

            try:
                self.perf_fee = float(fees[1].text
                                         .replace('.', '').replace(',', '.').replace('%',''))/100
            except (IndexError,ValueError): # ValueError cannot convert N/A to float
                self.perf_fee = None

        self.got_meta = True
        self.get_comments()
        self.save()


    def get_comments(self):
        if self.got_comments == True:
            print '[Download_Comments][available] Wiki %s ID: %s' % (self.wikiname,self.wiki_id)
            return 0

        self.got_comments = False
        self.save()

         # http://www.wikifolio.com/de/Invest/GetPagedMessagesForWikifolio?id=MKBODT&page=1&pageSize=3000
        try:
            print '[Download_Comments] WikiID: %s' % (self.wiki_id)
            #http://www.wikifolio.com/dynamic/de/de/invest/getpagedmessagesforwikifolio?page=1&pageSize=3000&id=investmentfox-nebenwerte
            page_url = "http://www.wikifolio.com/dynamic/" \
                       "de/de/invest/getpagedmessagesforwikifolio?" \
                       "page=1" \
                       "&pageSize=3000" \
                       "&id="+self.wiki_id
            page = urllib2.urlopen(page_url,timeout=3).read()#.decode('utf-8', 'ignore')
            try:
                soup = BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)
            except:
                soup = BeautifulSoup(page)
            #print soup.prettify()

        except socket.error as e:
            msg_info = type(e)
            print  msg_info
            print '[Errno 10054] Eine vorhandene Verbindung wurde vom Remotehost geschlossen'
            time.sleep(1)
            return 0

        except:
            return 0

        for comment in soup.findAll("div", {"class": "user-comment"}):
            comment_id = comment['id']
            #print comment_id
            new_comment, created = Comment.objects.update_or_create(
                comment_id = comment_id)

            new_comment.wikifolio = self
            new_comment.date_time = datetime.datetime\
                .strptime(comment.find("time")['datetime'],"%d.%m.%Y %H:%M:%S")\
                .replace(tzinfo=pytz.utc) #dateutil.parser.parse(comment.find("time")['datetime'])
            comment_text = comment.find("div", {"class": "message-item-content"})
            if not (comment_text is None):
                new_comment.content = comment_text.text

            isin = comment.find("div", {"class": "comment-underlying-isin"})
            if not (isin is None):
                isin = isin.text.replace('(','').replace(')','')
                new_asset, created = Asset.objects.update_or_create(
                    isin = isin)
                new_comment.asset = new_asset

            new_comment.save()

        self.got_comments = True
        self.save()

    def resultCollector(self, result):
        self.__result.append(result)


    def get_price(self):
        if self.got_price==True:
            print "[GOT_Download_Price] Wiki:'%s' |ID:%s" % (self.wikiname,self.wiki_id),
            return 0

        print "[Download_Price] Wiki:'%s' |ID:%s" % (self.wikiname,self.wiki_id),
        #self.got_price = False
        #self.save()

        #http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
        #start_date = datetime.datetime.strptime(self.created, "%d.%m.%y") # extract from string
        #http://stackoverflow.com/questions/6871016/adding-5-days-to-date-in-python
        start_date = self.updated_prices_on #.replace(tzinfo=None) # create day of wikifolio
        today = datetime.datetime.today().replace(tzinfo=pytz.utc)# Today date

        pool = multiprocessing.Pool(processes=nProcess)
        self.__result = []
        while (today - start_date) > datetime.timedelta(days = 0):
            start_date_str = start_date.strftime("%d.%m.%y")
            end_date = start_date + datetime.timedelta(days=120)
            end_date_str = end_date.strftime("%d.%m.%y")



            # download data in range
            pool.apply_async(self.get_price_history, args=(start_date_str,end_date_str),
                             callback=self.resultCollector)

            ### old sequencial version
            ### self.get_price_history(start_date_str,end_date_str)#

            # increase counter
            start_date = end_date + datetime.timedelta(days=1)

        pool.close()
        pool.join()

        print(self.__result)


        print "[Downloaded_Price_Finish] Wiki:'%s' |ID:%s" % (self.wikiname,self.wiki_id)

        self.got_price = True
        self.updated_prices_on = today.replace(tzinfo=pytz.utc) # update last avail. price
        self.save()


    def get_price_history(self,start_date_str,end_date_str):
        insert_list = []
        # http://voorloopnul.com/blog/doing-bulk-update-and-bulk-create-with-django-orm/

        #http://www.wikifolio.com/dynamic/de/de/invest/download?type=m60&name=CONTROL1
        price_url = 'http://www.wikifolio.com/dynamic/de/de/invest/download?type=m60&dateFrom=%s&dateTo=%s&name=%s' % \
                    (start_date_str,end_date_str,self.wiki_id)
        trade_url = 'http://www.wikifolio.com/de/Invest/Download?type=account-statement&name=%s' % \
                    (self.wiki_id)
        response = urllib2.urlopen(price_url,timeout=30).read()#.decode('utf-8', 'ignore').read()
        response = response.replace('\x00','')
        response = response.split('\n')
        for res in response[5:(len(response))]: # csv starts at row 6
            #sys.stdout.write('|')
            row = res.split(";")
            #print row
            date = datetime.datetime.strptime(row[0], "%d.%m.%Y %H:%M:%S").replace(tzinfo=pytz.utc)#dateutil.parser.parse(row[0])
            #print date
            #print (res.split(";")[0]) # in january days wrong way arround to month

            # OLD Version - Really Slow with update_or_create
            # new_price, created = Wiki_Price.objects.update_or_create(
            #     wikifolio = self,
            #     date = date)
            # if created:
            #     new_price.price_interval= float(row[1].replace(',','.'))
            #     new_price.open_price = float(row[2].replace(',','.'))
            #     new_price.close_price = float(row[3].replace(',','.'))
            #     new_price.high_price = float(row[4].replace(',','.'))
            #     new_price.low_price = float(row[5].replace(',','.'))
            #     new_price.save()

            new_price = Wiki_Price(
                wikifolio = self,
                date = date,
                price_interval= float(row[1].replace(',','.')),
                open_price = float(row[2].replace(',','.')),
                close_price = float(row[3].replace(',','.')),
                high_price = float(row[4].replace(',','.')),
                low_price = float(row[5].replace(',','.')),
            )

            insert_list.append(new_price)

        Wiki_Price.objects.bulk_create(insert_list)





        print "|",start_date_str,"-",end_date_str,"-OK",

    def get_trade(self):
        if self.got_trades==True:
            return 0

        print "[Download_Trade] Wiki:'%s' |ID:%s" % (self.wikiname,self.wiki_id),
        self.got_trades = False
        self.save()

        start_date = self.created #.replace(tzinfo=None) # create day of wikifolio
        start_date_str = start_date.strftime("%d.%m.%y")
        end_date = datetime.datetime.today().replace(tzinfo=pytz.utc)# Today date
        end_date_str = end_date.strftime("%d.%m.%y")

        print "\n|",start_date_str,"-",end_date_str,

        self.get_trade_history(start_date_str,end_date_str)

        print "[Download_Trade_Finish] Wiki:'%s' |ID:%s" % (self.wikiname,self.wiki_id)

        self.got_trades = True
        self.save()

    def get_trade_history(self,start_date_str,end_date_str):
        #http://www.wikifolio.com/dynamic/de/de/invest/download?type=account-statement&name=BULLE02
        trade_url = 'http://www.wikifolio.com/dynamic/de/de/invest/download?' \
              'type=account-statement' \
              '&name=%s' \
              '&dateFrom=%s' \
              '&dateTo=%s' % (self.wiki_id,start_date_str,end_date_str)
        print trade_url
        response = urllib2.urlopen(trade_url,timeout=30).read().decode('utf-8', 'ignore')#.read()
        response = response.replace('\x00','')
        response = response.split('\n')
        for res in response[5:(len(response))]: # csv starts at row 6

            row = res.split(";")
            #print row
            trade_date = datetime.datetime.strptime(row[0], "%d.%m.%Y %H:%M:%S").replace(tzinfo=pytz.utc)#dateutil.parser.parse(row[0])
            description         = row[1]
            isin                = row[2]

            try:
                num_assets_change   = float(row[3].replace('.','').replace(',','.'))
            except ValueError:
                num_assets_change   = None

            try:
                num_assets_after    = float(row[4].replace('.','').replace(',','.'))
            except ValueError:
                num_assets_after   = None

            try:
                asset_price         = float(row[5].replace('.','').replace(',','.'))
            except ValueError:
                asset_price   = None

            try:
                cash_change         = float(row[6].replace('.','').replace(',','.'))
            except ValueError:
                cash_change   = None

            try:
                cash_after          = float(row[7].replace('.','').replace(',','.'))
            except ValueError:
                cash_after   = None

            new_trade_type, created_trade_type = Trade_Type.objects.update_or_create(
                trade_type = description)

            new_asset, created_asset = Asset.objects.update_or_create(
                wkn = None,
                ticker = None,
                isin = isin)

            new_asset_price=Price.objects.create(
                asset = new_asset,
                date= trade_date,
                price = asset_price)

            new_trade = Trade.objects.create(
                wikifolio = self,
                asset = new_asset,
                trade_date = trade_date,
                trade_type = new_trade_type,
                num_asset_change = num_assets_change,
                num_asset_after = num_assets_after,
                cash_change = cash_change,
                cash_after_trade = cash_after)



    def __unicode__(self):
        return "%s" % (self.wiki_id)




class AssetUniverse(models.Model):
    # doku many to many https://gist.github.com/jacobian/827937
    asset_category = models.ForeignKey(AssetCategory)
    wikifolio = models.ForeignKey(Wikifolio)
    available_to_wikifolio  = models.BooleanField(blank=False,default=False)

    def __unicode__(self):
        return u"%s -->%s" % (self.asset_category,self.wikifolio)


class Wiki_Price(models.Model): # Preishistorie
    wikifolio   = models.ForeignKey(Wikifolio,blank=True)
    #price = models.FloatField(blank=True,null=True)
    date        = models.DateTimeField(blank=True,null=True)
    price_interval =   models.FloatField(blank=True,null=True)
    open_price = models.FloatField(blank=True,null=True)
    close_price = models.FloatField(blank=True,null=True)
    high_price = models.FloatField(blank=True,null=True)
    low_price = models.FloatField(blank=True,null=True)

    def __unicode__(self):
        return "%s" % (self.wikifolio.wikiname)

class Trade_Type(models.Model):
    trade_type =  models.CharField(max_length=200, blank=False,unique=True)

    def __unicode__(self):
        return "%s" % (self.trade_type)

class Trade(models.Model): # Konto
    wikifolio               = models.ForeignKey(Wikifolio,blank=True)
    asset                   = models.ForeignKey(Asset,blank=True)
    trade_date              = models.DateTimeField(blank=True,null=True)
    trade_type              = models.ForeignKey(Trade_Type,blank=True)
    num_asset_change        = models.FloatField(blank=True,null=True)
    num_asset_after         = models.FloatField(blank=True,null=True)
    cash_change             = models.FloatField(blank=True,null=True)
    cash_after_trade        = models.FloatField(blank=True,null=True)

    def __unicode__(self):
        return "%s for %s" % (self.wikifolio.wikiname,self.asset.isin)

    #quantity                = models.FloatField(blank=True,null=True)
    #cash                    = models.FloatField(blank=True,null=True) # as reported by wikifolio.de

class Comment(models.Model):
    comment_id =  models.CharField(max_length=200, blank=False, unique=True)
    date_time        = models.DateTimeField(blank=True,null=True)
    asset       = models.ForeignKey(Asset,blank=True,null=True)
    wikifolio    = models.ForeignKey(Wikifolio,blank=True,null=True)
    content     = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return "%s" % (self.comment_id)



#class Investments(Models.model):

#class (Models.model):