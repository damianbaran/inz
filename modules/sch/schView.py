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
import pickle
import webbrowser
import modules.baz.cDatabase as cDatabase
import wx.lib.mixins.listctrl as listmix
from schControler import sControler
from popup.publikacja import PubDialog

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
# Klasa zawiera widok wyszukiwania publikacji i metody do niego
class sView(wx.Panel, sControler):
    ##Konstruktor
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        self.control = sControler()
        self.handlerweb = webbrowser.get()
        
        if not os.path.exists('schdatabase.db'):
            cDatabase.createDatabase()
            self.session = cDatabase.connectDatabase()
            cDatabase.addEmptyString(self.session)
        
        self.session = cDatabase.connectDatabase()
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Wyszukiwarka Google Scholar" ), wx.VERTICAL )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Wszystkie słowa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer7.Add( self.m_staticText1, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        self.ctrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer7.Add( self.ctrl1, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Wyrażenie:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer8.Add( self.m_staticText2, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        self.ctrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer8.Add( self.ctrl2, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer1.Add( bSizer8, 0, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Jedno ze słów:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer9.Add( self.m_staticText3, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        self.ctrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer9.Add( self.ctrl3, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Bez słów:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer10.Add( self.m_staticText4, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        self.ctrl4 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer10.Add( self.ctrl4, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Autor:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer11.Add( self.m_staticText5, 1, wx.ALL, 5 )
        
        self.ctrl5 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer11.Add( self.ctrl5, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer1.Add( bSizer11, 0, wx.EXPAND, 5 )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Dziedzina:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer12.Add( self.m_staticText6, 1, wx.ALL, 5 )
        
        self.ctrl6 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer12.Add( self.ctrl6, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer1.Add( bSizer12, 0, wx.EXPAND, 5 )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Rok od:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer13.Add( self.m_staticText7, 1, wx.ALL, 5 )
        
        self.ctrl7 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 41,-1 ), 0 )
        bSizer13.Add( self.ctrl7, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticText8 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"do", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer13.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.ctrl8 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 41,-1 ), 0 )
        bSizer13.Add( self.ctrl8, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        self.but1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Pobierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.but1, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer1.Add( bSizer13, 0, wx.EXPAND, 5 )
        
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer1.Add( bSizer14, 1, wx.EXPAND, 5 )
        
        bSizer5.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Wyszukiwanie Grupowe" ), wx.VERTICAL )
        
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText9 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Wyszukiwanie dla wcześniej zdefiniowanej grupy autorów", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer15.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer2.Add( bSizer15, 0, wx.EXPAND, 5 )
        
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Grupa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer16.Add( self.m_staticText10, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        ch1Choices = cDatabase.getGroupName(self.session)
        self.ch1 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), ch1Choices, 0 )
        self.ch1.SetSelection( 0 )
        bSizer16.Add( self.ch1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer2.Add( bSizer16, 0, wx.EXPAND, 5 )
        
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText11 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Ogranicz do roku:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer17.Add( self.m_staticText11, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        self.m_textCtrl12 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
        bSizer17.Add( self.m_textCtrl12, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        self.but7 = wx.Button( self.m_panel1, wx.ID_ANY, u"Pobierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.but7, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer2.Add( bSizer17, 0, wx.EXPAND, 5 )
        
        bSizer6.Add( sbSizer2, 1, wx.ALL|wx.EXPAND, 5 )
        
        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Filtracja" ), wx.VERTICAL )
        
        bSizer18 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Filtrację danych można przeprowadzić po ściągnieciu danych", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer18.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer3.Add( bSizer18, 0, wx.EXPAND, 5 )
        
        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText13 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Imię i Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        bSizer19.Add( self.m_staticText13, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        self.ch4Choices = cDatabase.getUserName(self.session)
        self.ch4 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), self.ch4Choices, 0 )
        self.ch4.SetSelection( 0 )
        bSizer19.Add( self.ch4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer3.Add( bSizer19, 0, wx.EXPAND, 5 )
        
        bSizer20 = wx.BoxSizer( wx.VERTICAL )
        
        self.but2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Filtruj", wx.DefaultPosition, wx.DefaultSize, 0 )

        bSizer20.Add( self.but2, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer3.Add( bSizer20, 0, wx.EXPAND, 5 )
        
        bSizer6.Add( sbSizer3, 1, wx.EXPAND|wx.ALL, 5 )
        
        bSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )
        
        bSizer22.Add( bSizer3, 0, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.dataList = TestListCtrl(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 685,-1 ), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, u'ID', format=wx.LIST_FORMAT_CENTER, width=23)
        self.dataList.InsertColumn(1, u'Cytowań', format=wx.LIST_FORMAT_RIGHT, width=60)
        self.dataList.InsertColumn(2, u'Tytuł', format=wx.LIST_FORMAT_LEFT, width=260)
        self.dataList.InsertColumn(3, u'Autor', format=wx.LIST_FORMAT_LEFT, width=160)
        self.dataList.InsertColumn(4, u'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, u'Źródło', format=wx.LIST_FORMAT_LEFT, width=110)
        bSizer4.Add( self.dataList, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer22.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )
        
        self.m_panel1.SetSizer( bSizer21 )
        self.m_panel1.Layout()
        bSizer21.Fit( self.m_panel1 )
        
        ########################################################################
        ##  Bind
        ########################################################################
        
        self.but1.Bind(wx.EVT_BUTTON, self.GetData)
        self.dataList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClickCb)
        self.dataList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.selectOne)
        self.but2.Bind(wx.EVT_BUTTON, self.GetChoice)
        self.but7.Bind(wx.EVT_BUTTON, self.settmp)

        
        ########################################################################
        ##  Metody sch.controler.py
        ########################################################################
        
        self.menu_title_by_id = {1:'Zaznacz',2:'Odznacz',3:'Zaznacz wszystko',4:'Odznacz wszystko'}
        self.raport = []
    
    ## Dokumentacja GetChoice
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    # @return void
    # Funkcja wyświetla uzytkownikowi odfiltrowane dane
    def GetChoice(self, event):
        try:
            self.updateRecord(self.control.SetFilter(self.control.SetItems(), self.getChoice(), cDatabase.getUserFilter(self.session)))
        except ValueError:
            wx.MessageBox(u'Nie zaznaczono wartości \
            do filtracji', 'Blad', wx.OK | wx.ICON_INFORMATION)
        else:
            self.dataList.DeleteAllItems()
            self.updateRecord(self.control.SetFilter(self.control.SetItems(), self.getChoice(), cDatabase.getUserFilter(self.session)))
    
    ## Dokumentacja getRaport
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja wczytuje do programu zapisane publikacje w raporcie wyszukiwani
    def getRaport(self):
        dlg = wx.FileDialog(self, "Wybierz Plik", 'raport', "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = pickle.load(open(os.path.join(self.dirname, self.filename), 'r'))
            print f
            self.control.getRaportData(f)
            self.backList()
    
    ## Dokumentacja backList
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja przywraca ostatnio wczytana lub pobrana liste publikacji
    def backList(self):
        self.dataList.DeleteAllItems()
        self.updateRecord(self.control.SetSearchItem())
    
    ## Dokumentacja addOneRecord
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja wyświetla do edycji i dodaje publikacje do bazy danych
    def addOneRecord(self):
        tmp = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                tmp.append(i)
        
        data = self.control.SetItems()
        for i in range(len(tmp)):
            id = tmp[i]
            print len(data)
            print id
            self.editPubDial(data[id])
        
        self.deselectAll()
    
    ## Dokumentacja addMultiRecord
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja dodaje publikacje do bazy danych
    def addMultiRecord(self):
        tmp = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                tmp.append(i)
        
        if len(tmp) > 0:
            data = self.control.SetItems()
            for i in range(len(tmp)):
                n = tmp[i]
                t = data[n]
                print tmp
                
                r = (t[2], t[3], t[1], '', t[4], '', '', None, t[7], t[8], t[5], '', '', '')

                cDatabase.addPubMultiData(self.session, r)
        
        self.deselectAll()
    
    ## Dokumentacja editPubDial
    # @param self Wskaźnik obiektu
    # @param data Lista atrybutów wyszukanej publikacji
    #
    # @return void
    # Funkcja wyświetla wartosci publikacji w okienku do edycji
    def editPubDial(self, data):
        dlg = PubDialog()
        dlg.m_textCtrl2.SetValue(data[2])           #title
        dlg.m_textCtrl4.SetValue(data[3])           #author
        dlg.m_textCtrl3.SetValue(str(data[1]))     #citation
        dlg.m_textCtrl5.SetValue(str(data[4]))     #year
        dlg.m_textCtrl71.SetValue(data[5])          #zrodlo
        dlg.m_staticText11.SetLabel(data[7])        #urlpub
        dlg.m_staticText12.SetLabel(data[8])        #urlcit
        dlg.ShowModal()
        
    ## Dokumentacja RightClickCb
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wyświetla popmenu
    def RightClickCb(self, event):        
        self.currentItem = event.m_itemIndex
        menu = wx.Menu()
        for (id,title) in self.menu_title_by_id.items():
            menu.Append(id, title)
            wx.EVT_MENU(menu, id, self.MenuSelectionCb)        
        self.dataList.PopupMenu(menu, event.GetPoint())
        menu.Destroy()

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
    
    ## Dokumentacja openLink
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja otwiera publikacje w przegladarce internetowej
    def openLink(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                self.getLink(i)
            
    ## Dokumentacja getLink
    # @param self Wskaźnik obiektu
    # @param id ID wybranej publikacji
    #
    # @return void
    # Funkcja sprawdza czy wybrana publikacja ma adres url
    def getLink(self, id):
        data = self.control.SetItems()
        t = self.dataList.GetItemCount()
        for i in range(t):
            if i == id:
                tmp = data[i]
                self.handlerweb.open_new_tab(tmp[7])
                if tmp[7] == 'Brak':
                    wx.MessageBox(u'Brak adresu URL do artykułu', u'Bład!', wx.OK | wx.ICON_INFORMATION)
    
    ## Dokumentacja updateRecord
    # @param self Wskaźnik obiektu
    # @param data Lista publikacji do wyświetlenia
    #
    # @return void
    # Funkcja przekazuje do kontrolki liste publikacji
    def updateRecord(self, data):
        for i in range(len(data)):
            self.dataList.Append(data[i])
    
    ## Dokumentacja getChoice
    # @param self Wskaźnik obiektu
    #
    # @return string Ciag znaków z imieniem i nazwiskiem autora
    # Funkcja zwraca Imie i Nazwisko autora wybranego do filtracji
    def getChoice(self):
        h = self.ch4.GetCurrentSelection()
        if h == -1:
            raise ValueError
        return self.ch4Choices[h]
        
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
    
    ## Dokumentacja getItem
    # @param self Wskaźnik obiektu
    #
    # @return list Lista ID zaznaczonych publikacji
    # Funkcja pobiera ID wszystkich zaznaczonych publikacji w kontrolce
    def getItem(self):
        l = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                l.append(i)
        return l
    
    ## Dokumentacja printWord
    # @param self Wskaźnik obiektu
    #
    # @return tuple Lista z atrybutami do wyszukiwania
    # Funkcja przekazuje do kontrolera, liste z atrybutami do wyszukiwania publikacji
    def printWord(self):
        txt1 = self.ctrl1.GetValue()
        txt2 = self.ctrl2.GetValue()
        txt3 = self.ctrl3.GetValue()
        txt4 = self.ctrl4.GetValue()
        txt5 = self.ctrl5.GetValue()
        txt6 = self.ctrl6.GetValue()
        txt7 = self.ctrl7.GetValue()
        txt8 = self.ctrl8.GetValue()
        return (txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8)
        
    ## Dokumentacja GetGroupName
    # @param self Wskaźnik obiektu
    #
    # @return string Ciag znaków z nazwa grupy
    # Funkcja zwraca nazwe grupy do wyszukiwania grupowego
    def GetGroupName(self):
        curr = self.ch1.GetStringSelection()
        return curr
    
    ## Dokumentacja GetData
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja czyści listę i wyświetla pobrane publikacje
    def GetData(self, event):
        self.dataList.DeleteAllItems()
        self.control.AddWord(self.printWord())
        self.updateRecord(self.control.SetItems())
    
    ## Dokumentacja updateGroupName
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja aktualizuje wartości w kontrolce z nazwami grup
    def updateGroupName(self):
        ch1Choices = cDatabase.getGroupName(self.session)
        self.ch1.Clear()
        self.ch1.AppendItems(ch1Choices)
        self.ch1.SetSelection( 0 )
    
    ## Dokumentacja updateAutorName
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja aktualizuje wartości w kontrolce z nazwami autorów
    def updateAutorName(self):
        self.ch4Choices = cDatabase.getUserName(self.session)
        self.ch4.Clear()
        self.ch4.AppendItems(self.ch4Choices)
        self.ch4.SetSelection( 0 )
    
    ## Dokumentacja getYearGroup
    # @param self Wskaźnik obiektu
    #
    # @return string Rok do wyszukiwania grupwego
    # Funkcja pobiera rok podany przez uzytkownika przy wyszukiwaniu grupowym
    def getYearGroup(self):
        t1 = self.m_textCtrl12.GetValue()
        return t1
    
    ## Dokumentacja settmp
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja czyści listę i wyświetla pobrane publikacje z wyszukiwania grupwego
    def settmp(self,  event):
        self.dataList.DeleteAllItems()
        gname = self.GetGroupName()
        t = cDatabase.sendGroupSurname(self.session,  gname)
        self.control.GetYearGroup(self.getYearGroup())
        self.control.AddWordGroup(t)
        self.updateRecord(self.control.SetItems())
