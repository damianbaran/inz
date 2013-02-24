# -*- coding: utf-8 -*-

import wx
from modules.sch.schView import sView
from modules.men.menView import mView
from modules.baz.bazView import bView
from publikacja import PubDialog
from grupa import GroupDialog
from wydawca import JourDialog
from autor import AuthorDialog
from wx.lib.pubsub import Publisher

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id = wx.ID_ANY, title = u"Wyszukiwarka Publikacji", pos = wx.DefaultPosition, size = wx.Size( 1020,640 ), style = wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX) )
        
        self.panel_sch = sView(self)
        self.panel_men = mView(self)
        self.panel_baz = bView(self)
        self.panel_men.Hide()
        self.panel_baz.Hide()
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        firstSizer = wx.BoxSizer( wx.VERTICAL )
        
        firstSizer.Add(self.panel_sch, 1, wx.EXPAND)
        firstSizer.Add(self.panel_men, 1, wx.EXPAND)
        firstSizer.Add(self.panel_baz, 1, wx.EXPAND)
        
        self.SetSizer( firstSizer )
        self.Layout()
        self.statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        Publisher().subscribe(self.change_statusbar, 'change_statusbar')
        self.menubar = wx.MenuBar( 0 )
        self.menu1 = wx.Menu()
        
        self.item1 = wx.MenuItem( self.menu1, wx.ID_ANY, u"Wyszukiwarka", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu1.AppendItem( self.item1 )
        self.Bind(wx.EVT_MENU, self.SearchPanel, self.item1)
    
#        self.item2 = wx.MenuItem( self.menu1, wx.ID_ANY, u"Menadżer Publikacji", wx.EmptyString, wx.ITEM_NORMAL )
#        self.menu1.AppendItem( self.item2 )
#        self.Bind(wx.EVT_MENU, self.ManagePanel, self.item2)
        
        self.item3 = wx.MenuItem( self.menu1, wx.ID_ANY, u"Baza danych", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu1.AppendItem( self.item3 )
        self.Bind(wx.EVT_MENU, self.BasePanel, self.item3)
        
        
        self.menu1.AppendSeparator()
        
        self.item3 = wx.MenuItem( self.menu1, wx.ID_ANY, u"Wyjdź", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu1.AppendItem( self.item3 )
        
        self.menubar.Append( self.menu1, u"Widok" ) 
        
        self.menu2 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.menu2, wx.ID_ANY, u"Dodaj Publikację", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu2.AppendItem( self.m_menuItem5 )
        self.Bind(wx.EVT_MENU, self.onAddPub, self.m_menuItem5)
        
        self.m_menuItem6 = wx.MenuItem( self.menu2, wx.ID_ANY, u"Dodaj/Edytuj Grupę", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu2.AppendItem( self.m_menuItem6 )
        self.Bind(wx.EVT_MENU, self.onAddGroup, self.m_menuItem6)
        
        self.m_menuItem7 = wx.MenuItem( self.menu2, wx.ID_ANY, u"Dodaj/Edytuj Wydawcę", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu2.AppendItem( self.m_menuItem7 )
        self.Bind(wx.EVT_MENU, self.onAddJournal, self.m_menuItem7)
        
        self.m_menuItem10 = wx.MenuItem( self.menu2, wx.ID_ANY, u"Edytuj Autora", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu2.AppendItem( self.m_menuItem10 )
        self.Bind(wx.EVT_MENU, self.onEditAuthor, self.m_menuItem10)
        
        self.menubar.Append( self.menu2, u"Baza danych" ) 
        
        self.menu3 = wx.Menu()
        self.m_menuItem8 = wx.MenuItem( self.menu3, wx.ID_ANY, u"Pomoc", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu3.AppendItem( self.m_menuItem8 )
        
        self.m_menuItem9 = wx.MenuItem( self.menu3, wx.ID_ANY, u"O Programie", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu3.AppendItem( self.m_menuItem9 )
        
        self.menubar.Append( self.menu3, u"Pomoc" ) 
        
        self.SetMenuBar( self.menubar )
        
        self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL|wx.TB_FLAT ) 
#        self.m_toolBar1.AddSeparator()
        
        self.stool = self.m_toolBar1.AddLabelTool( 1, u"tool", wx.Bitmap( u"search.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, u"Wyszukiwarka", wx.EmptyString, None ) 
#        mtool = self.m_toolBar1.AddLabelTool( 2, u"tool", wx.Bitmap( u"stock_home.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, u"Menadżer Publikacji", wx.EmptyString, None )
        btool = self.m_toolBar1.AddLabelTool( 3, u"tool", wx.Bitmap( u"file-manager.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, u"Baza danych", wx.EmptyString, None ) 
        self.m_toolBar1.AddSeparator()
        
        addpub = self.m_toolBar1.AddLabelTool( 4, u"tool", wx.Bitmap( u"gnome-applications.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Dodaj/Usuń Publikację", wx.EmptyString, None ) 
        addgru = self.m_toolBar1.AddLabelTool( 5, u"tool", wx.Bitmap( u"grupa.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Dodaj/Edytuj/Usuń Grupę", wx.EmptyString, None ) 
        addwyd = self.m_toolBar1.AddLabelTool( 6, u"tool", wx.Bitmap( u"applications-graphics.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Dodaj/Edytuj Wydawcę", wx.EmptyString, None ) 
        addaut = self.m_toolBar1.AddLabelTool( 7, u"tool", wx.Bitmap( u"autor.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Edytuj/Usuń Autora", wx.EmptyString, None ) 
        self.m_toolBar1.AddSeparator()
        
        addrec = self.m_toolBar1.AddLabelTool( 8, u"tool", wx.Bitmap( u"add.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Edytuj i dodaj wybrane reokordy do bazy", wx.EmptyString, None ) 
        addrecm = self.m_toolBar1.AddLabelTool( 9, u"tool", wx.Bitmap( u"addm.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Dodaj wybrane rekordy do bazy", wx.EmptyString, None ) 
        viewpub = self.m_toolBar1.AddLabelTool( 10, u"tool", wx.Bitmap( u"browser.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Wyświetl publikację", wx.EmptyString, None ) 
        clear = self.m_toolBar1.AddLabelTool( 11, u"tool", wx.Bitmap( u"clear.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Czyść listę z publikacjami", wx.EmptyString, None ) 
        backlist = self.m_toolBar1.AddLabelTool( 12, u"tool", wx.Bitmap( u"back.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Przywróć ostatnio pobrane rekordy", wx.EmptyString, None ) 
        raport = self.m_toolBar1.AddLabelTool( 17, u"tool", wx.Bitmap( u"fileopen.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Wczytaj wyszukane już rekordy", wx.EmptyString, None ) 
        self.m_toolBar1.AddSeparator()
        
        editrec = self.m_toolBar1.AddLabelTool( 13, u"tool", wx.Bitmap( u"edit.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Edytuj wybrany rekord w bazie", wx.EmptyString, None ) 
        delrec = self.m_toolBar1.AddLabelTool( 14, u"tool", wx.Bitmap( u"delete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Usuń wybrane rekordy z bazy", wx.EmptyString, None ) 
        viewpubbase = self.m_toolBar1.AddLabelTool( 15, u"tool", wx.Bitmap( u"browser.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Wyświetl publikację", wx.EmptyString, None ) 
        clearbase = self.m_toolBar1.AddLabelTool( 16, u"tool", wx.Bitmap( u"clear.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Czyść listę z publikacjami", wx.EmptyString, None ) 
        viewcitbase = self.m_toolBar1.AddLabelTool( 18, u"tool", wx.Bitmap( u"globe.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Wyświetl cytowania", wx.EmptyString, None ) 
        cit = self.m_toolBar1.AddLabelTool( 19, u"tool", wx.Bitmap( u"cite.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Łacz wybrane publikacje", wx.EmptyString, None ) 
        
        self.m_toolBar1.Realize() 
        
        
        self.Centre( wx.BOTH )
        self.m_toolBar1.EnableTool(13, False)
        self.m_toolBar1.EnableTool(14, False)
        self.m_toolBar1.EnableTool(15, False)
        self.m_toolBar1.EnableTool(16, False)
        self.m_toolBar1.EnableTool(18, False)
        self.m_toolBar1.EnableTool(19, False)
        
        ## Panele
        self.Bind( wx.EVT_TOOL, self.SearchPanel, self.stool )
        self.Bind( wx.EVT_TOOL, self.BasePanel, btool )
        
        ##Edycja wartosci w bazie
        self.Bind( wx.EVT_TOOL, self.onAddPub, addpub )
        self.Bind( wx.EVT_TOOL, self.onAddGroup, addgru )
        self.Bind( wx.EVT_TOOL, self.onAddJournal, addwyd )
        self.Bind( wx.EVT_TOOL, self.onEditAuthor, addaut )
        
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
        self.Bind( wx.EVT_TOOL, self.GetCit, cit )
        self.Bind( wx.EVT_TOOL, self.OpenBaseCiteLink, viewcitbase )
    
    def change_statusbar(self, msg):
        self.statusbar.SetStatusText(msg.data)
    
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
        if self.panel_men.IsShown() or self.panel_baz.IsShown():
            self.panel_men.Hide()
            self.panel_baz.Hide()
            self.panel_sch.Show()
            self.m_toolBar1.EnableTool(8, True)
            self.m_toolBar1.EnableTool(9, True)
            self.m_toolBar1.EnableTool(10, True)
            self.m_toolBar1.EnableTool(11, True)
            self.m_toolBar1.EnableTool(12, True)
            self.m_toolBar1.EnableTool(17, True)
            self.m_toolBar1.EnableTool(13, False)
            self.m_toolBar1.EnableTool(14, False)
            self.m_toolBar1.EnableTool(15, False)
            self.m_toolBar1.EnableTool(16, False)
            self.m_toolBar1.EnableTool(18, False)
            self.m_toolBar1.EnableTool(19, False)
        self.Layout()
    
    def BasePanel(self, event):
        if self.panel_men.IsShown() or self.panel_sch.IsShown():
            self.panel_men.Hide()
            self.panel_sch.Hide()
            self.panel_baz.Show()
            self.m_toolBar1.EnableTool(8, False)
            self.m_toolBar1.EnableTool(9, False)
            self.m_toolBar1.EnableTool(10, False)
            self.m_toolBar1.EnableTool(11, False)
            self.m_toolBar1.EnableTool(12, False)
            self.m_toolBar1.EnableTool(17, False)
            self.m_toolBar1.EnableTool(13, True)
            self.m_toolBar1.EnableTool(14, True)
            self.m_toolBar1.EnableTool(15, True)
            self.m_toolBar1.EnableTool(16, True)
            self.m_toolBar1.EnableTool(18, True)
            self.m_toolBar1.EnableTool(19, True)
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
    
if __name__ == "__main__":
    app = wx.App(False)
    controller = MainFrame()
    controller.Show()
    app.MainLoop()
