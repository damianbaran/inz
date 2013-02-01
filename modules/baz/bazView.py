# -*- coding: utf-8 -*-
import wx
import wx.lib.mixins.listctrl as listmix
import cDatabase
from publikacja import PubDialog
from grupa import GroupDialog
from wydawca import JourDialog


class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class bView(wx.Panel, PubDialog):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        self.session = cDatabase.connectDatabase()
        listSearch = [u'Autor', u'Tytuł', u'Rok', u'Wydawca']

        ########################################################################
        #  Panel 1
        ########################################################################
        self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        globalBox = wx.BoxSizer( wx.VERTICAL )
        
        twoBox1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText12 = wx.StaticText( self.panel, wx.ID_ANY, u"Wyszukaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer24.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice31Choices = listSearch
        self.m_choice31 = wx.Choice( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice31Choices, 0 )
        self.m_choice31.SetSelection( 0 )
        bSizer24.Add( self.m_choice31, 0, wx.ALL, 5 )
        
        self.m_searchCtrl1 = wx.SearchCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.m_searchCtrl1.ShowSearchButton( True )
        self.m_searchCtrl1.ShowCancelButton( False )
        bSizer24.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )
        
        
        twoBox1.Add( bSizer24, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )
        
        twoBox11 = wx.BoxSizer( wx.VERTICAL )
        
#        self.dataList = wx.ListCtrl( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_ICON )
        self.dataList = TestListCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 995,490 ), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, '', format=wx.LIST_FORMAT_CENTER, width=25)
        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=70)
        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=320)
        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=180)
        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=120)
        twoBox11.Add( self.dataList, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        
        twoBox1.Add( twoBox11, 1, wx.EXPAND, 5 )
        
        twoBox12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.but5 = wx.Button( self.panel, wx.ID_ANY, u"Dodaj wybrane", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        twoBox12.Add( self.but5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.RIGHT, 5 )
        
        self.but6 = wx.Button( self.panel, wx.ID_ANY, u"Przywróć liste", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.but6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        twoBox12.Add( self.but6, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.RIGHT, 5 )
        
        
        twoBox1.Add( twoBox12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        globalBox.Add( twoBox1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.panel.SetSizer( globalBox )
        self.panel.Layout()
        globalBox.Fit( self.panel )
        
        #############################################################
        ## Bindowanie
        #############################################################
        
        self.m_searchCtrl1.Bind(wx.EVT_TEXT_ENTER, self.test)
        
    def test(self,  event):
        t = self.m_searchCtrl1.GetValue()
        d = self.m_choice31.GetStringSelection()
        tmp = cDatabase.getRecords(self.session, d, t)
        self.updateRecord(tmp)
    
    def updateRecord(self, data):
        """
        """
        try:
            for i in range(len(data)):
                self.dataList.Append(data[i])
        except TypeError:
            wx.MessageBox(u'Brak wyszukanych danych', 'Brak danych', wx.OK | wx.ICON_INFORMATION)      

