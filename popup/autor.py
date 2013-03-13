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
## Class AuthorDialog
###########################################################################

## Dokumentacja dla klasy
#
# Klasa zawiera widok z danymi o autorze
class AuthorDialog ( wx.Dialog ):
    ## Konstruktor
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Zarządzanie Autorami", pos = wx.DefaultPosition, size = wx.Size( 350,330 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()
        
        ico = wx.Icon('icon/autor.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
#        self.st1 =
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dodawanie Autora", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Edytuj Autora:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer9.Add( self.m_staticText2, 1, wx.ALL, 5 )
        
        self.m_choice1Choices = cDatabase.getUserName(self.session)
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 220,-1 ), self.m_choice1Choices, 0 )
#        self.m_choice1.SetSelection( 0 )
        bSizer9.Add( self.m_choice1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )
        
#        bSizer111 = wx.BoxSizer( wx.VERTICAL )
#        
#        self.m_button6 = wx.Button( self, wx.ID_ANY, u"Wybierz", wx.DefaultPosition, wx.DefaultSize, 0 )
#        bSizer111.Add( self.m_button6, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
#        
#        
#        bSizer3.Add( bSizer111, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Afiliacja:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer13.Add( self.m_staticText6, 1, wx.ALL, 5 )
        
        m_comboBox1Choices = cDatabase.getCollegeName(self.session)
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), m_comboBox1Choices, 0 )
        bSizer13.Add( self.m_comboBox1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer13, 0, wx.EXPAND, 5 )
        
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Wydział/Dział:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer16.Add( self.m_staticText7, 1, wx.ALL, 5 )
        
        m_comboBox2Choices = cDatabase.getFacultyName(self.session)
        self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), m_comboBox2Choices, 0 )
        bSizer16.Add( self.m_comboBox2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer16, 0, wx.EXPAND, 5 )
        
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Instytut/Stanowisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer17.Add( self.m_staticText8, 1, wx.ALL, 5 )
        
        m_comboBox3Choices = cDatabase.getInstituteName(self.session)
        self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), m_comboBox3Choices, 0 )
        bSizer17.Add( self.m_comboBox3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer17, 0, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Imię:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 1, wx.ALL, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
        bSizer4.Add( self.m_textCtrl3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer5.Add( self.m_staticText4, 1, wx.ALL, 5 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
        bSizer5.Add( self.m_textCtrl4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Filtr:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer12.Add( self.m_staticText5, 1, wx.ALL, 5 )
        
        self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
        self.m_textCtrl41.SetToolTipString( u"Format filtru: A Wójcik, A Wojcik, A WOJCIK" )
        bSizer12.Add( self.m_textCtrl41, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer12, 0, wx.EXPAND, 5 )
        
        bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
        
#        self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Notatki:", wx.DefaultPosition, wx.DefaultSize, 0 )
#        self.m_staticText55.Wrap( -1 )
#        bSizer55.Add( self.m_staticText55, 1, wx.ALL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), wx.TE_MULTILINE )
        self.m_textCtrl2.SetToolTipString( u"Notatki do autora" )
        bSizer55.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5  )
        
        
        bSizer1.Add( bSizer55, 0, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button2, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Zatwierdź", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button1, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.m_button7 = wx.Button( self, wx.ID_ANY, u"Usuń", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button7, 0, wx.RIGHT|wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Anuluj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button4, 0, wx.RIGHT|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_button1.Hide()
        self.m_button7.Hide()
        
###################################################
## Bind
###################################################
        
#        self.m_button6.Bind(wx.EVT_BUTTON, self.getPersonID)
        self.m_button1.Bind(wx.EVT_BUTTON, self.editPersonID)
        self.m_button2.Bind(wx.EVT_BUTTON, self.getUserData)
        self.m_button4.Bind(wx.EVT_BUTTON, self.cancel)
        self.m_button7.Bind(wx.EVT_BUTTON, self.deletePerson)
        self.m_choice1.Bind(wx.EVT_CHOICE,  self.getPersonID)

    ## Dokumentacja getUserData
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja pobiera wartości wprowadzone przez użytkownika do dodania nowego autora do bazy danych
    def getUserData(self, event):
        AllDict = {}
        UserDict = {}
        ColDict = {}
        FacDict = {}
        InsDict = {}
        
        dbCollege = self.m_comboBox1.GetValue()
        dbFaculty = self.m_comboBox2.GetValue()
        dbInstitut = self.m_comboBox3.GetValue()
        dbName = self.m_textCtrl3.GetValue()
        dbSurname = self.m_textCtrl4.GetValue()
        dbFilter = self.m_textCtrl41.GetValue()
        dbNote = self.m_textCtrl2.GetValue()
        
        if dbCollege == '' or dbName == '' or dbSurname == '' or dbFilter == '':
            wx.MessageBox(u'Wszystkie pola są wymagane', u'Błąd', wx.OK | wx.ICON_INFORMATION)
        else:
            ColDict['name'] = dbCollege
            FacDict['name'] = dbFaculty
            InsDict['name'] = dbInstitut
            UserDict['name'] = dbName
            UserDict['surname'] = dbSurname
            UserDict['filtr'] = dbFilter
            UserDict['note'] = dbNote
            AllDict = {'college':ColDict,'faculty':FacDict,'institute':InsDict,'person':UserDict}
            cDatabase.addUser(self.session,AllDict)
            wx.MessageBox(u'Poprawnie dodano Autora!', u'Sukces', wx.OK | wx.ICON_INFORMATION)
        
       #Aktualizacja kontrolki z imionami i nazwiskami autorów
        m_choice1Choices = cDatabase.getUserName(self.session)
        self.m_choice1.Clear()
        self.m_choice1.AppendItems(m_choice1Choices)

        self.clear()
        
        self.m_button1.Hide()
        self.m_button7.Hide()
        self.m_button2.Show()

    ## Dokumentacja clear
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja odświeza wszystkie kontrolki zawierajace dane z bazy danych
    def clear(self):
        """Aktualizacja kontrolki z nazwami uczelni"""
        m_comboBox1Choices = cDatabase.getCollegeName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
#        self.cb1.SetSelection( 0 )
        
        """Aktualizacja kontrolki z nazwami wydziałów"""
        m_comboBox2Choices = cDatabase.getFacultyName(self.session)
        self.m_comboBox2.Clear()
        self.m_comboBox2.AppendItems(m_comboBox2Choices)
#        self.cb2.SetSelection( 0 )
        
        """Aktualizacja kontrolki z nazwami instytutów"""
        m_comboBox3Choices = cDatabase.getInstituteName(self.session)
        self.m_comboBox3.Clear()
        self.m_comboBox3.AppendItems(m_comboBox3Choices)
#        self.cb3.SetSelection( 0 )
        
        self.m_textCtrl3.SetValue('')
        self.m_textCtrl4.SetValue('')
        self.m_textCtrl41.SetValue('')
        self.m_textCtrl2.SetValue('')

    ## Dokumentacja deletePerson
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wysyła żadanie o usunieciu autora wybranego przez użytkownika
    def deletePerson(self, event):
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
#        self.m_choice1.SetSelection( 0 )
        
        self.clear()
        
        self.m_staticText1.SetLabel(u'Dodawanie Autora')
#        self.st1 = u'Dodaj Autora'
        self.m_button1.Hide()
        self.m_button7.Hide()
        self.m_button2.Show()
        
        wx.MessageBox(u'Pomyślnie usunięto wybranego \
        Autora!', u'Sukces', wx.OK | wx.ICON_INFORMATION)

    ## Dokumentacja editPersonID
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wysyla zadanie o edycji wybranego autora wybranego przez uzytkownika
    def editPersonID(self, event):
        #Pobieranie wartosci z kontrolek
        tx1 = self.m_comboBox1.GetValue()
        tx2 = self.m_comboBox2.GetValue()
        tx3 = self.m_comboBox3.GetValue()
        tx4 = self.m_textCtrl3.GetValue()
        tx5 = self.m_textCtrl4.GetValue()
        tx6 = self.m_textCtrl41.GetValue()
        tx7 = self.m_textCtrl2.GetValue()
        
        t = (tx1, tx2, tx3, tx4, tx5, tx6, tx7)
        
        #Sprawdzanie czy wymagane wartości nie sa puste
        if tx1 == '' or tx4 == '' or tx5 == '' or tx6 == '':
            wx.MessageBox(u'Wszystkie wartości musz być \
            uzupełnione!', u'Bład!\
            ', wx.OK | wx.ICON_INFORMATION)
            return
        else:
            cDatabase.editUserDialog(self.session, t, self.tmp)
            wx.MessageBox(u'Dane zostały zaktualizowane!\
            ', u'Sukces', wx.OK | wx.ICON_INFORMATION)
        
        #Aktualizacja listy autorów
        m_choice1Choices = cDatabase.getUserName(self.session)
        self.m_choice1.Clear()
        self.m_choice1.AppendItems(m_choice1Choices)
#        self.m_choice1.SetSelection( 0 )
        
        self.clear()
        self.m_staticText1.SetLabel(u'Dodawanie Autora')
#        self.st1 = u'Dodaj Autora'
        self.m_button1.Hide()
        self.m_button7.Hide()
        self.m_button2.Show()
        
        
    ## Dokumentacja getPersonID
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja pobiera wartosci z bazy i wyswietla je w kontrolkach dla uzytkownika
    def getPersonID(self, event):
        self.m_staticText1.SetLabel(u'Edytowanie Autora')
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
        self.m_textCtrl2.SetValue(str(data[6]))
        
        self.m_button1.Show()
        self.m_button7.Show()
        self.m_button2.Hide()
    
    ## Dokumentacja cancel
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja zamyka okienko do zarzadzania autorami
    def cancel(self, event):
        self.m_staticText1.SetLabel(u'Dodawanie Autora')
#        self.st1 = u'Dodaj Autora'
        #Aktualizacja kontrolki z imionami i nazwiskami autorów
        m_choice1Choices = cDatabase.getUserName(self.session)
        self.m_choice1.Clear()
        self.m_choice1.AppendItems(m_choice1Choices)
#        self.m_choice1.SetSelection( 0 )

        self.clear()
        
        self.m_button1.Hide()
        self.m_button7.Hide()
        self.m_button2.Show()
        
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    controller = AuthorDialog()
    controller.Show()
    app.MainLoop()
