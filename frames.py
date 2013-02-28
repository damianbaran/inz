# -*- coding: utf-8 -*-

import wx
import os
from modules.sch.schView import sView
#from modules.men.menView import mView
from modules.baz.bazView import bView
from publikacja import PubDialog
from grupa import GroupDialog
from wydawca import JourDialog
from autor import AuthorDialog
from about import About
from wx.lib.pubsub import Publisher

class MainFrame(wx.Frame):
    def __init__(self):
#        wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = u"ScholBar", pos = wx.DefaultPosition, size = wx.Size( 1024,545 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_NO_TASKBAR|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
        wx.Frame.__init__(self, None, id = wx.ID_ANY, title = u"PubRansack", pos = wx.DefaultPosition, size = wx.Size( 1024,535 ), style = wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER))
        
        self.panel_sch = sView(self)
#        self.panel_men = mView(self)
        self.panel_baz = bView(self)
#        self.panel_men.Hide()
        self.panel_baz.Hide()
        
        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
        
        firstSizer = wx.BoxSizer( wx.VERTICAL )
        
        firstSizer.Add(self.panel_sch, 1, wx.EXPAND)
#        firstSizer.Add(self.panel_men, 1, wx.EXPAND)
        firstSizer.Add(self.panel_baz, 1, wx.EXPAND)
        
        self.SetSizer( firstSizer )
        self.Layout()
        
        self.statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        Publisher().subscribe(self.change_statusbar, 'change_statusbar')
        
        ico = wx.Icon('icon/ikona.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, 21, u"Wyszukiwarka", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem1.SetBitmap( wx.Bitmap( u"icon/search16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu1.AppendItem( self.m_menuItem1 )
        
        self.m_menuItem2 = wx.MenuItem( self.m_menu1, 22, u"Baza danych", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem2.SetBitmap( wx.Bitmap( u"icon/base16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu1.AppendItem( self.m_menuItem2 )
        
        self.m_menu1.AppendSeparator()
        
        self.m_menuItem6 = wx.MenuItem( self.m_menu1, 23, u"Wyjdź", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem6.SetBitmap( wx.Bitmap( u"icon/exit16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu1.AppendItem( self.m_menuItem6 )
        
        self.m_menubar1.Append( self.m_menu1, u"Widok" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menuItem20 = wx.MenuItem( self.m_menu2, 24, u"Wczytaj z pliku", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem20.SetBitmap( wx.Bitmap( u"icon/fileopen16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu2.AppendItem( self.m_menuItem20 )
        
        self.m_menuItem21 = wx.MenuItem( self.m_menu2, 25, u"Przywróc ostatnio wybrane", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem21.SetBitmap( wx.Bitmap( u"icon/back16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu2.AppendItem( self.m_menuItem21 )
        
        self.m_menuItem22 = wx.MenuItem( self.m_menu2, 26, u"Czyść listę", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem22.SetBitmap( wx.Bitmap( u"icon/clear16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu2.AppendItem( self.m_menuItem22 )
        
        self.m_menu2.AppendSeparator()
        
        self.m_menuItem23 = wx.MenuItem( self.m_menu2, 27, u"Edytuj i Zapisz", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem23.SetBitmap( wx.Bitmap( u"icon/add16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu2.AppendItem( self.m_menuItem23 )
        
        self.m_menuItem24 = wx.MenuItem( self.m_menu2, 28, u"Zapisz wszystkie", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem24.SetBitmap( wx.Bitmap( u"icon/addm16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu2.AppendItem( self.m_menuItem24 )
        
        self.m_menuItem25 = wx.MenuItem( self.m_menu2, 29, u"Wyświetl publikację", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem25.SetBitmap( wx.Bitmap( u"icon/browser16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu2.AppendItem( self.m_menuItem25 )
        
        self.m_menubar1.Append( self.m_menu2, u"Wyszukiwarka" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu3, 30, u"Zarządzanie Autorami", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem7.SetBitmap( wx.Bitmap( u"icon/autor16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu3.AppendItem( self.m_menuItem7 )
        
        self.m_menuItem8 = wx.MenuItem( self.m_menu3, 31, u"Zarządzanie Grupami", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem8.SetBitmap( wx.Bitmap( u"icon/grupa16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu3.AppendItem( self.m_menuItem8 )
        
        self.m_menuItem9 = wx.MenuItem( self.m_menu3, 32, u"Zarządzanie Publikacjami", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem9.SetBitmap( wx.Bitmap( u"icon/pub16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu3.AppendItem( self.m_menuItem9 )
        
        self.m_menuItem10 = wx.MenuItem( self.m_menu3, 33, u"Zarządzanie Wydawcami", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem10.SetBitmap( wx.Bitmap( u"icon/journal16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu3.AppendItem( self.m_menuItem10 )
        
        self.m_menu3.AppendSeparator()
        
        self.m_menu11 = wx.Menu()
        self.m_menuItem11 = wx.MenuItem( self.m_menu11, 34, u"Edytuj wybrane", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem11.SetBitmap( wx.Bitmap( u"icon/edit16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.AppendItem( self.m_menuItem11 )
        
        self.m_menuItem12 = wx.MenuItem( self.m_menu11, 35, u"Usuń wybrane", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem12.SetBitmap( wx.Bitmap( u"icon/delete16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.AppendItem( self.m_menuItem12 )
        
        self.m_menuItem13 = wx.MenuItem( self.m_menu11, 36, u"Wyczyść listę", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem13.SetBitmap( wx.Bitmap( u"icon/clear16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.AppendItem( self.m_menuItem13 )
        
        self.m_menuItem14 = wx.MenuItem( self.m_menu11, 37, u"Wyświetl publikację", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem14.SetBitmap( wx.Bitmap( u"icon/browser16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.AppendItem( self.m_menuItem14 )
        
        self.m_menuItem15 = wx.MenuItem( self.m_menu11, 38, u"Wyświetl cytowania", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem15.SetBitmap( wx.Bitmap( u"icon/globe16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.AppendItem( self.m_menuItem15 )
        
        self.m_menuItem16 = wx.MenuItem( self.m_menu11, 39, u"Połącz publikacje", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem16.SetBitmap( wx.Bitmap( u"icon/cite16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.AppendItem( self.m_menuItem16 )
        
        self.m_menu3.AppendSubMenu( self.m_menu11, u"Edycja" )
        
        self.m_menu31 = wx.Menu()
        self.m_menuItem17 = wx.MenuItem( self.m_menu31, 40, u"Generuj HTML", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem17.SetBitmap( wx.Bitmap( u"icon/www16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu31.AppendItem( self.m_menuItem17 )
        
        self.m_menuItem18 = wx.MenuItem( self.m_menu31, 41, u"Generuj Bibtex", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem18.SetBitmap( wx.Bitmap( u"icon/txt16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu31.AppendItem( self.m_menuItem18 )
        
        self.m_menu3.AppendSubMenu( self.m_menu31, u"Generowanie" )
        
        self.m_menu3.AppendSeparator()
        
        self.m_menuItem26 = wx.MenuItem( self.m_menu3, 43, u"Utwórz kopie", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem26.SetBitmap( wx.Bitmap( u"icon/backup16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu3.AppendItem( self.m_menuItem26 )
        
        self.m_menuItem27 = wx.MenuItem( self.m_menu3, 44, u"Wczytaj kopie", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem27.SetBitmap( wx.Bitmap( u"icon/replace16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu3.AppendItem( self.m_menuItem27 )
        
        self.m_menubar1.Append( self.m_menu3, u"Baza danych" ) 
        
        self.m_menu5 = wx.Menu()
        self.m_menuItem19 = wx.MenuItem( self.m_menu5, 42, u"O Programie", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem19.SetBitmap( wx.Bitmap( u"icon/about16.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.AppendItem( self.m_menuItem19 )
        
        self.m_menubar1.Append( self.m_menu5, u"Pomoc" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        self.m_toolBar1 = self.CreateToolBar( wx.TB_FLAT|wx.TB_HORIZONTAL, wx.ID_ANY ) 
        stool = self.m_toolBar1.AddLabelTool( 1, u"tool", wx.Bitmap( u"icon/search.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, u'Wyszukiwarka', wx.EmptyString ) 
        btool = self.m_toolBar1.AddLabelTool( 2, u"tool", wx.Bitmap( u"icon/base.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, u'Baza dancyh', wx.EmptyString ) 
        self.m_toolBar1.AddSeparator()
        addaut = self.m_toolBar1.AddLabelTool( 3, u"tool", wx.Bitmap( u"icon/autor.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Zarządzanie Autorami', wx.EmptyString ) 
        addgru = self.m_toolBar1.AddLabelTool( 4, u"tool", wx.Bitmap( u"icon/grupa.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Zarządzanie Grupami', wx.EmptyString ) 
        addpub = self.m_toolBar1.AddLabelTool( 5, u"tool", wx.Bitmap( u"icon/pub.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Zarządzanie Publikacjami', wx.EmptyString ) 
        addwyd = self.m_toolBar1.AddLabelTool( 6, u"tool", wx.Bitmap( u"icon/journal.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Zarządzanie Wydawcami', wx.EmptyString ) 
        self.m_toolBar1.AddSeparator()
        backup = self.m_toolBar1.AddLabelTool( 21, u"tool", wx.Bitmap( u"icon/backup.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Utworzenie kopii zapasowej bazy danych', wx.EmptyString ) 
        replace = self.m_toolBar1.AddLabelTool( 22, u"tool", wx.Bitmap( u"icon/replace.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Wczytanie kopii zapasowej bazy danych', wx.EmptyString ) 
        self.m_toolBar1.AddSeparator()
        raport = self.m_toolBar1.AddLabelTool( 7, u"tool", wx.Bitmap( u"icon/fileopen.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Wczytaj pobrane publikacje', wx.EmptyString ) 
        backlist = self.m_toolBar1.AddLabelTool( 8, u"tool", wx.Bitmap( u"icon/back.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Przywróć ostatnie publikacje', wx.EmptyString ) 
        clear = self.m_toolBar1.AddLabelTool( 9, u"tool", wx.Bitmap( u"icon/clear.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Wyczyść listę publikacji', wx.EmptyString ) 
        addrec = self.m_toolBar1.AddLabelTool( 10, u"tool", wx.Bitmap( u"icon/add.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Edytuj i Zapisz wybrane publikacje', wx.EmptyString ) 
        addrecm = self.m_toolBar1.AddLabelTool( 11, u"tool", wx.Bitmap( u"icon/addm.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Dodaj wszystkie wybrane publikacje', wx.EmptyString ) 
        viewpub = self.m_toolBar1.AddLabelTool( 12, u"tool", wx.Bitmap( u"icon/browser.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Wyświetl wybrane publikacje', wx.EmptyString ) 
        self.m_toolBar1.AddSeparator()
        editrec = self.m_toolBar1.AddLabelTool( 13, u"tool", wx.Bitmap( u"icon/edit.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Edytuj wybrane publikacje w bazie', wx.EmptyString ) 
        delrec = self.m_toolBar1.AddLabelTool( 14, u"tool", wx.Bitmap( u"icon/delete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Usuń wybrane publikacje z bazy', wx.EmptyString ) 
        clearbase = self.m_toolBar1.AddLabelTool( 15, u"tool", wx.Bitmap( u"icon/clear.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Wyczyść listę publikacji', wx.EmptyString ) 
        viewpubbase = self.m_toolBar1.AddLabelTool( 16, u"tool", wx.Bitmap( u"icon/browser.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Wyświetl wybrane publikacje', wx.EmptyString ) 
        viewcitbase = self.m_toolBar1.AddLabelTool( 17, u"tool", wx.Bitmap( u"icon/globe.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Wyświetl cytowania wybranych publikacji', wx.EmptyString ) 
        cit = self.m_toolBar1.AddLabelTool( 18, u"tool", wx.Bitmap( u"icon/cite.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Zarządzanie/Łączenie wybranych publikacji', wx.EmptyString ) 
        self.m_toolBar1.AddSeparator()
        gh = self.m_toolBar1.AddLabelTool( 19, u"tool", wx.Bitmap( u"icon/www.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Generowanie pliku HTML z wybranych publikacji', wx.EmptyString ) 
        gb = self.m_toolBar1.AddLabelTool( 20, u"tool", wx.Bitmap( u"icon/txt.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u'Generowanie pliku Bibtex z wybranych publikacji', wx.EmptyString ) 
        
        self.m_toolBar1.Realize()
        
        self.Centre( wx.BOTH )
        
        ## Visibility
        self.m_toolBar1.EnableTool(13, False)
        self.m_toolBar1.EnableTool(14, False)
        self.m_toolBar1.EnableTool(15, False)
        self.m_toolBar1.EnableTool(16, False)
        self.m_toolBar1.EnableTool(17, False)
        self.m_toolBar1.EnableTool(18, False)
        self.m_toolBar1.EnableTool(19, False)
        self.m_toolBar1.EnableTool(20, False)
#        self.m_toolBar1.EnableTool(21, False)
        self.m_menu11.Enable(34, False)
        self.m_menu11.Enable(35, False)
        self.m_menu11.Enable(36, False)
        self.m_menu11.Enable(37, False)
        self.m_menu11.Enable(38, False)
        self.m_menu11.Enable(39, False)
        self.m_menu31.Enable(40, False)
        self.m_menu31.Enable(41, False)
        
        ##Bindowanie
        ##Menubar
        ##Panele
        self.Bind(wx.EVT_MENU, self.SearchPanel, self.m_menuItem1)
        self.Bind(wx.EVT_MENU, self.BasePanel, self.m_menuItem2)
        self.Bind(wx.EVT_MENU, self.Close, self.m_menuItem6)
        
        ##Baza danych
        self.Bind(wx.EVT_MENU, self.onAddPub, self.m_menuItem9)
        self.Bind(wx.EVT_MENU, self.onAddGroup, self.m_menuItem8)
        self.Bind(wx.EVT_MENU, self.onAddJournal, self.m_menuItem10)
        self.Bind(wx.EVT_MENU, self.onEditAuthor, self.m_menuItem7)
        ##Edycja
        self.Bind(wx.EVT_MENU, self.EditDataBase, self.m_menuItem11)
        self.Bind(wx.EVT_MENU, self.DeleteMultiDataBase, self.m_menuItem12)
        self.Bind(wx.EVT_MENU, self.ClearDataBase, self.m_menuItem13)
        self.Bind(wx.EVT_MENU, self.OpenBaseLink, self.m_menuItem14)
        self.Bind(wx.EVT_MENU, self.OpenBaseCiteLink, self.m_menuItem15)
        self.Bind(wx.EVT_MENU, self.GetCit, self.m_menuItem16)
        ##Generowanie
        self.Bind(wx.EVT_MENU, self.GHtml, self.m_menuItem17)
        self.Bind(wx.EVT_MENU, self.GBibtex, self.m_menuItem18)
        ##Kopia bazy
        self.Bind(wx.EVT_MENU, self.saveDatabase, self.m_menuItem26)
        self.Bind(wx.EVT_MENU, self.GetDatabase, self.m_menuItem27)
        
        ##Wyszukiwanie
        self.Bind(wx.EVT_MENU, self.GetRaport, self.m_menuItem20)
        self.Bind(wx.EVT_MENU, self.BackList, self.m_menuItem21)
        self.Bind(wx.EVT_MENU, self.ClearDataSearch, self.m_menuItem22)
        self.Bind(wx.EVT_MENU, self.AddOneData, self.m_menuItem23)
        self.Bind(wx.EVT_MENU, self.AddMultiData, self.m_menuItem24)
        self.Bind(wx.EVT_MENU, self.OpenBrowserLink, self.m_menuItem25)
        
        ##O programie
        self.Bind(wx.EVT_MENU, self.viewAbout, self.m_menuItem19)
        
        ##Toolbar
        ## Panele
        self.Bind( wx.EVT_TOOL, self.SearchPanel, stool )
        self.Bind( wx.EVT_TOOL, self.BasePanel, btool )
        
        ##Edycja wartosci w bazie
        self.Bind( wx.EVT_TOOL, self.onAddPub, addpub ) #zarzadzanie publikacjami
        self.Bind( wx.EVT_TOOL, self.onAddGroup, addgru ) #zarzadzanie grupami
        self.Bind( wx.EVT_TOOL, self.onAddJournal, addwyd ) #zarzadzanie wydawcami
        self.Bind( wx.EVT_TOOL, self.onEditAuthor, addaut ) #zarzadzanie autorami
        
        ##Narzedzia dla wyszukiwania
        self.Bind( wx.EVT_TOOL, self.AddOneData, addrec ) #dodawanie jednego rekordu
        self.Bind( wx.EVT_TOOL, self.AddMultiData, addrecm ) #dodawanie wielu rekordów
        self.Bind( wx.EVT_TOOL, self.ClearDataSearch, clear ) #czyszczenie lsity
        self.Bind( wx.EVT_TOOL, self.BackList, backlist ) #przywracanie ostatnio pobranej listy
        self.Bind( wx.EVT_TOOL, self.OpenBrowserLink, viewpub ) #wyswietla publikacje w przegladarce
        self.Bind( wx.EVT_TOOL, self.GetRaport, raport )
        
        ##Narzedzia dla bazy dancyh
        self.Bind( wx.EVT_TOOL, self.DeleteMultiDataBase, delrec ) #usuwanie zaznaczonych rekordow
        self.Bind( wx.EVT_TOOL, self.ClearDataBase, clearbase ) #czyszczenie listy
        self.Bind( wx.EVT_TOOL, self.EditDataBase, editrec ) #edytowanie wybranych rekordów
        self.Bind( wx.EVT_TOOL, self.OpenBaseLink, viewpubbase ) #otwieranie publikacji w przegladarce
        self.Bind( wx.EVT_TOOL, self.GetCit, cit ) #otwieranie menadzera łaczenia publikacji
        self.Bind( wx.EVT_TOOL, self.OpenBaseCiteLink, viewcitbase ) #otwieranie cytowan w przegladarce
        self.Bind( wx.EVT_TOOL, self.GHtml, gh ) #generowanie html
        self.Bind( wx.EVT_TOOL, self.GBibtex, gb ) #generowanie bibtex
        self.Bind( wx.EVT_TOOL, self.saveDatabase, backup )
        self.Bind( wx.EVT_TOOL, self.GetDatabase, replace )
    
    def change_statusbar(self, msg):
        self.statusbar.SetStatusText(msg.data)
    
    def viewAbout(self, event):
        dlg = About()
        dlg.ShowModal()
    
    def GetDatabase(self, event):
        self.panel_baz.getBackUpBase()
    
    def saveDatabase(self, event):
        self.panel_baz.backUpBase()
    
    def GHtml(self, event):
        self.panel_baz.generateHtml()
    
    def GBibtex(self, event):
        self.panel_baz.generateBibtex()
    
    def GetCit(self, event):
        self.panel_baz.getCitPub()
    
    def GetRaport(self, event):
        self.panel_sch.getRaport()
    
    def AddOneData(self, event):
        self.panel_sch.addOneRecord()
    
    def AddMultiData(self, event):
        self.panel_sch.addMultiRecord()
    
    def DeleteMultiDataBase(self, event):
        self.panel_baz.deleteChoices()
    
    def ClearDataBase(self, event):
        self.panel_baz.dataList.DeleteAllItems()
    
    def ClearDataSearch(self, event):
        self.panel_sch.dataList.DeleteAllItems()
    
    def EditDataBase(self, event):
        self.panel_baz.editRecordData()
    
    def BackList(self, event):
        self.panel_sch.backList()
    
    def OpenBrowserLink(self, event):
        self.panel_sch.openLink()
    
    def OpenBaseLink(self, event):
        self.panel_baz.openLink()
    
    def OpenBaseCiteLink(self, event):
        self.panel_baz.openCite()
    
    def SearchPanel(self, event):
        if self.panel_baz.IsShown():
#            self.panel_men.Hide()
            self.panel_baz.Hide()
            self.panel_sch.Show()
            self.m_menu2.Enable(24, True)
            self.m_menu2.Enable(25, True)
            self.m_menu2.Enable(26, True)
            self.m_menu2.Enable(27, True)
            self.m_menu2.Enable(28, True)
            self.m_menu2.Enable(29, True)
            self.m_toolBar1.EnableTool(7, True)
            self.m_toolBar1.EnableTool(8, True)
            self.m_toolBar1.EnableTool(9, True)
            self.m_toolBar1.EnableTool(10, True)
            self.m_toolBar1.EnableTool(11, True)
            self.m_toolBar1.EnableTool(12, True)
            self.m_menu11.Enable(34, False)
            self.m_menu11.Enable(35, False)
            self.m_menu11.Enable(36, False)
            self.m_menu11.Enable(37, False)
            self.m_menu11.Enable(38, False)
            self.m_menu11.Enable(39, False)
            self.m_menu31.Enable(40, False)
            self.m_menu31.Enable(41, False)
            self.m_toolBar1.EnableTool(13, False)
            self.m_toolBar1.EnableTool(14, False)
            self.m_toolBar1.EnableTool(15, False)
            self.m_toolBar1.EnableTool(16, False)
            self.m_toolBar1.EnableTool(17, False)
            self.m_toolBar1.EnableTool(18, False)
            self.m_toolBar1.EnableTool(19, False)
            self.m_toolBar1.EnableTool(20, False)
#            self.m_toolBar1.EnableTool(21, False)
        self.Layout()
    
    def BasePanel(self, event):
        if self.panel_sch.IsShown():
#            self.panel_men.Hide()
            self.panel_sch.Hide()
            self.panel_baz.Show()
            self.m_menu2.Enable(24, False)
            self.m_menu2.Enable(25, False)
            self.m_menu2.Enable(26, False)
            self.m_menu2.Enable(27, False)
            self.m_menu2.Enable(28, False)
            self.m_menu2.Enable(29, False)
            self.m_toolBar1.EnableTool(7, False)
            self.m_toolBar1.EnableTool(8, False)
            self.m_toolBar1.EnableTool(9, False)
            self.m_toolBar1.EnableTool(10, False)
            self.m_toolBar1.EnableTool(11, False)
            self.m_toolBar1.EnableTool(12, False)
            self.m_menu11.Enable(34, True)
            self.m_menu11.Enable(35, True)
            self.m_menu11.Enable(36, True)
            self.m_menu11.Enable(37, True)
            self.m_menu11.Enable(38, True)
            self.m_menu11.Enable(39, True)
            self.m_menu31.Enable(40, True)
            self.m_menu31.Enable(41, True)
            self.m_toolBar1.EnableTool(13, True)
            self.m_toolBar1.EnableTool(14, True)
            self.m_toolBar1.EnableTool(15, True)
            self.m_toolBar1.EnableTool(16, True)
            self.m_toolBar1.EnableTool(17, True)
            self.m_toolBar1.EnableTool(18, True)
            self.m_toolBar1.EnableTool(19, True)
            self.m_toolBar1.EnableTool(20, True)
        self.Layout()
    
    def onAddPub(self, event):
        dlg = PubDialog()
        dlg.ShowModal()
        dlg.Destroy()
    
    def onAddGroup(self, event):
        dlg = GroupDialog()
        dlg.ShowModal()
        dlg.Destroy()
        self.panel_sch.updateGroupName()
    
    def onAddJournal(self, event):
        dlg = JourDialog()
        dlg.ShowModal()
        dlg.Destroy()
    
    def onEditAuthor(self, event):
        dlg = AuthorDialog()
        dlg.ShowModal()
        dlg.Destroy()
        self.panel_sch.updateAutorName()
    
    def Close(self, event):
        self.Destroy()
    
if __name__ == "__main__":
    app = wx.App(False)
    controller = MainFrame()
    controller.Show()
    app.MainLoop()
