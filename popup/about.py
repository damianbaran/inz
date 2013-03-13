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

###########################################################################
## Class About
###########################################################################

## Dokumentacja dla klasy
#
# Klasa zawiera widok z informacjami o programie
class About ( wx.Dialog ):
    ## Konstruktor
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u'O Programie', pos = wx.DefaultPosition, size = wx.Size( 350,320 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX )
        
        
        ico = wx.Icon('icon/about.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bitmap1 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"icon/pobrane.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer3.Add( self.m_bitmap1, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        bSizer2.Add( bSizer3, 0, wx.TOP|wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"PubRansack 1.0", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Program do wyszukiwania oraz zarządzania publikacjami naukowymi. Wyszukiwarka współpracująca z Google Scholar. Tworzy własną bazę publikację, na bazie której generowane są pliki bibliograficzne. Program został wykonany w ramach pracy dyplomowej.\nPubRansack  Copyright \xa9 2013  Damian Baran This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'. This is free software, and you are welcome to redistribute it under certain conditions; type `show c' for details.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText3.Wrap( -1 )
        bSizer5.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
        
#        bSizer6 = wx.BoxSizer( wx.VERTICAL )
#        
#        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"\xa9 2013 Damian Baran", wx.DefaultPosition, wx.DefaultSize, 0 )
#        self.m_staticText2.Wrap( -1 )
#        bSizer6.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
#        
#        bSizer2.Add( bSizer6, 0, wx.EXPAND, 5 )
    
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Licencja", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button2, 0, wx.ALL, 5 )
        
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Zamknij", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        bSizer7.Add( bSizer8, 1, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )
        
        bSizer2.Add( bSizer7, 0, wx.EXPAND, 5 )
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_button1.Bind(wx.EVT_BUTTON,  self.close)
        self.m_button2.Bind(wx.EVT_BUTTON,  self.license)
    
    ## Dokumentacja license
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja wyswietla plik z licencja
    def license(self, event):
        osCommandString = "notepad.exe license.txt"
        os.system(osCommandString)
        
    ## Dokumentacja close
    # @param self Wskaźnik obiektu
    # @param event Wywołanie żadania
    #
    # @return void
    # Funkcja zamyka okienko z informacjami o programie
    def close(self, event):
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    controller = About()
    controller.Show()
    app.MainLoop()
