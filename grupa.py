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
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Zarządzanie Grupami", pos = wx.DefaultPosition, size = wx.Size( 330,300 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dodawanie Grupy", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.EXPAND|wx.ALL, 5 )        
        
        
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Grupa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox1Choices = cDatabase.getGroupName(self.session)
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size( 230,-1 ), m_comboBox1Choices, 0 )
        bSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Autorzy:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer10.Add( self.m_staticText9, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        m_checkList3Choices = cDatabase.getUserName(self.session)
        self.m_checkList3 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), m_checkList3Choices, 0 )
        bSizer10.Add( self.m_checkList3, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button1, 0, wx.LEFT|wx.BOTTOM|wx.TOP, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"Zatwierdź", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button5, 0, wx.LEFT|wx.BOTTOM|wx.TOP, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Usuń", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button3, 0, wx.LEFT|wx.BOTTOM|wx.TOP, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Anuluj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button4, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_button5.Hide()
        self.m_button3.Hide()
        
###################################################
## Bind
###################################################
        
        self.m_button1.Bind(wx.EVT_BUTTON, self.addDataGroup)
        self.m_button5.Bind(wx.EVT_BUTTON, self.addDataGroup)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cancel)
        self.m_button3.Bind(wx.EVT_BUTTON, self.deleteGroupValue)
        self.m_comboBox1.Bind(wx.EVT_COMBOBOX, self.checkDataGroup)
        
###################################################
## Metody
###################################################
    
#    def printList(self):
#        """Funkcja pobiera dane z bazy i wyswietla w checklistbox.
#        id, imie i nazwisko autorow"""
#        t = cDatabase.getAllRecord(self.session)
#        return t
    
#    def printGroupList(self):
#        t = cDatabase.getGroupName(self.session)
#        return t

    def deleteGroupValue(self, event):
        """Usuwa grypy wraz z powiazanymi uzytkownikami"""
        
        #Pobiera wartosci z kontrolek
        gname = self.m_comboBox1.GetValue()
        
        #Sprawdza czy wybrana grupe
        if gname != '':
            cDatabase.delGroup(self.session, gname)
            wx.MessageBox(u'Pomyślnie usunięto grupę!', u'Sukces', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(u'Nie zaznaczono nazwy grupy!', u'Bład!', wx.OK | wx.ICON_INFORMATION)
        
        #Wyczyszczenie kontrolek
        self.clearData()
        
        self.m_staticText1.SetLabel(u'Dodawanie Grupy')
        self.m_button5.Hide()
        self.m_button3.Hide()
        self.m_button1.Show()
    
    def addDataGroup(self,  event):
        """Funkcja pobiera dane do utworzenia grupy widoku bazy danych"""
        
        #Pobieranie i deklaracji wartosci
        result = []
        gname = self.m_comboBox1.GetValue()
        
        #Usuwanie wszystkich powiazanych autorów z grupa
        guser = cDatabase.editUserGroup(self.session, gname)
        
        #Tworzenie listy nowych autorow dodanych do grupy
        guser = cDatabase.getUserName(self.session)
        t = cDatabase.getUserNameID(self.session)
        for i in range(len(guser)):
            if self.m_checkList3.IsChecked(i):
                tmp = guser[i].split(' ')
                id = t[guser[i]]
                l = (id,  gname)
                result.append(l)
        
        #Sprawdzanie czy wszystkie wymagane pola maja wartości
        if gname != '' and len(result) != 0:
            cDatabase.addGroup(self.session, result)
        else:
            wx.MessageBox(u'Nie podana nazwy grupy \nlub nie wybrano autorów.', u'Bład', wx.OK | wx.ICON_INFORMATION)
        
        #Wyczyszczenie kontrolek
        self.clearData()
        
        self.m_staticText1.SetLabel(u'Dodawanie Grupy')
        self.m_button5.Hide()
        self.m_button3.Hide()
        self.m_button1.Show()
    
    def checkDataGroup(self, event):
        """Sprawdza ktorzy autorzy sa powiazani z wybrana grupa"""
        
        #Czyszczenie wszystkich zaznaczeń
        alluser = cDatabase.getUserName(self.session)
        for i in range(len(alluser)):
            self.m_checkList3.Check(i,  False)
        
        #Zaznaczanie autorów dla wybranej grupy
        gname = self.m_comboBox1.GetValue()
        guser = cDatabase.getCheckedUser(self.session, gname)
        t = cDatabase.getUserNameID(self.session)
        d = t.values()
        d.sort()
        p = {}
        for i in range(len(d)):
            x = {d[i]:i}
            p.update(x)
        
        for i in range(len(guser)):
            y = p[guser[i]]
            self.m_checkList3.Check(y)
        
        self.m_staticText1.SetLabel(u'Edytowanie Grupy')
        self.m_button5.Show()
        self.m_button3.Show()
        self.m_button1.Hide()
    
    def clearData(self):
        """Czyści wszystkie kontrolki po wykonaniu zadania przez użytkownika"""
        
        #Czyszczenie kontrolkki z nazwami grup
        guser = cDatabase.getUserName(self.session)
        m_comboBox1Choices = cDatabase.getGroupName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
        
        #Czyszczenie zaznaczonych autorow
        self.m_comboBox1.SetValue('')
        for i in range(len(guser)):
            self.m_checkList3.Check(i,  False)
    
    def cancel(self, event):
        self.clearData()
        
        self.m_staticText1.SetLabel(u'Dodawanie Grupy')
        self.m_button5.Hide()
        self.m_button3.Hide()
        self.m_button1.Show()
        
        self.Destroy()
    
    def close(self, event):
        """Zamyka okienko z grupami"""
        self.Destroy()
        
if __name__ == "__main__":
    app = wx.App(False)
    controller = GroupDialog()
    controller.Show()
    app.MainLoop()
