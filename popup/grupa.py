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
## Class GroupDialog
###########################################################################

## Dokumentacja dla klasy
#
# Klasa zawiera widok z zarzadzaniem grupami
class GroupDialog ( wx.Dialog ):
    ## Konstruktor
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Zarządzanie Grupami", pos = wx.DefaultPosition, size = wx.Size( 330,330 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()

        ico = wx.Icon('icon/grupa.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        
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

    ## Dokumentacja deleteGroupValue
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wysyla zadanie o usuniecie grupy uzytkownikow
    def deleteGroupValue(self, event):
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
    
    ## Dokumentacja addDataGroup
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wysyla zadanie o dodanie lub edycje grupy uzytkownikow
    def addDataGroup(self,  event):
        #Pobieranie i deklaracji wartosci
        result = []
        gname = self.m_comboBox1.GetValue()
        gnote = self.m_textCtrl2.GetValue()
        
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
            cDatabase.addGroup(self.session, result, gnote)
        else:
            wx.MessageBox(u'Nie podana nazwy grupy \nlub nie wybrano \
            autorów.', u'Bład', wx.OK | wx.ICON_INFORMATION)
        
        #Wyczyszczenie kontrolek
        self.clearData()
        
        self.m_staticText1.SetLabel(u'Dodawanie Grupy')
        self.m_button5.Hide()
        self.m_button3.Hide()
        self.m_button1.Show()
    
    ## Dokumentacja checkDataGroup
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funcka wysyla zadanie, ktore sprawdza, jacy autorzy naleza do wybranej grupy
    def checkDataGroup(self, event):
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
        
        n = cDatabase.getGroup(self.session, gname)
        self.m_textCtrl2.SetValue(n)
        
        self.m_staticText1.SetLabel(u'Edytowanie Grupy')
        self.m_button5.Show()
        self.m_button3.Show()
        self.m_button1.Hide()
    
    ## Dokumentacja clearData
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja czyści wszystkie kontrolki po wykonaniu zadania przez użytkownika
    def clearData(self):
        #Czyszczenie kontrolkki z nazwami grup
        guser = cDatabase.getUserName(self.session)
        m_comboBox1Choices = cDatabase.getGroupName(self.session)
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(m_comboBox1Choices)
        
        #Czyszczenie zaznaczonych autorow
        self.m_comboBox1.SetValue('')
        self.m_textCtrl2.SetValue('')
        for i in range(len(guser)):
            self.m_checkList3.Check(i,  False)
    
    ## Dokumentacja cancel
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja zamyka okienko z zarzadzaniem grupami
    def cancel(self, event):
        self.clearData()
        
        self.m_staticText1.SetLabel(u'Dodawanie Grupy')
        self.m_button5.Hide()
        self.m_button3.Hide()
        self.m_button1.Show()
        
        self.Destroy()
    
if __name__ == "__main__":
    app = wx.App(False)
    controller = GroupDialog()
    controller.Show()
    app.MainLoop()
