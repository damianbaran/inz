# -*- coding: utf-8 -*-
import wx
import wx.lib.mixins.listctrl as listmix
from modules.men.menControler import mControler


class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class mView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        self.mcontrol = mControler()

        self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        globalBox = wx.BoxSizer( wx.VERTICAL )
        
        oneBox1 = wx.BoxSizer( wx.HORIZONTAL )
        
        oneBox11 = wx.BoxSizer( wx.VERTICAL )
        
        oneSB1 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Dodaj Publikacje" ), wx.VERTICAL )
        
        oneBox111 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt1 = wx.StaticText( self.panel, wx.ID_ANY, u"Tytył:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt1.Wrap( -1 )
        oneBox111.Add( self.txt1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl1 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox111.Add( self.ctrl1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox111, 0, wx.EXPAND, 5 )
        
        oneBox112 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt2 = wx.StaticText( self.panel, wx.ID_ANY, u"Imie:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt2.Wrap( -1 )
        oneBox112.Add( self.txt2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl2 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 200,20 ), 0 )
        oneBox112.Add( self.ctrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox112, 0, wx.EXPAND, 5 )
        
        oneBox113 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt3 = wx.StaticText( self.panel, wx.ID_ANY, u"Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )
        oneBox113.Add( self.txt3, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl3 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox113.Add( self.ctrl3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox113, 0, wx.EXPAND, 5 )
        
        oneBox114 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt4 = wx.StaticText( self.panel, wx.ID_ANY, u"Rok:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt4.Wrap( -1 )
        oneBox114.Add( self.txt4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl4 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox114.Add( self.ctrl4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox114, 0, wx.EXPAND, 5 )
        
        oneBox115 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt5 = wx.StaticText( self.panel, wx.ID_ANY, u"Wydawca:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt5.Wrap( -1 )
        oneBox115.Add( self.txt5, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl5 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox115.Add( self.ctrl5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox115, 0, wx.EXPAND, 5 )
        
        oneBox117 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.but1 = wx.Button( self.panel, wx.ID_ANY, u"Pobierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox117.Add( self.but1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox117, 0, wx.ALIGN_RIGHT, 5 )
        
        
        oneBox11.Add( oneSB1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneBox1.Add( oneBox11, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        globalBox.Add( oneBox1, 0, wx.EXPAND, 5 )
        
        twoBox1 = wx.BoxSizer( wx.VERTICAL )
        
        twoBox11 = wx.BoxSizer( wx.VERTICAL )
        
#        self.dataList = wx.ListCtrl( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_ICON )
        self.dataList = TestListCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,295 ), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, '', format=wx.LIST_FORMAT_CENTER, width=25)
        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=70)
        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=320)
        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=180)
        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=120)
        twoBox11.Add( self.dataList, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )
        
        
        twoBox1.Add( twoBox11, 1, wx.RIGHT|wx.EXPAND, 5 )
        
        twoBox12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.but5 = wx.Button( self.panel, wx.ID_ANY, u"Wyświetl wybrane", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        twoBox12.Add( self.but5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        self.but6 = wx.Button( self.panel, wx.ID_ANY, u"Przywróć liste", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.but6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        twoBox12.Add( self.but6, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        
        twoBox1.Add( twoBox12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        globalBox.Add( twoBox1, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )
        
        
        self.panel.SetSizer( globalBox )
        self.panel.Layout()
        globalBox.Fit( self.panel )
        
        ########################################################################
        #  Panel 2
        ########################################################################
        
        self.but5.Bind(wx.EVT_BUTTON, self.test)
        
    def test(self, event):
        self.dataList.DeleteAllItems()
        t = self.mcontrol.getRecords()
        self.updateRecord(t)
    
    def updateRecord(self, data):
        """
        """
        for i in range(len(data)):
            self.dataList.Append(data[i])
