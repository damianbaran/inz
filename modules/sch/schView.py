# -*- coding: utf-8 -*-
import wx
import os
import webbrowser
import cDatabase
import wx.lib.mixins.listctrl as listmix
#from src.frames import MainFrame
from schControler import sControler
from publikacja import PubDialog

#from ObjectListView import ObjectListView, ColumnDefn

class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class sView(wx.Panel, sControler):
    def __init__(self, parent):
        #wx.Frame.__init__(self, None)
        wx.Panel.__init__(self, parent=parent)
        
        self.control = sControler()
        self.handlerweb = webbrowser.get()
        
        if not os.path.exists('schdatabase.db'):
            cDatabase.createDatabase()
            
        self.session = cDatabase.connectDatabase()
        
        #cDatabase.getAllRecord(self.session)
        #cDatabase.getUserFilter(self.session)
        

        self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        globalBox = wx.BoxSizer( wx.VERTICAL )
        
        oneBox1 = wx.BoxSizer( wx.HORIZONTAL )
        
        oneBox11 = wx.BoxSizer( wx.VERTICAL )
        
        oneSB1 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Wyszukiwarka Google Scholar" ), wx.VERTICAL )
        
        oneBox111 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt1 = wx.StaticText( self.panel, wx.ID_ANY, u"Wszystkie słowa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt1.Wrap( -1 )
        oneBox111.Add( self.txt1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl1 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox111.Add( self.ctrl1, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB1.Add( oneBox111, 0, wx.EXPAND, 5 )
        
        oneBox112 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt2 = wx.StaticText( self.panel, wx.ID_ANY, u"Wyrażenie:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt2.Wrap( -1 )
        oneBox112.Add( self.txt2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl2 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 200,20 ), 0 )
        oneBox112.Add( self.ctrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB1.Add( oneBox112, 0, wx.EXPAND, 5 )
        
        oneBox113 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt3 = wx.StaticText( self.panel, wx.ID_ANY, u"Jedno ze słów:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )
        oneBox113.Add( self.txt3, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl3 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox113.Add( self.ctrl3, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB1.Add( oneBox113, 0, wx.EXPAND, 5 )
        
        oneBox114 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt4 = wx.StaticText( self.panel, wx.ID_ANY, u"Bez słów:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt4.Wrap( -1 )
        oneBox114.Add( self.txt4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl4 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox114.Add( self.ctrl4, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB1.Add( oneBox114, 0, wx.EXPAND, 5 )
        
        oneBox115 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt5 = wx.StaticText( self.panel, wx.ID_ANY, u"Autor:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt5.Wrap( -1 )
        oneBox115.Add( self.txt5, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl5 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox115.Add( self.ctrl5, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB1.Add( oneBox115, 0, wx.EXPAND, 5 )
        
        oneBox116 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt6 = wx.StaticText( self.panel, wx.ID_ANY, u"Dziedzina:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt6.Wrap( -1 )
        oneBox116.Add( self.txt6, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl6 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox116.Add( self.ctrl6, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB1.Add( oneBox116, 0, wx.EXPAND, 5 )
        
        oneBox117 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt7 = wx.StaticText( self.panel, wx.ID_ANY, u"Rok od:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt7.Wrap( -1 )
        oneBox117.Add( self.txt7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl7 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 49,20 ), 0 )
        oneBox117.Add( self.ctrl7, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )
        
        self.txt8 = wx.StaticText( self.panel, wx.ID_ANY, u"do", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt8.Wrap( -1 )
        oneBox117.Add( self.txt8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl8 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 48,20 ), 0 )
        oneBox117.Add( self.ctrl8, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )
        
        self.but1 = wx.Button( self.panel, wx.ID_ANY, u"Pobierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox117.Add( self.but1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB1.Add( oneBox117, 0, wx.EXPAND, 5 )
        
        
        oneBox11.Add( oneSB1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneBox1.Add( oneBox11, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
        
        oneBox12 = wx.BoxSizer( wx.VERTICAL )
        
        oneSB2 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Wyszukiwanie Grupowe" ), wx.VERTICAL )
        
        oneBox121 = wx.BoxSizer( wx.VERTICAL )
        
        self.txt21 = wx.StaticText( self.panel, wx.ID_ANY, u"Wyszukiwanie dla wcześniej zdefiniowanej grupy autorów.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt21.Wrap( -1 )
        oneBox121.Add( self.txt21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.FIXED_MINSIZE, 5 )
        
        
        oneSB2.Add( oneBox121, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        self.oneBox122 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt22 = wx.StaticText( self.panel, wx.ID_ANY, u"Grupa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt22.Wrap( -1 )
        self.oneBox122.Add( self.txt22, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        ch1Choices = cDatabase.getGroupName(self.session)
        self.ch1 = wx.Choice( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,-1 ), ch1Choices, 0 )
        self.ch1.SetSelection( 0 )
        self.oneBox122.Add( self.ch1, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5 )
        
        
        oneSB2.Add( self.oneBox122, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        oneBox123 = wx.BoxSizer( wx.VERTICAL )
        
        self.but7 = wx.Button( self.panel, wx.ID_ANY, u"Pobierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox123.Add( self.but7, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB2.Add( oneBox123, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneBox12.Add( oneSB2, 1, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
        
        oneSB3 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Filtracja" ), wx.VERTICAL )
        
        oneBox124 = wx.BoxSizer( wx.VERTICAL )
        
        self.txt12 = wx.StaticText( self.panel, wx.ID_ANY, u"Filtracje danych można przeprowadzić po ściągnięciu danych.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.txt12.Wrap( -1 )
        oneBox124.Add( self.txt12, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        oneSB3.Add( oneBox124, 0, wx.EXPAND, 5 )
        
        oneBox125 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt13 = wx.StaticText( self.panel, wx.ID_ANY, u"Imie i Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt13.Wrap( -1 )
        oneBox125.Add( self.txt13, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ch4Choices = cDatabase.getUserName(self.session)
        self.ch4 = wx.Choice( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,-1 ), self.ch4Choices, 0 )
        self.ch4.SetSelection( 0 )
        oneBox125.Add( self.ch4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB3.Add( oneBox125, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        oneBox126 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.but2 = wx.Button( self.panel, wx.ID_ANY, u"Filtruj", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox126.Add( self.but2, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB3.Add( oneBox126, 0, wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, 5 )
        
        
        oneBox12.Add( oneSB3, 1, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
        
        
        oneBox1.Add( oneBox12, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
        
        oneBox13 = wx.BoxSizer( wx.VERTICAL )
        
        oneSB4 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Dodaj autora" ), wx.VERTICAL )
        
        oneBox132 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt14 = wx.StaticText( self.panel, wx.ID_ANY, u"Uczelnia Wyższa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt14.Wrap( -1 )
        oneBox132.Add( self.txt14, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        cb1Choices = []
        self.cb1 = wx.ComboBox( self.panel, wx.ID_ANY, u"Uczelnia", wx.DefaultPosition, wx.Size( 202,21 ), cb1Choices, 0 )
        self.cb1.SetSelection( 0 )
        oneBox132.Add( self.cb1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB4.Add( oneBox132, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        oneBox133 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt15 = wx.StaticText( self.panel, wx.ID_ANY, u"Wydział:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt15.Wrap( -1 )
        oneBox133.Add( self.txt15, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        cb2Choices = []
        self.cb2 = wx.ComboBox( self.panel, wx.ID_ANY, u"Wydział", wx.DefaultPosition, wx.Size( 202,21 ), cb2Choices, 0 )
        self.cb2.SetSelection( 0 )
        oneBox133.Add( self.cb2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB4.Add( oneBox133, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        oneBox134 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt16 = wx.StaticText( self.panel, wx.ID_ANY, u"Instytut:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt16.Wrap( -1 )
        oneBox134.Add( self.txt16, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        cb3Choices = []
        self.cb3 = wx.ComboBox( self.panel, wx.ID_ANY, u"Instytut", wx.DefaultPosition, wx.Size( 202,21 ), cb3Choices, 0 )
        self.cb3.SetSelection( 0 )
        oneBox134.Add( self.cb3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB4.Add( oneBox134, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        oneBox135 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt17 = wx.StaticText( self.panel, wx.ID_ANY, u"Imię:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt17.Wrap( -1 )
        oneBox135.Add( self.txt17, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl17 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 202,-1 ), 0 )
        oneBox135.Add( self.ctrl17, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB4.Add( oneBox135, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        oneBox136 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt18 = wx.StaticText( self.panel, wx.ID_ANY, u"Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt18.Wrap( -1 )
        oneBox136.Add( self.txt18, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl18 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 202,-1 ), 0 )
        oneBox136.Add( self.ctrl18, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB4.Add( oneBox136, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        oneBox137 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt19 = wx.StaticText( self.panel, wx.ID_ANY, u"Filtracja:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt19.Wrap( -1 )
        oneBox137.Add( self.txt19, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl19 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 202,-1 ), 0 )
        oneBox137.Add( self.ctrl19, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB4.Add( oneBox137, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
        
        oneBox138 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt20 = wx.StaticText( self.panel, wx.ID_ANY, u"np. J Wójcik, J Wojcik, J WÓJCIK, J WOJCIK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt20.Wrap( -1 )
        oneBox138.Add( self.txt20, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.but4 = wx.Button( self.panel, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox138.Add( self.but4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneSB4.Add( oneBox138, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
        
        
        oneBox13.Add( oneSB4, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneBox1.Add( oneBox13, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
        
        
        globalBox.Add( oneBox1, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        twoBox1 = wx.BoxSizer( wx.VERTICAL )
        
        twoBox11 = wx.BoxSizer( wx.VERTICAL )
        
#        self.dataList = wx.ListCtrl( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_ICON )
        self.dataList = TestListCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,310 ), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, '', format=wx.LIST_FORMAT_CENTER, width=25)
        self.dataList.InsertColumn(1, u'Cytowań', format=wx.LIST_FORMAT_RIGHT, width=60)
        self.dataList.InsertColumn(2, u'Tytuł', format=wx.LIST_FORMAT_LEFT, width=370)
        self.dataList.InsertColumn(3, u'Autor', format=wx.LIST_FORMAT_LEFT, width=210)
        self.dataList.InsertColumn(4, u'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, u'Źródło', format=wx.LIST_FORMAT_LEFT, width=120)
#        self.dataList.InsertColumn(6, u'Wydawca', format=wx.LIST_FORMAT_LEFT, width=90)
        twoBox11.Add( self.dataList, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        
        twoBox1.Add( twoBox11, 1, wx.EXPAND, 5 )
#        
#        twoBox12 = wx.BoxSizer( wx.HORIZONTAL )
#        
#        self.but5 = wx.Button( self.panel, wx.ID_ANY, u"Dodaj wybrane", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
#        twoBox12.Add( self.but5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.RIGHT, 5 )
#        
#        self.but6 = wx.Button( self.panel, wx.ID_ANY, u"Przywróć liste", wx.DefaultPosition, wx.DefaultSize, 0 )
#        self.but6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
#        
#        twoBox12.Add( self.but6, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.RIGHT, 5 )
#        
#        
#        twoBox1.Add( twoBox12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        globalBox.Add( twoBox1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.panel.SetSizer( globalBox )
        self.panel.Layout()
        globalBox.Fit( self.panel )
        
        ########################################################################
        #  Bind
        ########################################################################
        
#        self.dataList = TestListCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,295 ), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
#        self.dataList.InsertColumn(0, '', format=wx.LIST_FORMAT_CENTER, width=25)
#        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=70)
#        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=320)
#        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=180)
#        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
#        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=120)
        
        self.but1.Bind(wx.EVT_BUTTON, self.GetData)
        self.dataList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClickCb)
        self.dataList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.selectOne)
#        self.but5.Bind(wx.EVT_BUTTON, self.GetItem)
#        self.but6.Bind(wx.EVT_BUTTON, self.backList)
        self.but2.Bind(wx.EVT_BUTTON, self.GetChoice)
#        self.but4.Bind(wx.EVT_BUTTON, self.getUserData)
        self.but7.Bind(wx.EVT_BUTTON, self.settmp)
        
        ########################################################################
        #  Metody sch.controler.py
        ########################################################################
        
        self.menu_title_by_id = {1:'Zaznacz',2:'Odznacz',3:'Zaznacz wszystko',4:'Odznacz wszystko'}
        
    def GetChoice(self, event):
        try:
            self.updateRecord(self.control.SetFilter(self.control.SetItems(), self.getChoice(), cDatabase.getUserFilter(self.session)))
        except ValueError:
            wx.MessageBox(u'Nie zaznaczono wartości do filtracji', 'Blad', wx.OK | wx.ICON_INFORMATION)
        else:
            self.dataList.DeleteAllItems()
            self.updateRecord(self.control.SetFilter(self.control.SetItems(), self.getChoice(), cDatabase.getUserFilter(self.session)))
    
        
    def backList(self):
        self.dataList.DeleteAllItems()
        self.updateRecord(self.control.SetSearchItem())
    
    def addOneRecord(self):
        tmp = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                tmp.append(i)
#        print len(tmp)
        
        if len(tmp) == 1:
            data = self.control.SetItems()
            id = tmp[0]
            print data[id]
            self.editPubDial(data[id])
        else:
            wx.MessageBox(u'Nie wybrałeś rekordu, badz\nwybrales ich za dużo!', u'Bład', wx.OK | wx.ICON_INFORMATION)
        
        self.deselectAll()
    
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
                
                r = (t[2], t[3], t[1], '', t[4], '', '', None, '', '')
                print r
                cDatabase.addPubMultiData(self.session, r)
        
        self.deselectAll()
    
    def editPubDial(self, data):
        dlg = PubDialog()
#        print data
        dlg.m_textCtrl2.SetValue(data[2])
        dlg.m_textCtrl4.SetValue(data[3])
        dlg.m_textCtrl3.SetValue(str(data[1]))
#        dlg.m_choice1.SetStringSelection(data[4])
        dlg.m_textCtrl5.SetValue(str(data[4]))
#        dlg.m_textCtrl6.SetValue(data[6])
#        dlg.m_textCtrl7.SetValue(data[7])
#        dlg.m_choice2.SetStringSelection(data[8])
#        print data
        dlg.ShowModal()
        
    def RightClickCb(self, event):        
        self.currentItem = event.m_itemIndex
        menu = wx.Menu()
        for (id,title) in self.menu_title_by_id.items():
            menu.Append(id, title)
            wx.EVT_MENU(menu, id, self.MenuSelectionCb)        
        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        self.dataList.PopupMenu(menu, event.GetPoint())
        menu.Destroy() # destroy to avoid mem leak
            
    def MenuSelectionCb(self, event):
        operation = self.menu_title_by_id[event.GetId()]
        print operation
        if operation == 'Zaznacz':
            self.selectOne(self)
        elif operation == 'Odznacz':
            self.deselectOne()
        elif operation == 'Czysc liste':
            self.dataList.DeleteAllItems()
        elif operation == 'Zaznacz wszystko':
            self.selectAll()
        elif operation == 'Odznacz wszystko':
            self.deselectAll()
        elif operation == 'Otworz artykul':
            self.getLink(self.currentItem)
        elif operation == 'Zapisz do bazy':
            print 't'
    
    def openLink(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
#                x = self.dataList.GetItemText(i)
                self.getLink(i)
            
    def getLink(self, id):
        data = self.control.SetItems()
        t = self.dataList.GetItemCount()
        for i in range(t):
            if i == id:
                tmp = data[i]
                self.handlerweb.open_new_tab(tmp[7])
                if tmp[7] == 'Brak':
                    wx.MessageBox(u'Brak adresu URL do artykułu', u'Bład!', wx.OK | wx.ICON_INFORMATION)
    
    def updateRecord(self, data):
        """
        """
        for i in range(len(data)):
            self.dataList.Append(data[i])
            
    def getChoice(self):
        h = self.ch4.GetCurrentSelection()
        if h == -1:
            raise ValueError
        print h
        return self.ch4Choices[h]
        
    def selectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i)
        
    def deselectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i, False)
            
    def selectOne(self, event):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i)

    def getItem(self):
        l = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                l.append(i)
        return l
            
    def deselectOne(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i, False)
        
    def printWord(self):
        txt1 = self.ctrl1.GetValue()
        txt2 = self.ctrl2.GetValue()
        txt3 = self.ctrl3.GetValue()
        txt4 = self.ctrl4.GetValue()
        txt5 = self.ctrl5.GetValue()
        txt6 = self.ctrl6.GetValue()
        txt7 = self.ctrl7.GetValue()
        txt8 = self.ctrl8.GetValue()
#        print (txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8)
        return (txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8)
        
    def GetGroupName(self):
        curr = self.ch1.GetStringSelection()
        return curr
    
    def GetItem(self, event):
        """Pobieranie danych z wyszukiwania i tworzenie listy do przekazania dla menadzera publikacji"""
        self.control.SelectAllClick(self.getItem())
        
    def GetData(self, event):
        self.dataList.DeleteAllItems()
        self.control.AddWord(self.printWord())
        self.updateRecord(self.control.SetItems())
    
#    def upStat(self):
#        t = self.control.getProc()
#        return t
#        
        ########################################################################
        ## Metody cDatabase.py
        ########################################################################
        
#    def getUserData(self, event):
#        AllDict = {}
#        UserDict = {}
#        ColDict = {}
#        FacDict = {}
#        InsDict = {}
#        
#        dbCollege = self.cb1.GetValue()
#        dbFaculty = self.cb2.GetValue()
#        dbInstitut = self.cb3.GetValue()
#        dbName = self.ctrl17.GetValue()
#        dbSurname = self.ctrl18.GetValue()
#        dbFilter = self.ctrl19.GetValue()
#        
#        if dbCollege == '' or dbFaculty == '' or dbInstitut == '' or dbName == '' or dbSurname == '' or dbFilter == '':
#            wx.MessageBox(u'Wszystkie pola są wymagane', u'Błąd', wx.OK | wx.ICON_INFORMATION)
#            return
#        
#        ColDict['name'] = dbCollege
#        FacDict['name'] = dbFaculty
#        InsDict['name'] = dbInstitut
#        UserDict['name'] = dbName
#        UserDict['surname'] = dbSurname
#        UserDict['filtr'] = dbFilter
#        
#        AllDict = {'college':ColDict,'faculty':FacDict,'institute':InsDict,'person':UserDict}
#        
#        print AllDict
#        cDatabase.addUser(self.session,AllDict)
#        
#        """Update kontrolki z imionami i nazwiskami autorów do filtracji"""
#        self.ch4Choices = self.SetUserName()
#        self.ch4.Clear()
#        self.ch4.AppendItems(self.ch4Choices)
#        self.ch4.SetSelection( 0 )
#        
#        """Aktualizacja kontrolki z nazwami uczelni"""
#        cb1Choices = self.SetCollegeName()
#        self.cb1.Clear()
#        self.cb1.AppendItems(cb1Choices)
##        self.cb1.SetSelection( 0 )
#        
#        """Aktualizacja kontrolki z nazwami wydziałów"""
#        cb2Choices = self.SetFacultyName()
#        self.cb2.Clear()
#        self.cb2.AppendItems(cb2Choices)
##        self.cb2.SetSelection( 0 )
#        
#        """Aktualizacja kontrolki z nazwami instytutów"""
#        cb3Choices = self.SetInstituteName()
#        self.cb3.Clear()
#        self.cb3.AppendItems(cb3Choices)
##        self.cb3.SetSelection( 0 )
#        
#        self.ctrl17.SetValue('')
#        self.ctrl18.SetValue('')
#        self.ctrl19.SetValue('')
    
    def updateGroupName(self):
        ch1Choices = cDatabase.getGroupName(self.session)
        self.ch1.Clear()
        self.ch1.AppendItems(ch1Choices)
        self.ch1.SetSelection( 0 )
    
    def updateAutorName(self):
        self.ch4Choices = cDatabase.getUserName(self.session)
        self.ch4.Clear()
        self.ch4.AppendItems(self.ch4Choices)
        self.ch4.SetSelection( 0 )
    
#    def SetCollegeName(self):
#        t = cDatabase.getCollegeName(self.session)
#        return t
#    
#    def SetFacultyName(self):
#        t = cDatabase.getFacultyName(self.session)
#        return t
#    
#    def SetInstituteName(self):
#        t = cDatabase.getInstituteName(self.session)
#        return t
        
    ###########################################
    ## Funkcje z Bindowane z kontrlolera bazy danych
    ###########################################
        
    def settmp(self,  event):
        self.dataList.DeleteAllItems()
        gname = self.GetGroupName()
        t = cDatabase.sendGroupSurname(self.session,  gname)
        self.control.AddWordGroup(t)
        self.updateRecord(self.control.SetItems())

