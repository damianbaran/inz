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
import wx.xrc
import modules.baz.cDatabase as cDatabase
import webbrowser
import wx.lib.mixins.listctrl as listmix
from wx.lib.pubsub import Publisher

###########################################################################
## Class CiteDialog
###########################################################################

## Dokumentacja dla klasy
#
# Klasa tworzy zaawansowana kontrolke do wyswietlania publikacji
class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

## Dokumentacja dla klasy
#
# Klasa zawiera widok z publikacjami
class CitePubDialog ( wx.Dialog ):
    ## Konstruktor
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Dodaj Publikację", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.session = cDatabase.connectDatabase()
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        
#        self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
        self.dataList = TestListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, u'ID', format=wx.LIST_FORMAT_CENTER, width=23)
        self.dataList.InsertColumn(1, u'Cytowań', format=wx.LIST_FORMAT_RIGHT, width=60)
        self.dataList.InsertColumn(2, u'Tytuł', format=wx.LIST_FORMAT_LEFT, width=130)
        self.dataList.InsertColumn(3, u'Autor', format=wx.LIST_FORMAT_LEFT, width=100)
        self.dataList.InsertColumn(4, u'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, u'Źródło', format=wx.LIST_FORMAT_LEFT, width=100)
        self.dataList.InsertColumn(6, u'DOI', format=wx.LIST_FORMAT_LEFT, width=100)
        bSizer13.Add( self.dataList, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.ALIGN_RIGHT, 5 )
        
        
        bSizer13.Add( bSizer4, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
#################################################
## Bind
###################################################
        
#        self.Bind( wx.EVT_TOOL, self.openLinkCit, addall )
#        self.Bind( wx.EVT_TOOL, self.openLinkPub, addone )
#        self.Bind( wx.EVT_TOOL, self.clearData, clear )
#        self.Bind( wx.EVT_TOOL, self.mergePub, merge )
#        self.Bind( wx.EVT_TOOL, self.deletePub, delpub )
#        self.Bind( wx.EVT_TOOL, self.backListPub, backlist )
        self.m_button1.Bind(wx.EVT_BUTTON, self.addPub)

###################################################
## Metody
###################################################
        self.data = cDatabase.getCitPubData(self.session)
        self.updateRecord()
    
    ## Dokumentacja addPub
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja przekazuje wartosci wybranej publikacji do innego widoku
    def addPub(self, event):
        result = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                t = int(t)
                x = cDatabase.getMergePubData(self.session, t)
                result.append(x)
        Publisher().sendMessage(('update_data'), result)
        wx.MessageBox(u'Poprawnie dodano wybrane publikacje', u'Sukces', wx.OK | wx.ICON_INFORMATION)
        self.Destroy()
    
    ## Dokumentacja updateRecord
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja wyswietla liste publikacji w kontrolce
    def updateRecord(self):
        for i in range(len(self.data)):
            self.dataList.Append(self.data[i])

if __name__ == "__main__":
    app = wx.App(False)
    controller = CitePubDialog()
    controller.Show()
    app.MainLoop()
