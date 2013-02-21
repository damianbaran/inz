# -*- coding: utf-8 -*-
import wx
from schModel import sModel
from wx.lib.pubsub import Publisher
from modules.men.menModel import mModel
from bs4 import BeautifulSoup

class sControler(sModel, mModel):
    """Controler dla modules.sch czyli wyszukiwania"""
    def __init__(self):
        self.smodel = sModel()
        self.mmodel = mModel()
#        self.statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
#        self.statusbar.SetStatusText(u'Jesteś w panelu wyszukiwania publikacji')
#        self.frame = MainFrame()
    
    def SetFilter(self, r, f, db):
        c = self.smodel.filtruj(r,f,db)
        return c
    
    def SelectAllClick(self, data):
        t = self.smodel.selectingString(data)
        self.mmodel.getData(t)
#        return t
    
    def DataforMen(self):
        return self.smodel.mendata
    
    def SetItems(self):
        r = self.smodel.allRecords()
        return r
        
    def SetSearchItem(self):
        r = self.smodel.schlist
        self.smodel.fulllist = r
        return r
    
#    def AddWord(self, data):
#        self.smodel.addWord(data)
#        self.smodel.fulllist = []
#        self.smodel.downloadData()
##        self.smodel.all_item = 0
    
    def AddWord(self, data):
        self.smodel.addWord(data)
        self.smodel.fulllist = []
        self.smodel.all_item = 0
        urls = []
        procent = float(0)
        self.smodel.firstQuery()
        for i in range(len(self.smodel.all_url)):
            print self.smodel.all_url[i]
            x = self.smodel.queryScholar(self.smodel.all_url[i])
            urls.append(x)
            p = float(100/len(self.smodel.all_url))
            procent = procent + p
            print procent
            text = ' Trwa pobieranie danych. Pobrano: ' + str(procent) + ' %'
            Publisher().sendMessage(('change_statusbar'), text)
        procent = float(0)
        for i in range(len(urls)):
            self.smodel.htmlsoup = BeautifulSoup(urls[i])
            self.smodel.doThis()
            self.smodel.onePage()
            p = float(100/len(urls))
            procent = procent + p
            text = ' Trwa generowanie danych. Wygenerowano: ' + str(procent) + ' %'
            Publisher().sendMessage(('change_statusbar'), text)
        Publisher().sendMessage(('change_statusbar'), 'Gotowe!')
        self.smodel.saveResult(self.smodel.fulllist)
        self.smodel.searchList(self.smodel.fulllist)
#        self.smodel.all_item = 0
        self.smodel.all_url = []
        self.smodel.all_number_query = 0
        
#    def AddWordGroup(self,  data):
#        self.smodel.searchGroup(data)
#        self.smodel.fulllist = []
##        self.smodel.all_item = 0
#        self.smodel.downloadDataGroup()
##        self.smodel.all_item = 0
    
    def AddWordGroup(self,  data):
        self.smodel.searchGroup(data)
        self.smodel.fulllist = []
