# -*- coding: utf-8 -*- 

################################################
##    Aplikacja wspomagajaca tworzenie bazy publikacji naukowych wpsółpracujaca z Google Scholar
##    Copyright (C) 2013  Damian Baran
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################

import wx
import os
import wx.xrc
import modules.baz.cDatabase as cDatabase

###########################################################################
## Class JourDialog
###########################################################################

## Dokumentacja dla klasy
#
# Klasa zawiera widok z zarzadzaniem wydawcami
class JourDialog ( wx.Dialog ):
    ##Konstruktor
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Zarządzanie Wydawcami", pos = wx.DefaultPosition, size = wx.Size( 350,230 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()

        ico = wx.Icon('icon/jou.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
    
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dodawanie Wydawcy", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
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
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Adres:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer5.Add( self.m_staticText4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,-1 ), 0 )
        bSizer5.Add( self.m_textCtrl4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
        
#        self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Notatki:", wx.DefaultPosition, wx.DefaultSize, 0 )
#        self.m_staticText55.Wrap( -1 )
#        bSizer55.Add( self.m_staticText55, 1, wx.ALL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), wx.TE_MULTILINE )
        self.m_textCtrl2.SetToolTipString( u"Notatki do autora" )
        bSizer55.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5  )
        
        
        bSizer1.Add( bSizer55, 0, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Zatwierdź", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Usuń", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Anuluj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button4, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_button3.Hide()
        self.m_button2.Hide()

###################################################
## Bind
###################################################
        
        self.m_button1.Bind(wx.EVT_BUTTON, self.addJournalValue)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cancel)
        self.m_button3.Bind(wx.EVT_BUTTON, self.editJournalValue)
        self.m_button2.Bind(wx.EVT_BUTTON, self.deleteJournalValue)
        self.m_comboBox1.Bind(wx.EVT_COMBOBOX, self.viewJournalValue)
        
###################################################
## Metody
###################################################
        
    ## Dokumentacja deleteJournalValue
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wysyla zadanie z usunieciem wybranego wydawcy przez uzytkownika
    def deleteJournalValue(self, event):
        tx1 = self.m_comboBox1.GetValue()   #pobieranie nazwy wydawcy z kontrolki
        
        if tx1 != '':
            cDatabase.delJournalData(self.session, tx1) #wywoałnie metody usuwajcej rekord z bazy
        else:
            wx.MessageBox(u'Nie ma takiego wydawcy w bazie!', u'Błąd!', wx.OK | wx.ICON_INFORMATION) 
        
        self.m_staticText1.SetLabel(u'Dodawanie Wydawcy')
        #Po usunięciu wyświetlnie w kontrolce nowej listy wydawców
        m_comboBox1Choices = cDatabase.getJournalName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
        self.m_comboBox1.SetSelection( 0 )
        
        self.cancel()

    ## Dokumentacja viewJournalValue
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wysyla zadanie z wyswietleniem wartosci dla wybranego wydawcy
    def viewJournalValue(self, event):
        self.tx1 = self.m_comboBox1.GetValue()
        
        data = cDatabase.getJournalData(self.session, self.tx1)
        
        self.m_textCtrl3.SetValue(data[0])
        self.m_textCtrl4.SetValue(data[1])
        self.m_textCtrl2.SetValue(data[2])
        
        self.m_staticText1.SetLabel(u'Edytowanie Wydawcy')
        self.m_button3.Show()
        self.m_button2.Show()
        self.m_button1.Hide()
    
    ## Dokumentacja addJournalValue
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wysyla zadanie o dodanie nowego wydawcy do bazy danych
    def addJournalValue(self, event):
        #Pobieranie danych wydawcy z kontrolek
        tx1 = self.m_comboBox1.GetValue()
        tx2 = self.m_textCtrl3.GetValue()
        tx3 = self.m_textCtrl4.GetValue()
        tx4 = self.m_textCtrl2.GetValue()
        t = (tx1, tx2, tx3, tx4)
        
        #Sprawdzenie czy obowiazkowe wartości nie sa puste
        if tx1 != '' or tx3 != '':
            cDatabase.addJournalData(self.session, t)
        else:
            wx.MessageBox(u'Nie podano pełnej nazwy \nlub adresu.', u'Błąd', wx.OK | wx.ICON_INFORMATION)   
        
        #Wyczysczenie wszystkich kontrolek i aktualizacja listy wydawców
        m_comboBox1Choices = cDatabase.getJournalName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
#        self.m_comboBox1.SetSelection( 0 )
        self.m_textCtrl3.SetValue('')
        self.m_textCtrl4.SetValue('')
        self.m_textCtrl2.SetValue('')
        
    ## Dokumentacja editJournalValue
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wysyla zadanie z edycja wybranego wydawcy przez uzytkownika
    def editJournalValue(self, event):
        #Pobieranie danych wydawcy z kontrolek
        tx1 = self.m_comboBox1.GetValue()
        tx2 = self.m_textCtrl3.GetValue()
        tx3 = self.m_textCtrl4.GetValue()
        tx4 = self.m_textCtrl2.GetValue()
        t = (tx1, tx2, tx3, tx4)
        
        jourID = cDatabase.getJournalNameID(self.session)
        id = jourID[self.tx1]
#        print id
        
        #Sprawdzenie czy obowiazkowe wartości nie sa puste
        if tx1 != '' or tx3 != '':
            try:
                cDatabase.editJournalData(self.session, t, id)
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
        self.m_textCtrl2.SetValue('')
        
        self.m_staticText1.SetLabel(u'Dodawanie Wydawcy')
        self.m_button3.Hide()
        self.m_button2.Hide()
        self.m_button1.Show()
        
    ## Dokumentacja cancel
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja zamyka okienko z zarzadzaniem wydawcami
    def cancel(self, event):
        #Wyczysczenie wszystkich kontrolek i aktualizacja listy wydawców
        m_comboBox1Choices = cDatabase.getJournalName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
#        self.m_comboBox1.SetSelection( 0 )
        self.m_textCtrl3.SetValue('')
        self.m_textCtrl4.SetValue('')
        self.m_textCtrl2.SetValue('')
        
        self.m_staticText1.SetLabel(u'Dodawanie Wydawcy')
        self.m_button3.Hide()
        self.m_button2.Hide()
        self.m_button1.Show()
        
        self.Destroy()
        """Zamyka okienko wydawcy"""
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    controller = JourDialog()
    controller.Show()
    app.MainLoop()
