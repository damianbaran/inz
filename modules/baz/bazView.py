# -*- coding: utf-8 -*-
import wx
import wx.lib.mixins.listctrl as listmix
import cDatabase


class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class bView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        self.session = cDatabase.connectDatabase()

        ########################################################################
        #  Panel 1
        ########################################################################
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
        
        
        oneBox1.Add( oneBox11, 1, wx.EXPAND|wx.ALL, 5 )
        
        oneBox12 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Dodaj grupe" ), wx.VERTICAL )
        
        bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText18 = wx.StaticText( self.panel, wx.ID_ANY, u"Grupa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        bSizer30.Add( self.m_staticText18, 0, wx.ALL, 5 )
        
        self.m_textCtrl9 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer30.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
        
        
        sbSizer5.Add( bSizer30, 1, wx.EXPAND, 5 )
        
        bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText19 = wx.StaticText( self.panel, wx.ID_ANY, u"Użytkownicy:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        bSizer32.Add( self.m_staticText19, 0, wx.ALL, 5 )
        
        m_checkList1Choices = self.printList()
        self.m_checkList1 = wx.CheckListBox( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
        bSizer32.Add( self.m_checkList1, 1, wx.ALL, 5 )
        
        
        sbSizer5.Add( bSizer32, 1, wx.EXPAND, 5 )
        
        bSizer39 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button8 = wx.Button( self.panel, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer39.Add( self.m_button8, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        
        sbSizer5.Add( bSizer39, 1, wx.EXPAND, 5 )
        
        
        oneBox12.Add( sbSizer5, 1, wx.EXPAND, 5 )
        
        
        oneBox1.Add( oneBox12, 1, wx.EXPAND|wx.ALL, 5 )
        
        bSizer38 = wx.BoxSizer( wx.VERTICAL )
        
        
        oneBox1.Add( bSizer38, 1, wx.EXPAND, 5 )
        
        
        globalBox.Add( oneBox1, 0, wx.EXPAND, 5 )
        
        
        self.panel.SetSizer( globalBox )
        self.panel.Layout()
        globalBox.Fit( self.panel )
        globalBox.Fit( self.panel ) 
        
        #############################################################
        ## Bindowanie
        #############################################################
        
        self.m_button8.Bind(wx.EVT_BUTTON, self.getDataGroup)
        
    def printList(self):
        """Funkcja pobiera dane z bazy, i wyswietla w checklistbox.
        id, imie i nazwisko autorow"""
        t = cDatabase.getAllRecord(self.session)
        return t
    
    def getDataGroup(self,  event):
        """Funkcja pobiera dane do utworzenia grupy z kontrolek"""
        result = []
        gname = self.m_textCtrl9.GetValue()
        guser = self.printList()
        for i in range(len(guser)):
            if self.m_checkList1.IsChecked(i):
                tmp = guser[i].split(' ')
                id = tmp[0]
                l = (id,  gname)
                result.append(l)
#        print result
        cDatabase.addGroup(self.session, result)
