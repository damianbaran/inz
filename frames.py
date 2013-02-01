# -*- coding: utf-8 -*-
import wx
from modules.sch.schView import sView
from modules.men.menView import mView
from modules.baz.bazView import bView
from publikacja import PubDialog
from grupa import GroupDialog
from wydawca import JourDialog

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id = wx.ID_ANY, title = u"Wyszukiwarka Publikacji", pos = wx.DefaultPosition, size = wx.Size( 1030,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
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
        self.statusbar.SetStatusText(u'Jesteś w panelu wyszukiwania publikacji')
        self.menubar = wx.MenuBar( 0 )
        self.menu1 = wx.Menu()
        
        self.item1 = wx.MenuItem( self.menu1, wx.ID_ANY, u"Wyszukiwarka", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu1.AppendItem( self.item1 )
        self.Bind(wx.EVT_MENU, self.SearchPanel, self.item1)
        		
        self.item2 = wx.MenuItem( self.menu1, wx.ID_ANY, u"Menadżer Publikacji", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu1.AppendItem( self.item2 )
        self.Bind(wx.EVT_MENU, self.ManagePanel, self.item2)
        
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
        		
        self.m_menuItem6 = wx.MenuItem( self.menu2, wx.ID_ANY, u"Dodaj Grupę", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu2.AppendItem( self.m_menuItem6 )
        self.Bind(wx.EVT_MENU, self.onAddGroup, self.m_menuItem6)
        		
        self.m_menuItem7 = wx.MenuItem( self.menu2, wx.ID_ANY, u"Dodaj Wydawcę", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu2.AppendItem( self.m_menuItem7 )
        self.Bind(wx.EVT_MENU, self.onAddJournal, self.m_menuItem7)
        		
        self.menubar.Append( self.menu2, u"Baza danych" ) 
        		
        self.menu3 = wx.Menu()
        self.m_menuItem8 = wx.MenuItem( self.menu3, wx.ID_ANY, u"Pomoc", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu3.AppendItem( self.m_menuItem8 )
        		
        self.m_menuItem9 = wx.MenuItem( self.menu3, wx.ID_ANY, u"O Programie", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu3.AppendItem( self.m_menuItem9 )
        		
        self.menubar.Append( self.menu3, u"Pomoc" ) 
        		
        self.SetMenuBar( self.menubar )
        		
        		
        self.Centre( wx.BOTH )
        
    def SearchPanel(self, event):
        if self.panel_men.IsShown() or self.panel_baz.IsShown():
            self.panel_men.Hide()
            self.panel_baz.Hide()
            self.panel_sch.Show()
            self.statusbar.SetStatusText(u'Jesteś w panelu wyszukiwania publikacji')
        self.Layout()
        
    def ManagePanel(self, event):
        if self.panel_sch.IsShown() or self.panel_baz.IsShown():
            self.panel_sch.Hide()
            self.panel_baz.Hide()
            self.panel_men.Show()
            self.statusbar.SetStatusText(u'Jesteś w menadżerze publikacji')
        self.Layout() 
        
    def BasePanel(self, event):
        if self.panel_men.IsShown() or self.panel_sch.IsShown():
            self.panel_men.Hide()
            self.panel_sch.Hide()
            self.panel_baz.Show()
            self.statusbar.SetStatusText(u'Jesteś w panelu zarzadzania baza')
        self.Layout()
        
    def onAddPub(self, event):
        dlg = PubDialog()
        dlg.ShowModal()
        dlg.Destroy()
        
    def onAddGroup(self, event):
        dlg = GroupDialog()
        dlg.ShowModal()
        dlg.Destroy()
        
    def onAddJournal(self, event):
        dlg = JourDialog()
        dlg.ShowModal()
        dlg.Destroy()
        
if __name__ == "__main__":
    app = wx.App(False)
    controller = MainFrame()
    controller.Show()
    app.MainLoop()
