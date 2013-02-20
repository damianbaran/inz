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
## Class PubDialog
###########################################################################

class PubDialog ( wx.Dialog ):
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Dodawanie i edycja publikacji", pos = wx.DefaultPosition, size = wx.Size( 350,350 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()
        listType = [u'Artykuł', u'Książka', u'Publikacja', u'Inne']
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dodaj Publikacje", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
    
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Tytuł:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer3.Add( self.m_textCtrl2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Autorzy:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer5.Add( self.m_staticText4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer5.Add( self.m_textCtrl4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Cytowania:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer4.Add( self.m_textCtrl3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Typ:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer6.Add( self.m_staticText5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice1Choices = listType
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer6.Add( self.m_choice1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Rok:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer7.Add( self.m_staticText6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer7.Add( self.m_textCtrl5, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"DOI:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer8.Add( self.m_staticText7, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer8.Add( self.m_textCtrl6, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer8, 0, wx.EXPAND, 5 )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Inny klucz:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer12.Add( self.m_staticText9, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer12.Add( self.m_textCtrl7, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer12, 0, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Wydawca:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer9.Add( self.m_staticText8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice2Choices = cDatabase.getJournalName(self.session)
        self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), m_choice2Choices, 0 )
#        self.m_choice2.SetSelection( 0 )
        bSizer9.Add( self.m_choice2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Powiąż z autorami:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer10.Add( self.m_staticText9, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        m_checkList3Choices = cDatabase.getUserName(self.session)
        self.m_checkList3 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), m_checkList3Choices, 0 )
        bSizer10.Add( self.m_checkList3, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Edytuj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Zamknij", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button4, 0, wx.ALL, 5 )
            
        
        bSizer1.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_button3.Hide()
        
###################################################
## Bind
###################################################
        
        self.m_button1.Bind(wx.EVT_BUTTON, self.addPubValue)
        self.m_button4.Bind(wx.EVT_BUTTON, self.close)
        self.m_button3.Bind(wx.EVT_BUTTON, self.editPubValue)
        
###################################################
## Metody
###################################################
    
    def editPubValue(self, event):
        """Edytowanie wybranej publikacji"""
        #Pobiera wartosci z kontrolek do edycji
        tmp = self.m_staticText1.GetLabel()
        tmp = tmp.split('. ', 1)
        t0 = tmp[1]
        t1 = self.m_textCtrl2.GetValue()
        t2 = self.m_textCtrl4.GetValue()
        t3 = self.m_textCtrl3.GetValue()
        t4 = self.m_choice1.GetStringSelection()
        t5 = self.m_textCtrl5.GetValue()
        t6 = self.m_textCtrl6.GetValue()
        t7 = self.m_textCtrl7.GetValue()
        t8 = self.m_choice2.GetStringSelection()
        
        #Odznacza już powiazanych autorów
#        ch = cDatabase.getCheckItemAuthor(self.session, t0)
        ch = cDatabase.editItemAuthor(self.session, t0)
#        for i in range(len(ch)):
#            self.m_checkList3.Check(ch[i]-1, False)
        
        t9 = self.getCheckUser()
        
        #Pobiera wartosci ID dla zaznaczonych autorów
        tmp = cDatabase.getJournalNameID(self.session)
        t8 = tmp[t8]
        
        t = (t1, t2, t3, t4, t5, t6, t7, t8, t9)
        
        #Sprawdzenie czy obowiazkowe wartości nie sa puste
        if t1 != '' and t2 != '' and t3 != '' and t5 != '':
            cDatabase.editPubData(self.session, t, t0)
            wx.MessageBox(u'Zauktualizowano wartości!', u'Sukces', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(u'Nie podana nazwy grupy \nlub nie wybrano autorów.', u'Bład', wx.OK | wx.ICON_INFORMATION)
        
        self.Destroy()

        
    def addPubValue(self, event):
        #Pobiera wartosci z kontrolek do edycji
        tx1 = self.m_textCtrl2.GetValue()
        tx2 = self.m_textCtrl4.GetValue()
        tx3 = self.m_textCtrl3.GetValue()
        tx4 = self.m_choice1.GetStringSelection()
        tx5 = self.m_textCtrl5.GetValue()
        tx6 = self.m_textCtrl6.GetValue()
        tx9 = self.m_textCtrl7.GetValue()
        tx7 = self.m_choice2.GetStringSelection()
        tx8 = self.getCheckUser()
        
        #Pobiera wartosci ID dla zaznaczonych autorów
        tmp = cDatabase.getJournalNameID(self.session)
        if tx7 != u'':
            tx7 = tmp[tx7]
        else:
            tx7 = None
        
        t = (tx1, tx2, tx3, tx4, tx5, tx6, tx9, tx7, tx8)
        
        #Sprawdzenie czy obowiazkowe wartości nie sa puste
        if tx1 != '' and tx2 != '' and tx3 != '' and tx5 != '' and tx8 != []:
            cDatabase.addPubData(self.session, t)
        else:
            wx.MessageBox(u'Pola "Tytuł, Autor, Cytowania, Rok" sa wymagane!', u'Bład', wx.OK | wx.ICON_INFORMATION)
        
        #Czyszczenie kontrolek po dodaniu publikacji
        self.m_choice1.SetSelection( 0 )        
        self.m_choice2.SetSelection( 0 )
        self.m_textCtrl2.SetValue('')
        self.m_textCtrl3.SetValue('')
        self.m_textCtrl4.SetValue('')
        self.m_textCtrl5.SetValue('')
        self.m_textCtrl6.SetValue('')
        self.m_textCtrl7.SetValue('')
        guser = cDatabase.getUserName(self.session)
        for i in range(len(guser)):
            self.m_checkList3.Check(i,  False)
        

    def getCheckUser(self):
        """Pobiera id wszystkich powiazanych autorów do publikacji"""
        result = []
        guser = cDatabase.getUserName(self.session) 
        t = cDatabase.getUserNameID(self.session)
        for i in range(len(guser)):
            if self.m_checkList3.IsChecked(i):
                id = t[guser[i]]
                result.append(id)
        return result
    
    def close(self, event):
        """Zamyka okienko publikacji"""
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    controller = PubDialog()
    controller.Show()
    app.MainLoop()
