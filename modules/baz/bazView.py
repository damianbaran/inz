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
import os
import re
import wx.lib.mixins.listctrl as listmix
import webbrowser
import cDatabase
import lxml.html
import time
import shutil
from lxml.html import builder as E
from wx.lib.pubsub import Publisher
from popup.publikacja import PubDialog
from popup.grupa import GroupDialog
from popup.wydawca import JourDialog
from popup.wys_cytowania import CiteDialog

## Dokumentacja dla klasy
#
# Klasa tworzy zaawansowana kontrolke do wyswietlania publikacji
class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    ##Konstruktor
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

## Dokumentacja dla klasy
#
# Klasa zawiera widok bazy danych i metody do niego
class bView(wx.Panel, PubDialog):
    ## Konstruktor
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        self.session = cDatabase.connectDatabase()
        listSearch = [u'Autor', u'AutorID', u'DOI', u'Grupa', u'Adres', u'Rok', u'Tytul', u'Wydawca']
        self.handlerweb = webbrowser.get()
    
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        m_choice31Choices = listSearch
        self.m_choice31 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice31Choices, 0 )
        self.m_choice31.SetSelection( 0 )
        bSizer3.Add( self.m_choice31, 0, wx.ALL, 5 )        
        
        self.m_searchCtrl1 = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.m_searchCtrl1.ShowSearchButton( True )
        self.m_searchCtrl1.ShowCancelButton( False )
        bSizer3.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )
        
        bSizer21.Add( bSizer3, 0, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.dataList = TestListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1007,390 ), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, 'ID', format=wx.LIST_FORMAT_CENTER, width=23)
        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=60)
        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=370)
        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=210)
        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=120)
        self.dataList.InsertColumn(6, u'Źródło', format=wx.LIST_FORMAT_LEFT, width=120)
        bSizer4.Add( self.dataList, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer21.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        self.m_panel1.SetSizer( bSizer21 )
        self.m_panel1.Layout()
        bSizer21.Fit( self.m_panel1 )
        
############################################################
## Bindowanie
#############################################################
        
        self.m_searchCtrl1.Bind(wx.EVT_TEXT_ENTER, self.searchPubClick)
        self.dataList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.selectOne)
        self.dataList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClickCb)

        #Pozycje dal popmenu
        self.menu_title_by_id = {1:'Zaznacz',2:'Odznacz',3:'Zaznacz wszystko',4:'Odznacz wszystko'}
        self.id_cit = []
    
    ## Dokumentacja getBackUpBase
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja wczytuje kopie zapasowa bazy danych do programu
    def getBackUpBase(self):
        dlg = wx.FileDialog(self, "Wybierz Plik", 'archive', "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            shutil.copy2(os.path.join(self.dirname, self.filename), 'schdatabase.db')
            wx.MessageBox(u'Wczytano wybrana baze danych!', 'Kopia zapasowa', wx.OK | wx.ICON_INFORMATION)
    
    ## Dokumentacja backUpBase
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja wykonuje kopie zapasowa bazy danych
    def backUpBase(self):
        t = time.asctime( time.localtime(time.time()) )
        t = re.sub(u':','', t)
        shutil.copy2('schdatabase.db', 'archive/'+t+'.db')
        wx.MessageBox(u'Zrobione kopie zapasowa bazy danych\nDostępna w folderze "archive" pod nazwa '+t+'.db', 'Kopia zapasowa', wx.OK | wx.ICON_INFORMATION)
    
    ## Dokumentacja generateHtml
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja generuje plik bibliografii html'a z wybranych publikacji
    def generateHtml(self):
        home = os.getcwd()
        os.chdir('bibliography')
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                t = int(t)
                c = cDatabase.getHtmlData(self.session, t)
                self.htm(c[0])
        os.chdir(home)
        wx.MessageBox(u'Poprawnie wygenerowano bibliografię do pliku .html\nZnajdziesz go w folderze "Bibliography"', 'Wygenerowano HTML', wx.OK | wx.ICON_INFORMATION)
    
    ## Dokumentacja htm
    # @param self Wskaźnik obiektu
    # @param data Wartości publikacji
    #
    # @return void
    # Funkcja tworzy kod html dla wybranych publikacji
    def htm(self, data):
        aut = 'Czyzycki, W.; Filo, G.; Domagala, M.;'
        html = E.DIV(E.CLASS("iso-690"), 
            E.SPAN(''+data[3]+'.', E.I(' '+data[2]+'.'), ' '+data[5]+'.', ' '+str(data[4])+'.')
        ) 

        fo = open('biblografia.html', 'a')
        fo.write(lxml.html.tostring(html)+'\n')
        fo.close()
    
    ## Dokumentacja generateBibtex
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja generuje plik bibliografii bibtex z wybranych publikacji
    def generateBibtex(self):
        home = os.getcwd()
        os.chdir('bibliography')
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                t = int(t)
                c = cDatabase.getHtmlData(self.session, t)
                self.bib(c[0])
        os.chdir(home)
        wx.MessageBox(u'Poprawnie wygenerowano bibliografię do pliku .bib\nZnajdziesz go w folderze "Bibliography"', 'Wygenerowano Bibtex', wx.OK | wx.ICON_INFORMATION)
    
    ## Dokumentacja bib
    # @param self Wskaźnik obiektu
    # @param data Wartości publikacji
    #
    # @return void
    # Funkcja tworzy strukturę bibtex dla wybranej publikacji
    def bib(self, data):
        author = data[3].encode('utf-8')
        title = data[2].encode('utf-8')
        publisher = data[5].encode('utf-8')
        year = str(data[4])
        identy = title[:3] +':'+ publisher[:3]+':'+year
        book = '@misc{%s,\n' \
        '  Author = {%s},\n' \
        '  Title = {%s},\n' \
        '  Publisher = {%s},\n' \
        '  Year = {%s}\n}' % (identy, author, title, publisher, year)
        
        fo = open('bibliografia.bib', 'a')
        fo.write(book+'\n')
        fo.close()
    
    ## Dokumentacja searchPubClick
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wyswietla publikacje zapisane w bazie danych na żadania uzytkownika
    def searchPubClick(self, event):
        self.searchPub()
        
    ## Dokumentacja searchPub
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja wyszukuje wartości w bazie podane przez użytkownika
    def searchPub(self):
        self.dataList.DeleteAllItems() #Ksowanie listy w wx.ListCtrl
        t = self.m_searchCtrl1.GetValue() #Pobieranie wartości wpisanej przez użytkownika
        d = self.m_choice31.GetStringSelection() #pobieranie wartości z listy wybranej przez użytkownika
        tmp = cDatabase.getRecords(self.session, d, t) #zapytanie do bazy, zwracajace szukane elementy
        self.updateRecord(tmp) #wyswietlenie wartosci w ListCtrl
    
    ## Dokumentacja getCitPub
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja przekazuje wybrane publikacje do łaczenia
    def getCitPub(self):
        self.id_cit = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                t = int(t)
                c = cDatabase.getMergePubData(self.session, t)
                self.id_cit.append(c)
        dlg = CiteDialog()
        Publisher().sendMessage(('change_data'), self.id_cit)
        dlg.updateRecord()
        dlg.ShowModal()
    
    ## Dokumentacja editRecordData
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja dla wybranych publikacji obsluguje ich edycje
    def editRecordData(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                self.editRecord(t, cDatabase.geteditPubData(self.session, t))
        
        self.deselectAll()
    
    ## Dokumentacja editRecord
    # @param self Wskaźnik obiektu
    # @param id ID wybranej publikacji
    # @param data Wartosci wybranej publikacji
    #
    # @return void
    # Funkcja wyswietla w okienku wszystkie wartosci publikacji do edycji dla uzytkownika
    def editRecord(self, id, data):
        dlg = PubDialog()
        dlg.m_staticText1.SetLabel('Edytujesz rekord o nr. '+str(data[0]))
        dlg.m_textCtrl2.SetValue(data[1])
        dlg.m_textCtrl4.SetValue(data[2])
        dlg.m_textCtrl3.SetValue(str(data[3]))
        dlg.m_choice1.SetStringSelection(data[4])
        dlg.m_textCtrl5.SetValue(str(data[5]))
        dlg.m_textCtrl6.SetValue(data[6])
        dlg.m_textCtrl7.SetValue(data[7])
        if data[8] != None:
            dlg.m_choice2.SetStringSelection(data[8])
        dlg.m_textCtrl71.SetValue(data[12])
        dlg.m_textCtrl99.SetValue(data[13]) #Lista ministerialna
        dlg.m_choice3.SetStringSelection(data[14]) #jcr
        dlg.m_textCtrl55.SetValue(data[15])
        u = data[9]
        
        guser = cDatabase.getUserName(self.session) 
        t = cDatabase.getUserNameID(self.session)
        d = t.values()
        d.sort()
        p = {}
        for i in range(len(d)):
            x = {d[i]:i}
            p.update(x)
        print p
        
        for i in range(len(u)):
            y = p[u[i]]
            dlg.m_checkList3.Check(y)
        
        dlg.m_button1.Hide()
        dlg.m_button3.Show()
        dlg.ShowModal()
    
    ## Dokumentacja updateRecord
    # @param self Wskaźnik obiektu
    # @param data Lista wszystkich wybranych publikacji
    #
    # @return void
    # Funkcja wyswietla wszystkie publikacje jakie zostaly wyszukane na zadanie uzytkownika
    def updateRecord(self, data):
        """Funkcja uaktualnia wartości listctrl o podane wartosci"""
        a = cDatabase.getPerPubID(self.session)
        c = cDatabase.getCiteID(self.session)
        
        try:            
            for i in range(len(data)):
                self.dataList.Append(data[i])
            
            num = self.dataList.GetItemCount()
            for i in range(num):
                for j in range(len(a)):
                    if int(self.dataList.GetItemText(i)) == a[j]:
                        self.dataList.SetItemBackgroundColour(i, "green")
                for j in range(len(c)):
                    t = c[j]
                    if int(self.dataList.GetItemText(i)) == t[0]:
                        self.dataList.SetItemBackgroundColour(i, "yellow")
        except TypeError:
            wx.MessageBox(u'Brak wyszukanych danych', 'Brak danych', wx.OK | wx.ICON_INFORMATION)
    
    ## Dokumentacja RightClickCb
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wyświetla popmenu
    def RightClickCb(self, event):
        self.currentItem = event.m_itemIndex
#        print self.currentItem
        menu = wx.Menu()
        for (id,title) in self.menu_title_by_id.items():
            menu.Append(id, title)
            wx.EVT_MENU(menu, id, self.MenuSelectionCb)        
        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        self.dataList.PopupMenu(menu, event.GetPoint())
        menu.Destroy() # destroy to avoid mem leak

    ## Dokumentacja MenuSelectionCb
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wykonuje żadania użytkownika z popup menu
    def MenuSelectionCb(self, event):
        operation = self.menu_title_by_id[event.GetId()]
        print operation
        if operation == 'Zaznacz':
            self.selectOne(self)
        elif operation == 'Odznacz':
            self.deselectOne()
        elif operation == 'Zaznacz wszystko':
            self.selectAll()
        elif operation == 'Odznacz wszystko':
            self.deselectAll()
    
    ## Dokumentacja deleteChoices
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja obsługuje usuwanie publikacji wybranych przez uzytkownika
    def deleteChoices(self):
        tmp = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                tmp.append(t)
        
        dlg = wx.MessageDialog(None, u"Czy na pewno chcesz\nwykasować wybrane rekordy?", u"Kasowanie rekordów", wx.YES_NO|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if  result == wx.ID_YES:
            text = u'Trwa usuwanie zaznaczonych rekordów!'
            Publisher().sendMessage(('change_statusbar'), text)
            cDatabase.deleteMultiRecord(self.session, tmp)
        elif result == wx.ID_NO:
            dlg.Destroy()
        
        text = u'Usuwanie zakończono powodzeniem!'
        Publisher().sendMessage(('change_statusbar'), text)
        self.searchPub()
    
    ## Dokumentacja openLink
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja otwiera publikacje w przegladarce internetowej
    def openLink(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                l = cDatabase.getLinkPub(self.session, t)
                self.handlerweb.open_new_tab(l)
                if l == 'Brak':
                    wx.MessageBox(u'Brak adresu URL do artykułu', u'Bład!', wx.OK | wx.ICON_INFORMATION)
    
    ## Dokumentacja openCite
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja wyswietla wszystkie cytowania dla wybanej publikacji w przegladarce internetowej
    def openCite(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                l = cDatabase.getLinkCit(self.session, t)
                link = 'http://' + l
                self.handlerweb.open_new_tab(link)
                if l == 'Brak':
                    wx.MessageBox(u'Brak adresu URL do artykułu', u'Bład!', wx.OK | wx.ICON_INFORMATION)
    
    ## Dokumentacja selectAll
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Zaznacza wszytkie publikacje w kontrolce
    def selectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i)
    
    ## Dokumentacja deselectAll
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Odznacza wszystkie publikacje w kontrolce
    def deselectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i, False)
    
    ## Dokumentacja selectOne
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja zaznacza wybrana publikacje w kontrolce
    def selectOne(self, event):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i)
    
    ## Dokumentacja deselectOne
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja odznacza wybrana publikacje w kontrolce
    def deselectOne(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i, False)
