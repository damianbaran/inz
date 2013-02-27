# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class BibDialog
###########################################################################

class BibDialog ( wx.Dialog ):
	
	def __init__( self ):
		wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 200,175 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Wybierz typ publikacji", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"Artykuł", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"Książka", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, u"Dokumentacja Techniczna", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
		
		self.m_radioBtn4 = wx.RadioButton( self, wx.ID_ANY, u"Inne", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_radioBtn4, 0, wx.ALL, 5 )
		
		bSizer1.Add( bSizer5, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button2, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

if __name__ == "__main__":
    app = wx.App(False)
    controller = BibDialog()
    controller.Show()
    app.MainLoop()
