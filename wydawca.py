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
## Class JourDialog
###########################################################################

class JourDialog ( wx.Dialog ):
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Dodawanie i edycja wydawcy:", pos = wx.DefaultPosition, size = wx.Size( 350,165 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
    
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dodaj Wydawcę", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Pełna nazwa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox1Choices = cDatabase.getJournalName(self.session)
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size( 230,-1 ), m_comboBox1Choices, 0 )
        bSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Skrócona nazwa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer4.Add( self.m_textCtrl3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"ISSN:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer5.Add( self.m_staticText4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer5.Add( self.m_textCtrl4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Aktualizuj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button3, 0, wx.ALL, 5 )
        
#        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Usuń", wx.DefaultPosition, wx.DefaultSize, 0 )
#        bSizer11.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Zamknij", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button4, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )

###################################################
## Bind
###################################################
        
        self.m_button1.Bind(wx.EVT_BUTTON, self.addJournalValue)
        self.m_button4.Bind(wx.EVT_BUTTON, self.close)
        self.m_button3.Bind(wx.EVT_BUTTON, self.editJournalValue)
#        self.m_button2.Bind(wx.EVT_BUTTON, self.deleteJournalValue)
        self.m_comboBox1.Bind(wx.EVT_COMBOBOX, self.viewJournalValue)
        
###################################################
## Metody
###################################################
        
#    def deleteJournalValue(self, event):
#        """Usuwanie wybranego wydawcy z bazy danych"""
#        tx1 = self.m_comboBox1.GetValue()   #pobieranie nazwy wydawcy z kontrolki
#        
#        if tx1 != '':
#            cDatabase.delJournalData(self.session, tx1) #wywoałnie metody usuwajcej rekord z bazy
#        else:
#            wx.MessageBox(u'Nie ma takiego wydawcy w bazie!', u'Błąd!', wx.OK | wx.ICON_INFORMATION) 
#        
#        #Po usunięciu wyświetlnie w kontrolce nowej listy wydawców
#        m_comboBox1Choices = cDatabase.getJournalName(self.session)
#        self.m_comboBox1.Clear()
#        self.m_comboBox1.AppendItems(m_comboBox1Choices)
#        self.m_comboBox1.SetSelection( 0 )

    def viewJournalValue(self, event):
        tx1 = self.m_comboBox1.GetValue()
        
        data = cDatabase.getJournalData(self.session, tx1)
        
        self.m_textCtrl3.SetValue(data[0])
        self.m_textCtrl4.SetValue(data[1])
    
    def addJournalValue(self, event):
        """Dodawanie nowego wydawcy do bazy danych"""
        #Pobieranie danych wydawcy z kontrolek
        tx1 = self.m_comboBox1.GetValue()
        tx2 = self.m_textCtrl3.GetValue()
        tx3 = self.m_textCtrl4.GetValue()
        t = (tx1, tx2, tx3)
        
        #Sprawdzenie czy obowiazkowe wartości nie sa puste
        if tx1 != '' or tx3 != '':
            cDatabase.addJournalData(self.session, t)
        else:
            wx.MessageBox(u'Nie podano pełnej nazwy \nlub numeru ISSN.', u'Błąd', wx.OK | wx.ICON_INFORMATION)   
        
        #Wyczysczenie wszystkich kontrolek i aktualizacja listy wydawców
        m_comboBox1Choices = cDatabase.getJournalName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
#        self.m_comboBox1.SetSelection( 0 )
        self.m_textCtrl3.SetValue('')
        self.m_textCtrl4.SetValue('')
        
    def editJournalValue(self, event):
        """Edytowanie wybranego wydawcy w bazie danych"""
        #Pobieranie danych wydawcy z kontrolek
        tx1 = self.m_comboBox1.GetValue()
        tx2 = self.m_textCtrl3.GetValue()
        tx3 = self.m_textCtrl4.GetValue()
        t = (tx1, tx2, tx3)
        
        #Sprawdzenie czy obowiazkowe wartości nie sa puste
        if tx1 != '' or tx3 != '':
            try:
                cDatabase.editJournalData(self.session, t)
                wx.MessageBox(u'Dane zaktualizowano pomyślnie!', u'Sukces!', wx.OK | wx.ICON_INFORMATION) 
            except Exception, e: #Wywołanie wyjtku, który został stworzony w zapytaniu do bazy
                e
        
        #Wyczysczenie wszystkich kontrolek i aktualizacja listy wydawców
        m_comboBox1Choices = cDatabase.getJournalName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
#        self.m_comboBox1.SetSelection( 0 )
        self.m_textCtrl3.SetValue('')
        self.m_textCtrl4.SetValue('')
    
    def close(self, event):
        """Zamyka okienko wydawcy"""
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    controller = JourDialog()
    controller.Show()
    app.MainLoop()
