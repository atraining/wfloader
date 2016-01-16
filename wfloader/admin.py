from django.contrib import admin
from .models import Asset, Price, Wikifolio, Investor, Trade, Comment,Wiki_Price, AssetUniverse,AssetCategory
from commands import get_wikifolios
from commands import MemorySavingQuerysetIterator
import socket
import time
# http://stackoverflow.com/questions/2338041/python-django-polling-of-database-has-memory-leak
# delete Queries, which are normall stored in debug mode
from django import db

class PriceAdmin(admin.ModelAdmin):
    #exclude = ('contacts',)
    #actions = [get_contacts_with_openapi, get_profile_from_xing]
    list_display = ('asset','date','price')
    #readonly_fields = ('created_at','updated_at','contacts')
    search_fields = ['wkn','isin','ticker']

class Wiki_PriceAdmin(admin.ModelAdmin):
    list_display = ('wikifolio','date')
    #search_fields = ['wikifolio']


class CommentAdmin(admin.ModelAdmin):
    #exclude = ('contacts',)
    #actions = [get_contacts_with_openapi, get_profile_from_xing]
    list_display = ('comment_id','date_time','asset','wikifolio')
    #readonly_fields = ('created_at','updated_at','contacts')
    search_fields = ['content']



class WikifolioAdmin(admin.ModelAdmin):
    #exclude = ('contacts',)
    #actions = [get_contacts_with_openapi, get_profile_from_xing]
    list_display = ('wiki_id','owner','wikiname')
    #readonly_fields = ('created_at','updated_at','contacts')
    search_fields = ['isin','wiki_id']#,'owner']
    actions = ['search_new_wikifolios','get_meta','get_comments','get_price','get_trade']
    list_filter = ('got_meta','got_comments','got_price','got_trades')
    #ordering = ('?',)

    def search_new_wikifolios(self, request, queryset):
        page_start= 8900
        self.message_user(request, "9000 possible Wikifolios will be updated. Wait until you See Finish!" )
        while page_start<12000:
            print(page_start)
            page_start = get_wikifolios(page_start)
        self.message_user(request, "Finished! 9000 possible Wikifolios successfully updated.")

    search_new_wikifolios.short_description = "1. Get all Wikifolios"

    def get_meta(self, request, queryset):
        queryset = queryset.order_by('?') # random processing
        #print queryset
        #return 0
        #queryset all selected Wikifolios
        info_msg = ''
        while True:

            try:
                for wiki in queryset:
                    wiki.get_meta()
                    db.reset_queries()
            except MemoryError as e:
                print '[MemoryError in wiki.get_meta() %s]: %s'+ (wiki.wiki_id,e)

            except:
                raise
                print "[Get_Wiki_Meta]:failed totally for %s, %s, %s" % (wiki.wiki_id,wiki.wikiname,wiki.id)

            else:
                break

                info_msg = '%s, %s' % (wiki.wiki_id,info_msg)

        self.message_user(request, "%s successfully updated." % info_msg)

    get_meta.short_description = "2. Update Wikifolio(s) Meta-Infos"

    def get_comments(self, request, queryset):
        info_msg = ''
        self.message_user(request, "Start collecting comments for selected Wikifolios")
        for wiki in queryset:
            #wiki.get_comments()

            try:
                wiki.get_comments()
                db.reset_queries()

            except socket.error as e:
                msg_info = type(e)
                print  msg_info
                print '[Errno 10054] Eine vorhandene Verbindung wurde vom Remotehost geschlossen'
                time.sleep(10)

            except:
                raise
                print "[Get_Wiki_Comments]:failed for %s, %s, %s" % (wiki.wiki_id,wiki.wikiname,wiki.id)

            info_msg = '%s, %s' % (wiki.wiki_id,info_msg)

        self.message_user(request, "Dowlnloaded all comments for %s" % info_msg)

    get_comments.short_description = "3. Get Comments of Wikifolio(s)"

    def get_price(self, request, queryset):
        queryset = queryset.order_by('?')
        info_msg = ''
        wiki_ids = queryset.values('id')

        for wiki_id in wiki_ids:
            wiki = Wikifolio.objects.get(id=wiki_id['id'])
            try:
                wiki.get_price()
                db.reset_queries()

            except socket.error as e:
                msg_info = type(e)
                print  msg_info
                print '[Errno 10054] Eine vorhandene Verbindung wurde vom Remotehost geschlossen'
                time.sleep(10)

            except:
                raise
                print "[Get_Wiki_Prices]:failed for %s, %s, %s" % (wiki.wiki_id,wiki.wikiname,wiki.id)

            info_msg = '%s, %s' % (wiki.wiki_id,info_msg)

        self.message_user(request, "Downloaded all prices for %s" % info_msg)

    get_price.short_description = "4. Get past Prices of Wikifolio(s)"

    def get_trade(self, request, queryset):
        queryset = queryset.order_by('?')
        info_msg = ''
        wiki_ids = queryset.values('id')

        for wiki_id in wiki_ids:
            wiki = Wikifolio.objects.get(id=wiki_id['id'])
            #print wiki
            try:
                wiki.get_trade()
                db.reset_queries()
                print "[Get_Wiki_Trades]: %s, %s, %s" % (wiki.wiki_id,wiki.wikiname,wiki.id)
            except socket.error as e:
                msg_info = type(e)
                print  msg_info
                print '[Errno 10054] Eine vorhandene Verbindung wurde vom Remotehost geschlossen'
                time.sleep(10)

            except AttributeError:
                print "[Get_Wiki_Trades]:failed for %s,  %s" % (wiki.wiki_id,wiki.id)

            except:
                print '#########Trade all went wrong#############'
                time.sleep(20)

            info_msg = '%s, %s' % (wiki.wiki_id,info_msg)

        self.message_user(request, "Downloaded all Trades for %s" % info_msg)

    get_trade.short_description = "5. Get Trades of Wikifolio(s)"



class InvestorAdmin(admin.ModelAdmin):
    list_display = ('nick_name','first_name','last_name','desc')
    search_fields = ['first_name','last_name','desc']
    actions = ['get_meta']
    list_filter = ('got_meta',)

    def get_meta(self, request, queryset):
        info_msg = ''
        for investor in queryset:
            try:
                investor.get_meta()
                db.reset_queries()

            except socket.error as e:
                msg_info = type(e)
                print  msg_info
                print '[Errno 10054] Eine vorhandene Verbindung wurde vom Remotehost geschlossen'
                time.sleep(10)

            except:
                print "[Get_Wiki_Investor]:failed for %s" % (investor.nick_name)
            info_msg = '%s, %s' % (investor.nick_name,info_msg)

        self.message_user(request, "%s successfully updated." % info_msg)

    get_meta.short_description = "Update Investor(s)"

# Register your models here.
admin.site.register(Asset)
admin.site.register(Price,PriceAdmin)
admin.site.register(Wikifolio,WikifolioAdmin)
admin.site.register(Investor,InvestorAdmin)
admin.site.register(Trade)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Wiki_Price,Wiki_PriceAdmin)
admin.site.register(AssetCategory)
admin.site.register(AssetUniverse)