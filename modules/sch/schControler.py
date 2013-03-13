# -*- coding: utf-8 -*-

################################################
##    Aplikacja wspomagajaca tworzenie bazy publikacji naukowych wpsółpracujaca z Google Scholar
##    Copyright (C) 2013  Damian Baran
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################

import wx
from schModel import sModel
from wx.lib.pubsub import Publisher
from bs4 import BeautifulSoup

## Dokumentacja dla klasy
#
# Kontroler do modelu wyszukiwania publikacji naukowych
class sControler(sModel):
    ## Konstruktor
    def __init__(self):
        self.smodel = sModel()
    
    ## Dokumentacja SetFilter
    # @param self Wskaźnik obiektu
    # @param r Lista wszystkich pobranych publikacji
    # @param f Imie i Nazwisko autora do filtracji
    # @param db Klucze filtrujace dla wybranego autora
    #
    # @return list Lista odfiltrowanych publikacji
    def SetFilter(self, r, f, db):
        c = self.smodel.filtruj(r,f,db)
        return c
    
    ## Dokumentacja getRaportData
    # @param self Wskaźnik obiektu
    # @param data Lista publikacji
    #
    # @return void
    # Funkcja przekazuje listę publikacji wczytana z raportu wyszukiwnaia
    def getRaportData(self, data):
        self.smodel.schlist = data
    
    ## Dokumentacja SetItems
    # @param self Wskaźnik obiektu
    #
    # @return list Lista wszystkich wyszukanych publikacji
    def SetItems(self):
        r = self.smodel.allRecords()
        return r
    
    ## Dokumentacja SetSearchItem
    # @param self Wskaźnik obiektu
    #
    # @return list Lista odfiltrowanych publikacji
    def SetSearchItem(self):
        r = self.smodel.schlist
        self.smodel.fulllist = r
        return r
    
    ## Dokumentacja GetYearGroup
    # @param self Wskaźnik obiektu
    # @param data Liczba z rokiem podana przez użytkownika
    #
    # @return void
    # Funkcja przypisuje atrybuty do generowania adresów url
    def GetYearGroup(self, data):
        self.smodel.item['ylow'] = str(data)
        self.smodel.item['yhigh'] = str(data)

    ## Dokumentacja AddWord
    # @param self Wskaźnik obiektu
    # @param data Lista atrybutów do wyszukiwania
    #
    # @return void
    # Funkcja kontroluje wyszukiwanie zdefiniowane przez użytkownika
    def AddWord(self, data):
        self.smodel.addWord(data)
        self.smodel.fulllist = []
        self.smodel.all_item = 0
        urls = []
        procent = float(0)
        self.smodel.firstQuery()
        dlg = wx.MessageDialog(None, u"Zostanie pobranych " + str(self.smodel.all_item) + u' publikacji.\nCzy na pewno chcesz kontynuować?', u"Informacja", wx.YES_NO|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if  result == wx.ID_YES:
            for i in range(len(self.smodel.all_url)):
                x = self.smodel.queryScholar(self.smodel.all_url[i])
                urls.append(x)
                p = float(100/len(self.smodel.all_url))
                procent = procent + p
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
            self.smodel.all_url = []
            self.smodel.all_number_query = 0
            self.smodel.all_item_group = 0
        elif result == wx.ID_NO:
            self.smodel.all_item_group = 0
    
    ## Dokumentacja AddWordGroup
    # @param self Wskaźnik obiektu
    # @param data Lista autorów do wyszukiwania
    #
    # @return void
    # Funkcja kontroluje wyszukiwanie grupowe
    def AddWordGroup(self,  data):
        self.smodel.searchGroup(data)
        self.smodel.fulllist = []
        self.smodel.all_item = 0
        urls = []
        procent = float(0)
        self.smodel.firstQueryGroup(data)
        dlg = wx.MessageDialog(None, u"Zostanie pobranych " + str(self.smodel.all_item_group) + u' publikacji.\nCzy na pewno chcesz kontynuować?', u"Informacja", wx.YES_NO|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if  result == wx.ID_YES:
            for i in range(len(self.smodel.all_url)):
                x = self.smodel.queryScholar(self.smodel.all_url[i])
                urls.append(x)
                p = float(100/len(self.smodel.all_url))
                procent = procent + p
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
            self.smodel.all_url = []
            self.smodel.all_number_query = 0
            self.smodel.all_item_group = 0
        elif result == wx.ID_NO:
            self.smodel.all_item_group = 0
