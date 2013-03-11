# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import os
import wx.xrc
import modules.baz.cDatabase as cDatabase
import linecache

###########################################################################
## Class PubDialog
###########################################################################

class PubDialog ( wx.Dialog ):
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Zarządzanie Publikacjami", pos = wx.DefaultPosition, size = wx.Size( 450,430 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()
        self.listType = []
        self.getType()
        
        ico = wx.Icon('icon/pub.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer28 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dodawanie Publikacji", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
        self.m_staticText1.Wrap( -1 )
        bSizer21.Add( self.m_staticText1, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        bSizer28.Add( bSizer21, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer1.Add( bSizer28, 0, wx.EXPAND, 5 )
        
        bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Tytuł:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
        bSizer3.Add( self.m_textCtrl2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Autorzy:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer5.Add( self.m_staticText4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
        bSizer5.Add( self.m_textCtrl4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Cytowania:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
        bSizer4.Add( self.m_textCtrl3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Typ:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer6.Add( self.m_staticText5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice1Choices = self.listType
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 145,-1 ), m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer6.Add( self.m_choice1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer6, 0, wx.EXPAND, 5 )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Rok:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer7.Add( self.m_staticText6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
        bSizer7.Add( self.m_textCtrl5, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer7, 0, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"DOI:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer8.Add( self.m_staticText7, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
        bSizer8.Add( self.m_textCtrl6, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer8, 0, wx.EXPAND, 5 )
        
        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Inny klucz:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer29.Add( self.m_staticText9, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
        bSizer29.Add( self.m_textCtrl7, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer29, 0, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Wydawca:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer9.Add( self.m_staticText8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice2Choices = cDatabase.getJournalName(self.session)
        self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 145,-1 ), m_choice2Choices, 0 )
        bSizer9.Add( self.m_choice2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer9, 0, wx.EXPAND, 5 )
        
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Źródło:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer17.Add( self.m_staticText10, 1, wx.ALL, 5 )
        
        self.m_textCtrl71 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
        bSizer17.Add( self.m_textCtrl71, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer17, 1, wx.EXPAND, 5 )
        
        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"LMCP:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText99.Wrap( -1 )
        bSizer18.Add( self.m_staticText99, 1, wx.ALL, 5 )
        
        self.m_textCtrl99 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), 0 )
        self.m_textCtrl99.SetToolTipString( u"Ilość punktów na liście ministerialnej" )
        bSizer18.Add( self.m_textCtrl99, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer18, 1, wx.EXPAND, 5 )
        
        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText98 = wx.StaticText( self, wx.ID_ANY, u"JCR:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText98.Wrap( -1 )
        bSizer19.Add( self.m_staticText98, 1, wx.ALL, 5 )
        
        m_choice3Choices = ['True', 'False']
        self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 145,-1 ), m_choice3Choices, 0 )
        bSizer19.Add( self.m_choice3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer15.Add( bSizer19, 1, wx.EXPAND, 5 )
        
        bSizer26.Add( bSizer15, 1, wx.EXPAND, 5 )
        
        bSizer23 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        
        m_checkList3Choices = cDatabase.getUserName(self.session)
        self.m_checkList3 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,281 ), m_checkList3Choices, 0 )
        self.m_checkList3.SetToolTipString( u"Powiąż autorów z publikacją" )
        
        bSizer10.Add( self.m_checkList3, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer23.Add( bSizer10, 0, wx.EXPAND, 5 )
        
        
        bSizer26.Add( bSizer23, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer26, 0, wx.EXPAND, 5 )
        
        bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl55 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), wx.TE_MULTILINE )
        self.m_textCtrl55.SetToolTipString( u"Notatki do publikacji" )
        bSizer55.Add( self.m_textCtrl55, 1, wx.ALL|wx.EXPAND, 5  )
        
        
        bSizer1.Add( bSizer55, 0, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Zatwierdź", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Zamknij", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button4, 0, wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer11.Add( self.m_staticText11, 1, wx.ALL, 5 )
        
        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer11.Add( self.m_staticText12, 1, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_button3.Hide()
        self.m_staticText11.Hide()
        self.m_staticText12.Hide()
        
##################################################
## Bind
###################################################
        
        self.m_button1.Bind(wx.EVT_BUTTON, self.addPubValue)
        self.m_button4.Bind(wx.EVT_BUTTON, self.close)
        self.m_button3.Bind(wx.EVT_BUTTON, self.editPubValue)
        
###################################################
## Metody
###################################################
        self.getType()
    
    def getType(self):
        count = len(open('type.txt', 'rU').readlines())
        for i in range(count):
            self.listType.append(linecache.getline('type.txt',i+1))
        print self.listType
    
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
        t10 = self.m_textCtrl71.GetValue()
        t11 = self.m_textCtrl99.GetValue() #Lista ministerialna
        t12 = self.m_choice3.GetStringSelection() #czy jest w JCR
        t13 = self.m_textCtrl55.GetValue() #notatka
        
        #Odznacza już powiazanych autorów
        ch = cDatabase.editItemAuthor(self.session, t0)
        
        t9 = self.getCheckUser()
        
        #Pobiera wartosci ID dla zaznaczonych autorów
        tmp = cDatabase.getJournalNameID(self.session)
        print t8
        if t8 != u'':
            t8 = tmp[t8]
        else:
            t8 = None
        
        t = (t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13)
        
        #Sprawdzenie czy obowiazkowe wartości nie sa puste
        if t1 != '' and t2 != '' and t3 != '' and t5 != '':
            cDatabase.editPubData(self.session, t, t0)
            wx.MessageBox(u'Zauktualizowano wartości!', u'Sukces', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(u'Nie podana nazwy grupy \nlub nie wybrano autorów.', u'Bład', wx.OK | wx.ICON_INFORMATION)
        
        self.Destroy()

        
    def addPubValue(self, event):
        #Pobiera wartosci z kontrolek do edycji
        tx1 = self.m_textCtrl2.GetValue()               #tytul
        tx2 = self.m_textCtrl4.GetValue()               #autor
        tx3 = self.m_textCtrl3.GetValue()               #cytowania
        tx4 = self.m_choice1.GetStringSelection()   #typ
        tx5 = self.m_textCtrl5.GetValue()               #rok
        tx6 = self.m_textCtrl6.GetValue()               #doi
        tx9 = self.m_textCtrl7.GetValue()               #identy
        tx7 = self.m_choice2.GetStringSelection()   #wydawca ID
        tx8 = self.getCheckUser()                        #autor id
        tx10 = self.m_textCtrl71.GetValue()            #zrodlo
        tx11 = self.m_staticText11.GetLabel()           #urlpub
        tx12 = self.m_staticText12.GetLabel()           #urlcit
        tx13 = self.m_textCtrl99.GetValue() #Lista ministerialna
        tx14 = self.m_choice3.GetStringSelection() #jcr
        tx15 = self.m_textCtrl55.GetValue() #note
        
        #Pobiera wartosci ID dla zaznaczonych autorów
        tmp = cDatabase.getJournalNameID(self.session)
        if tx7 != u'':
            tx7 = tmp[tx7]
        else:
            tx7 = None
        
        t = (tx1, tx2, tx3, tx4, tx5, tx6, tx9, tx7, tx8, tx11, tx12, tx10, tx13, tx14, tx15)
        
        #Sprawdzenie czy obowiazkowe wartości nie sa puste
        if tx1 != '' and tx2 != '' and tx3 != '' and tx5 != '':
            cDatabase.addPubData(self.session, t)
        else:
            wx.MessageBox(u'Pola "Tytuł, Autor, Cytowania, Rok" sa wymagane!', u'Bład', wx.OK | wx.ICON_INFORMATION)
        
        self.Destroy()

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
