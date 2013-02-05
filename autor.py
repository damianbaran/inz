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
## Class AuthorDialog
###########################################################################

class AuthorDialog ( wx.Dialog ):
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Edycja autorów", pos = wx.DefaultPosition, size = wx.Size( 350,300 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Edytuj Autora", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Pełna nazwa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer9.Add( self.m_staticText2, 1, wx.ALL, 5 )
        
        self.m_choice1Choices = cDatabase.getUserName(self.session)
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), self.m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer9.Add( self.m_choice1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )
        
        bSizer111 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"Wybierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer111.Add( self.m_button6, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer3.Add( bSizer111, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Uczelnia:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer13.Add( self.m_staticText6, 1, wx.ALL, 5 )
        
        m_comboBox1Choices = []
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), m_comboBox1Choices, 0 )
        bSizer13.Add( self.m_comboBox1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer13, 0, wx.EXPAND, 5 )
        
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Wydział:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer16.Add( self.m_staticText7, 1, wx.ALL, 5 )
        
        m_comboBox2Choices = []
        self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), m_comboBox2Choices, 0 )
        bSizer16.Add( self.m_comboBox2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer16, 0, wx.EXPAND, 5 )
        
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Instytut:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer17.Add( self.m_staticText8, 1, wx.ALL, 5 )
        
        m_comboBox3Choices = []
        self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), m_comboBox3Choices, 0 )
        bSizer17.Add( self.m_comboBox3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer17, 0, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Imię:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 1, wx.ALL, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer4.Add( self.m_textCtrl3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer5.Add( self.m_staticText4, 1, wx.ALL, 5 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer5.Add( self.m_textCtrl4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Filtr:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer12.Add( self.m_staticText5, 1, wx.ALL, 5 )
        
        self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer12.Add( self.m_textCtrl41, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer12, 0, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Edytuj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button1, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.m_button7 = wx.Button( self, wx.ID_ANY, u"Usuń", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button7, 0, wx.RIGHT|wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Zamknij", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button4, 0, wx.RIGHT|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
###################################################
## Bind
###################################################
        
        self.m_button6.Bind(wx.EVT_BUTTON, self.getPersonID)
        self.m_button1.Bind(wx.EVT_BUTTON, self.editPersonID)
        self.m_button4.Bind(wx.EVT_BUTTON, self.close)
        self.m_button7.Bind(wx.EVT_BUTTON, self.deletePerson)

###################################################
## Metody
###################################################

    def deletePerson(self, event):
        """Usuwa wybranego autora"""
        
        #Pobiera Imie i Nazwisko użytkownika, wraz z jego ID
        t = self.m_choice1.GetStringSelection()
        a = cDatabase.getUserNameID(self.session)
        self.tmp = a[t]
        
        #Usuwanie użytkownika
        cDatabase.delUserDialog(self.session, self.tmp)
        
        #Aktualizacja kontrolki z imionami i nazwiskami autorów
        m_choice1Choices = cDatabase.getUserName(self.session)
        self.m_choice1.Clear()
        self.m_choice1.AppendItems(m_choice1Choices)
        self.m_choice1.SetSelection( 0 )
        

    def editPersonID(self, event):
        """Edycja wybranego autora"""
        
        #Pobieranie wartosci z kontrolek
        tx1 = self.m_comboBox1.GetValue()
        tx2 = self.m_comboBox2.GetValue()
        tx3 = self.m_comboBox3.GetValue()
        tx4 = self.m_textCtrl3.GetValue()
        tx5 = self.m_textCtrl4.GetValue()
        tx6 = self.m_textCtrl41.GetValue()
        
        t = (tx1, tx2, tx3, tx4, tx5, tx6)
        
        #Sprawdzanie czy wymagane wartości nie sa puste
        if tx1 == '' or tx2 == '' or tx3 == '' or tx4 == '' or tx5 == '' or tx6 == '':
            wx.MessageBox(u'Wszystkie wartości musz być uzupełnione!', u'Bład!', wx.OK | wx.ICON_INFORMATION)
            return
        else:
            cDatabase.editUserDialog(self.session, t, self.tmp)
            wx.MessageBox(u'Dane zostały zaktualizowane!', u'Sukces!', wx.OK | wx.ICON_INFORMATION)
        
        #Aktualizacja listy autorów
        m_choice1Choices = cDatabase.getUserName(self.session)
        self.m_choice1.Clear()
        self.m_choice1.AppendItems(m_choice1Choices)
        self.m_choice1.SetSelection( 0 )
        
    def getPersonID(self, event):
        """Funkcja pobiera wartosci z bazy i ustawia je w kontrolkach"""
        t = self.m_choice1.GetStringSelection()
        a = cDatabase.getUserNameID(self.session)
        self.tmp = a[t]
        
        data = cDatabase.getUserDialog(self.session, self.tmp)
        
        """Dodaje wszystkie nazwy uczelni i ustawia wartość z wybranego rekordu"""
        m_comboBox1Choices = cDatabase.getCollegeName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
        self.m_comboBox1.SetValue(data[0])
        
        """Dodaje wszystkie nazwy wydziałów i ustawia wartość z wybranego rekordu"""
        m_comboBox2Choices = cDatabase.getFacultyName(self.session)
        self.m_comboBox2.Clear()
        self.m_comboBox2.AppendItems(m_comboBox2Choices)
        self.m_comboBox2.SetValue(data[1])
        
        """Dodaje wszystkie nazwy instytutów i ustawia wartość z wybranego rekordu"""
        m_comboBox3Choices = cDatabase.getInstituteName(self.session)
        self.m_comboBox3.Clear()
        self.m_comboBox3.AppendItems(m_comboBox3Choices)
        self.m_comboBox3.SetValue(data[2])
        
        self.m_textCtrl3.SetValue(data[3])
        self.m_textCtrl4.SetValue(data[4])
        self.m_textCtrl41.SetValue(data[5])
    
    def close(self, event):
        """Zamknięcie okienka autorów"""
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    controller = AuthorDialog()
    controller.Show()
    app.MainLoop()
