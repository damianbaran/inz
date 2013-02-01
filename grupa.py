# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import cDatabase

###########################################################################
## Class GroupDialog
###########################################################################

class GroupDialog ( wx.Dialog ):
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Dodawanie grup i uzytkowników", pos = wx.DefaultPosition, size = wx.Size( 300,350 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dodaj Grupę", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.EXPAND|wx.ALL, 5 )        
        
        
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Grupa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox1Choices = self.printGroupList()
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size( 230,-1 ), m_comboBox1Choices, 0 )
        bSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Autorzy:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer10.Add( self.m_staticText9, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        m_checkList3Choices = self.printList()
        self.m_checkList3 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), m_checkList3Choices, 0 )
        bSizer10.Add( self.m_checkList3, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"Sprawdź", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button5, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Zamknij", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button4, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_button1.Bind(wx.EVT_BUTTON, self.setDataGroup)
        self.m_button5.Bind(wx.EVT_BUTTON, self.checkDataGroup)
        self.m_button4.Bind(wx.EVT_BUTTON, self.close)
        
    def __del__( self ):
        pass
    
    def printList(self):
        """Funkcja pobiera dane z bazy i wyswietla w checklistbox.
        id, imie i nazwisko autorow"""
        t = cDatabase.getAllRecord(self.session)
        return t
    
    def printGroupList(self):
        t = cDatabase.getGroupName(self.session)
        return t
    
    def setDataGroup(self,  event):
        """Funkcja pobiera dane do utworzenia grupy widoku bazy danych"""
        result = []
        gname = self.m_comboBox1.GetValue()
        guser = self.printList()
        for i in range(len(guser)):
            if self.m_checkList3.IsChecked(i):
                tmp = guser[i].split(' ')
                id = tmp[0]
                l = (id,  gname)
                result.append(l)
                
        if gname != '' or len(result) != 0:
            cDatabase.addGroup(self.session, result)
        else:
            wx.MessageBox(u'Nie podana nazwy grupy \nlub nie wybrano autorów.', u'Bład', wx.OK | wx.ICON_INFORMATION)   
        
        self.m_comboBox1.SetValue('')
        for i in range(len(guser)):
            self.m_checkList3.Check(i,  False)
    
    def checkDataGroup(self, event):
        alluser = self.printList()
        for i in range(len(alluser)):
            self.m_checkList3.Check(i,  False)
        
        gname = self.m_comboBox1.GetValue()
        guser = cDatabase.getCheckedUser(self.session, gname)
        for i in range(len(guser)):
            self.m_checkList3.Check(guser[i]-1)
        
    def close(self, event):
        self.Destroy()
