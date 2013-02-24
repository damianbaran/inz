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
    
    def getRaportData(self, data):
        self.smodel.schlist = data
    
    def DataforMen(self):
        return self.smodel.mendata
    
    def SetItems(self):
        r = self.smodel.allRecords()
        return r
        
    def SetSearchItem(self):
        r = self.smodel.schlist
        self.smodel.fulllist = r
        return r
    
    def GetYearGroup(self, data):
        self.smodel.item['ylow'] = str(data)
        self.smodel.item['yhigh'] = str(data)

    def AddWord(self, data):
        self.smodel.addWord(data)
        self.smodel.fulllist = []
        self.smodel.all_item = 0
        urls = []
        procent = float(0)
        self.smodel.firstQuery()
#        self.smodel.all_number_query
        dlg = wx.MessageDialog(None, u"Zostanie pobranych " + str(self.smodel.all_item) + u' publikacji.\nCzy na pewno chcesz kontynuować?', u"Informacja", wx.YES_NO|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if  result == wx.ID_YES:
            for i in range(len(self.smodel.all_url)):
#            print self.smodel.all_url[i]
                x = self.smodel.queryScholar(self.smodel.all_url[i])
                urls.append(x)
                p = float(100/len(self.smodel.all_url))
                procent = procent + p
#            print procent
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
            self.smodel.all_item_group = 0
        elif result == wx.ID_NO:
            self.smodel.all_item_group = 0
    
    def AddWordGroup(self,  data):
        self.smodel.searchGroup(data)
        self.smodel.fulllist = []
        self.smodel.all_item = 0
        urls = []
        procent = float(0)
        self.smodel.firstQueryGroup(data)
#        print self.smodel.all_url
        dlg = wx.MessageDialog(None, u"Zostanie pobranych " + str(self.smodel.all_item_group) + u' publikacji.\nCzy na pewno chcesz kontynuować?', u"Informacja", wx.YES_NO|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if  result == wx.ID_YES:
            for i in range(len(self.smodel.all_url)):
#            print self.smodel.all_url[i]
                x = self.smodel.queryScholar(self.smodel.all_url[i])
                urls.append(x)
                p = float(100/len(self.smodel.all_url))
                procent = procent + p
#            print procent
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
            self.smodel.all_item_group = 0
        elif result == wx.ID_NO:
            self.smodel.all_item_group = 0
