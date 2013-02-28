# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class About
###########################################################################

class About ( wx.Dialog ):
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u'O Programie', pos = wx.DefaultPosition, size = wx.Size( 350,270 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX )
        
        
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
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Program do wyszukiwania oraz zarządzania publikacjami naukowymi. Wyszukiwarka współpracująca z Google Scholar. Tworzy własną bazę publikację, na bazie której generowane są pliki bibliograficzne.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText3.Wrap( -1 )
        bSizer5.Add( self.m_staticText3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"\xa9 2013 Damian Baran", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer6.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer2.Add( bSizer6, 0, wx.EXPAND, 5 )
    
        bSizer7 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Zamknij", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        bSizer2.Add( bSizer7, 0, wx.EXPAND, 5 )
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_button1.Bind(wx.EVT_BUTTON,  self.close)
    
    def close(self, event):
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    controller = About()
    controller.Show()
    app.MainLoop()
