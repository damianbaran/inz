# -*- coding: utf-8 -*-
import wx
import os
#from src.frames import MainFrame
from schControler import sControler
import cDatabase
import wx.lib.mixins.listctrl as listmix
#from ObjectListView import ObjectListView, ColumnDefn

class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class sView(wx.Panel):
    def __init__(self, parent):
        #wx.Frame.__init__(self, None)
        wx.Panel.__init__(self, parent=parent)
        
        self.control = sControler()
        
        if not os.path.exists('schdatabase.db'):
            cDatabase.createDatabase()
            
        self.session = cDatabase.connectDatabase()
        
        #cDatabase.getAllRecord(self.session)
        #cDatabase.getUserFilter(self.session)
        

        self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        globalBox = wx.BoxSizer( wx.VERTICAL )
		
        oneBox1 = wx.BoxSizer( wx.HORIZONTAL )
        oneBox11 = wx.BoxSizer( wx.VERTICAL )
		
    	oneSB1 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Wyszukiwarka Google Scholar" ), wx.VERTICAL )
		
        oneBox111 = wx.BoxSizer( wx.HORIZONTAL )
		
    	self.txt1 = wx.StaticText( self.panel, wx.ID_ANY, u"Wszystkie słowa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt1.Wrap( -1 )
        oneBox111.Add( self.txt1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl1 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox111.Add( self.ctrl1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
        oneSB1.Add( oneBox111, 0, wx.EXPAND, 5 )
		
        oneBox112 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt2 = wx.StaticText( self.panel, wx.ID_ANY, u"Wyrażenie:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt2.Wrap( -1 )
        oneBox112.Add( self.txt2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl2 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 200,20 ), 0 )
        oneBox112.Add( self.ctrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
        oneSB1.Add( oneBox112, 0, wx.EXPAND, 5 )
		
        oneBox113 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt3 = wx.StaticText( self.panel, wx.ID_ANY, u"Jedno ze słów:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )
        oneBox113.Add( self.txt3, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl3 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox113.Add( self.ctrl3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
        oneSB1.Add( oneBox113, 0, wx.EXPAND, 5 )
		
        oneBox114 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt4 = wx.StaticText( self.panel, wx.ID_ANY, u"Bez słów:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt4.Wrap( -1 )
        oneBox114.Add( self.txt4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl4 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox114.Add( self.ctrl4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
        oneSB1.Add( oneBox114, 0, wx.EXPAND, 5 )
		
        oneBox115 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt5 = wx.StaticText( self.panel, wx.ID_ANY, u"Autor:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt5.Wrap( -1 )
        oneBox115.Add( self.txt5, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl5 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox115.Add( self.ctrl5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
        oneSB1.Add( oneBox115, 0, wx.EXPAND, 5 )
		
        oneBox116 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt6 = wx.StaticText( self.panel, wx.ID_ANY, u"Dziedzina:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt6.Wrap( -1 )
        oneBox116.Add( self.txt6, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl6 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox116.Add( self.ctrl6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
        oneSB1.Add( oneBox116, 0, wx.EXPAND, 5 )
		
        oneBox117 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt7 = wx.StaticText( self.panel, wx.ID_ANY, u"Rok od:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt7.Wrap( -1 )
        oneBox117.Add( self.txt7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl7 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,20 ), 0 )
        oneBox117.Add( self.ctrl7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.txt8 = wx.StaticText( self.panel, wx.ID_ANY, u"do", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt8.Wrap( -1 )
        oneBox117.Add( self.txt8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl8 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,20 ), 0 )
        oneBox117.Add( self.ctrl8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.but1 = wx.Button( self.panel, wx.ID_ANY, u"Pobierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox117.Add( self.but1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		
        oneSB1.Add( oneBox117, 0, wx.EXPAND, 5 )
		
		
        oneBox11.Add( oneSB1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		
        oneBox1.Add( oneBox11, 1, wx.EXPAND|wx.ALL, 5 )
		
        oneBox12 = wx.BoxSizer( wx.VERTICAL )
		
        oneSB2 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Wyszukiwanie Grupowe" ), wx.VERTICAL )
		
        bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
        self.m_staticText18 = wx.StaticText( self.panel, wx.ID_ANY, u"Wyszukiwanie dla wcześniej zdefiniowanej grupy autorów.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        bSizer27.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.FIXED_MINSIZE, 5 )
		
		
        oneSB2.Add( bSizer27, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.m_staticText19 = wx.StaticText( self.panel, wx.ID_ANY, u"Grupa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        bSizer28.Add( self.m_staticText19, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice2Choices = self.SetGroupName()
        self.m_choice2 = wx.Choice( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,-1 ), m_choice2Choices, 0 )
#        self.m_choice2.SetSelection( 0 )
        bSizer28.Add( self.m_choice2, 0, wx.ALL, 5 )
        
        
        oneSB2.Add( bSizer28, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        bSizer29 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button7 = wx.Button( self.panel, wx.ID_ANY, u"Pobierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer29.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        
        oneSB2.Add( bSizer29, 0, wx.EXPAND, 5 )
        
        
        oneBox12.Add( oneSB2, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
        oneSB3 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Filtracja" ), wx.VERTICAL )
		
        oneBox124 = wx.BoxSizer( wx.VERTICAL )
		
        self.txt12 = wx.StaticText( self.panel, wx.ID_ANY, u"Filtracje danych można przeprowadzić po ściągnięciu danych.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.txt12.Wrap( -1 )
        oneBox124.Add( self.txt12, 0, wx.ALL|wx.EXPAND, 5 )
		
		
        oneSB3.Add( oneBox124, 1, wx.EXPAND, 5 )
		
        oneBox125 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt13 = wx.StaticText( self.panel, wx.ID_ANY, u"Imie i Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt13.Wrap( -1 )
        oneBox125.Add( self.txt13, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ch4Choices = self.SetUserName()
        self.ch4 = wx.Choice( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,-1 ), self.ch4Choices, 0 )
#        self.ch4.SetSelection( 0 )
        oneBox125.Add( self.ch4, 0, wx.ALL, 5 )
		
		
        oneSB3.Add( oneBox125, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
        oneBox126 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.but2 = wx.Button( self.panel, wx.ID_ANY, u"Filtruj", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox126.Add( self.but2, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.LEFT, 5 )
		
        self.but3 = wx.Button( self.panel, wx.ID_ANY, u"Ofiltruj", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox126.Add( self.but3, 0, 0, 5 )
		
		
        oneSB3.Add( oneBox126, 1, wx.ALIGN_RIGHT|wx.TOP|wx.RIGHT, 5 )
		
		
        oneBox12.Add( oneSB3, 1, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		
        oneBox1.Add( oneBox12, 1, wx.EXPAND|wx.ALL, 5 )
		
        oneBox13 = wx.BoxSizer( wx.VERTICAL )
		
        oneSB4 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Dodaj użytkownika" ), wx.VERTICAL )
		
        oneBox131 = wx.BoxSizer( wx.VERTICAL )
		
        oneBox132 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt14 = wx.StaticText( self.panel, wx.ID_ANY, u"Uczelnia Wyższa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt14.Wrap( -1 )
        oneBox132.Add( self.txt14, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        cb1Choices = self.SetCollegeName()
        self.cb1 = wx.ComboBox( self.panel, wx.ID_ANY, u"Uczelnia", wx.DefaultPosition, wx.Size( 202,21 ), cb1Choices, 0 )
        oneBox132.Add( self.cb1, 0, wx.ALL, 5 )
		
		
        oneBox131.Add( oneBox132, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
        oneBox133 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt15 = wx.StaticText( self.panel, wx.ID_ANY, u"Wydział:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt15.Wrap( -1 )
        oneBox133.Add( self.txt15, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        cb2Choices = self.SetFacultyName()
        self.cb2 = wx.ComboBox( self.panel, wx.ID_ANY, u"Wydział", wx.DefaultPosition, wx.Size( 202,21 ), cb2Choices, 0 )
        oneBox133.Add( self.cb2, 0, wx.ALL, 5 )
		
		
        oneBox131.Add( oneBox133, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
        oneBox134 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt16 = wx.StaticText( self.panel, wx.ID_ANY, u"Instytut:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt16.Wrap( -1 )
        oneBox134.Add( self.txt16, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        cb3Choices = self.SetInstituteName()
        self.cb3 = wx.ComboBox( self.panel, wx.ID_ANY, u"Instytut", wx.DefaultPosition, wx.Size( 202,21 ), cb3Choices, 0 )
        oneBox134.Add( self.cb3, 0, wx.ALL, 5 )
		
		
        oneBox131.Add( oneBox134, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
        oneBox135 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt17 = wx.StaticText( self.panel, wx.ID_ANY, u"Imię:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt17.Wrap( -1 )
        oneBox135.Add( self.txt17, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl17 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 202,-1 ), 0 )
        oneBox135.Add( self.ctrl17, 0, wx.ALL, 5 )
		
		
        oneBox131.Add( oneBox135, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
	
        oneBox136 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt18 = wx.StaticText( self.panel, wx.ID_ANY, u"Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt18.Wrap( -1 )
        oneBox136.Add( self.txt18, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl18 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 202,-1 ), 0 )
        oneBox136.Add( self.ctrl18, 0, wx.ALL, 5 )
		
		
        oneBox131.Add( oneBox136, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
        oneBox137 = wx.BoxSizer( wx.HORIZONTAL )
        
		
        self.txt19 = wx.StaticText( self.panel, wx.ID_ANY, u'Filtracja:', wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt19.Wrap( -1 )
        oneBox137.Add( self.txt19, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
        self.ctrl19 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 202,-1 ), 0 )
        oneBox137.Add( self.ctrl19, 0, wx.ALL, 5 )
		
		
        oneBox131.Add( oneBox137, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
        oneBox138 = wx.BoxSizer( wx.HORIZONTAL )
		
        self.txt20 = wx.StaticText( self.panel, wx.ID_ANY, u"np. J Wójcik, J Wojcik, J WOJCIK, J WÓJCIK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt20.Wrap( -1 )
        oneBox138.Add( self.txt20, 0, wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
        self.but4 = wx.Button( self.panel, wx.ID_ANY, u"Dodaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox138.Add( self.but4, 0, wx.ALL, 5 )
		
		
        oneBox131.Add( oneBox138, 1, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		
        oneSB4.Add( oneBox131, 1, wx.EXPAND, 5 )
		
		
        oneBox13.Add( oneSB4, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
        oneBox1.Add( oneBox13, 1, wx.EXPAND, 5 )
		
		
        globalBox.Add( oneBox1, 0, wx.EXPAND, 5 )
		
        twoBox1 = wx.BoxSizer( wx.HORIZONTAL )
		
        twoBox11 = wx.BoxSizer( wx.VERTICAL )
		
        #self.dataList = wx.ListCtrl( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,295 ), wx.LC_ICON )
        self.dataList = TestListCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,295 ), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, '', format=wx.LIST_FORMAT_CENTER, width=25)
        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=70)
        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=320)
        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=180)
        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=120)
        
        twoBox11.Add( self.dataList, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		
        twoBox1.Add( twoBox11, 1, wx.RIGHT|wx.EXPAND, 5 )
	
        twoBox12 = wx.BoxSizer( wx.VERTICAL )
		
        self.but5 = wx.Button( self.panel, wx.ID_ANY, u"Dodaj zaznaczone", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        twoBox12.Add( self.but5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
        self.but6 = wx.Button( self.panel, wx.ID_ANY, u"Przywróć liste", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.but6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
	
        twoBox12.Add( self.but6, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
        twoBox1.Add( twoBox12, 0, wx.ALL, 5 )
		
		
        globalBox.Add( twoBox1, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )
	
		
        self.panel.SetSizer( globalBox )
        self.panel.Layout()
        globalBox.Fit( self.panel )
        
        """
        ########################################################################
        #  Panel 1
        ########################################################################
        self.panel1 = wx.Panel(self, -1, pos=(0,0), size=(330,210))
        self.panel2 = wx.Panel(self, -1, pos=(0,210), size=(1024,410))
        self.panel3 = wx.Panel(self, -1, pos=(330,0), size=(330,210))
        self.panel4 = wx.Panel(self, -1, pos=(660,0), size=(360,210))
        

        wx.StaticBox(self.panel1, -1, 'Wyszukiwanie Google Scholar',
                     pos=(5, 5), size=(320, 200))
        #1
        text1 = wx.StaticText(self.panel1, label="Wszystkie slowa:", pos=(15,30))
        self.ctrl1 = wx.TextCtrl(self.panel1, size=(200,20), pos=(105,27.5))
        #2
        text2 = wx.StaticText(self.panel1, label="Wyrazenie:", pos=(15,55))
        self.ctrl2 = wx.TextCtrl(self.panel1, size=(200,20), pos=(105,52.5))
        #3
        text3 = wx.StaticText(self.panel1, label="Jedno ze slow:", pos=(15,80))
        self.ctrl3 = wx.TextCtrl(self.panel1, size=(200,20), pos=(105,77.5))
        #4
        text4 = wx.StaticText(self.panel1, label="Bez slow:", pos=(15,105))
        self.ctrl4 = wx.TextCtrl(self.panel1, size=(200,20), pos=(105,102.5))
        #5
        text5 = wx.StaticText(self.panel1, label="Autor:", pos=(15,130))
        self.ctrl5 = wx.TextCtrl(self.panel1, size=(200,20), pos=(105,127.5))
        #6
        text6 = wx.StaticText(self.panel1, label="Dziedzina:", pos=(15,155))
        self.ctrl6 = wx.TextCtrl(self.panel1, size=(200,20), pos=(105,152.5))
        #7
        text7 = wx.StaticText(self.panel1, label="Rok od:", pos=(15,180))
        self.ctrl7 = wx.TextCtrl(self.panel1, size=(50,20), pos=(105,177.5))
        text8 = wx.StaticText(self.panel1, label=" do ", pos=(165,180))
        self.ctrl8 = wx.TextCtrl(self.panel1, size=(50,20), pos=(185,177.5))
        #button
        self.but1 = wx.Button(self.panel1, -1, label='Pobierz', pos=(245,177.5))
        
        ########################################################################
        #  Panel 2
        ########################################################################
        
        self.dataList = TestListCtrl(self.panel2, pos=(5,5), size=(780,400),
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, '', format=wx.LIST_FORMAT_CENTER, width=25)
        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=70)
        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=220)
        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=150)
        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=100)
        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=140)
        
        self.but7 = wx.Button(self.panel2, -1, label='Dodaj wybrane', pos=(790,5))
        self.but10 = wx.Button(self.panel2, -1, label='Przywroc liste', pos=(790,30))
        #self.but2 = wx.Button(self.panel2, -1, label='Czysc Liste', pos=(790,5))
        #self.but3 = wx.Button(self.panel2, -1, label='Zaznacz Wszystko', pos=(790,30))
        #self.but4 = wx.Button(self.panel2, -1, label='Odznacz Wszystko', pos=(790,55))
        #self.but5 = wx.Button(self.panel2, -1, label='Zaznacz Rekord', pos=(790,80))
        #self.but6 = wx.Button(self.panel2, -1, label='Odznacz Rekord', pos=(790,105))
        
        ########################################################################
        #  Panel 3
        ########################################################################
        
        
        self.tmp = ['Leszek Wojnar','Marcin Majorek','Zbiegniew Latala']
        text9 = wx.StaticText(self.panel3, label="Imie i nazwisko: ", pos=(10,12.5))
        self.ch = wx.Choice(self.panel3, -1, pos=(90,10), choices=self.tmp)
        self.but8 = wx.Button(self.panel3, -1, label='Filtruj', pos=(200,30))
        self.but9 = wx.Button(self.panel3, -1, label='Odfiltruj', pos=(200,60))
        
        self.menu_title_by_id = {1:'Zaznacz',2:'Odznacz',3:'Zaznacz wszystko',
                                    4:'Odznacz wszystko',5:'Czysc liste'}
        
        ########################################################################
        #  Panel 4
        ########################################################################
        
        text10 = wx.StaticText(self.panel4, label="Liczba rekordow: ", pos=(10,10))
        text11 = wx.StaticText(self.panel4, label="Liczba cytowan: ", pos=(10,30))
        text12 = wx.StaticText(self.panel4, label=" do ", pos=(10,50))
        text13 = wx.StaticText(self.panel4, label=" do ", pos=(10,180))
        """
        ########################################################################
        #  Bind
        ########################################################################
        
        self.but1.Bind(wx.EVT_BUTTON, self.GetData)
        self.dataList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClickCb)
        self.dataList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.selectOne)
        self.but5.Bind(wx.EVT_BUTTON, self.GetItem)
        self.but3.Bind(wx.EVT_BUTTON, self.backList)
        self.but6.Bind(wx.EVT_BUTTON, self.backList)
        self.but2.Bind(wx.EVT_BUTTON, self.GetChoice)
        self.but4.Bind(wx.EVT_BUTTON, self.getUserData)
        
        
        ########################################################################
        #  Metody sch.controler.py
        ########################################################################
        
        self.menu_title_by_id = {1:'Zaznacz',2:'Odznacz',3:'Zaznacz wszystko',4:'Odznacz wszystko',5:'Czysc liste'}
        
    def GetChoice(self, event):
        try:
            self.updateRecord(self.control.SetFilter(self.control.SetItems(), self.getChoice(), cDatabase.getUserFilter(self.session)))
        except ValueError:
            wx.MessageBox(u'Nie zaznaczono wartości do filtracji', 'Blad', wx.OK | wx.ICON_INFORMATION)
        else:
            self.dataList.DeleteAllItems()
            self.updateRecord(self.control.SetFilter(self.control.SetItems(), self.getChoice(), cDatabase.getUserFilter(self.session)))
    
        
    def backList(self, event):
        self.dataList.DeleteAllItems()
        self.updateRecord(self.control.SetItems())
    
        
    def RightClickCb(self, event):        
        menu = wx.Menu()
        for (id,title) in self.menu_title_by_id.items():
            menu.Append(id, title)
            wx.EVT_MENU(menu, id, self.MenuSelectionCb)        
        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        self.dataList.PopupMenu(menu, event.GetPoint())
        menu.Destroy() # destroy to avoid mem leak
            
    def MenuSelectionCb(self, event):
        operation = self.menu_title_by_id[event.GetId()]
        print operation
        if operation == 'Zaznacz':
            self.selectOne(self)
        elif operation == 'Odznacz':
            self.deselectOne()
        elif operation == 'Czysc liste':
            self.dataList.DeleteAllItems()
        elif operation == 'Zaznacz wszystko':
            self.selectAll()
        elif operation == 'Odznacz wszystko':
            self.deselectAll()
    
    def updateRecord(self, data):
        """
        """
        for i in range(len(data)):
            self.dataList.Append(data[i])
            
    def getChoice(self):
        h = self.ch4.GetCurrentSelection()
        if h == -1:
            raise ValueError
        print h
        return self.ch4Choices[h]
        
    def selectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i)
        
    def deselectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i, False)
            
    def selectOne(self, event):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i)

    def getItem(self):
        l = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                l.append(i)
        return l
            
    def deselectOne(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i, False)
        
    def printWord(self):
        txt1 = self.ctrl1.GetValue()
        txt2 = self.ctrl2.GetValue()
        txt3 = self.ctrl3.GetValue()
        txt4 = self.ctrl4.GetValue()
        txt5 = self.ctrl5.GetValue()
        txt6 = self.ctrl6.GetValue()
        txt7 = self.ctrl7.GetValue()
        txt8 = self.ctrl8.GetValue()
        print (txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8)
        return (txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8)
    
    def GetItem(self, event):
        """Pobieranie danych z wyszukiwania i tworzenie listy do przekazania dla menadzera publikacji"""
        self.control.SelectAllClick(self.getItem())
        
    def GetData(self, event):
        self.control.AddWord(self.printWord())
        self.updateRecord(self.control.SetItems())
        
        ########################################################################
        #  Metody cDatabase.py
        ########################################################################
        
    def getUserData(self, event):
        AllDict = {}
        UserDict = {}
        ColDict = {}
        FacDict = {}
        InsDict = {}
        
        dbCollege = self.cb1.GetValue()
        dbFaculty = self.cb2.GetValue()
        dbInstitut = self.cb3.GetValue()
        dbName = self.ctrl17.GetValue()
        dbSurname = self.ctrl18.GetValue()
        dbFilter = self.ctrl19.GetValue()
        
        if dbCollege == '' or dbFaculty == '' or dbInstitut == '' or dbName == '' or dbSurname == '' or dbFilter == '':
            wx.MessageBox(u'Wszystkie pola są wymagane', u'Błąd', wx.OK | wx.ICON_INFORMATION)
            return
        
        #print dbName
        ColDict['name'] = dbCollege
        FacDict['name'] = dbFaculty
        InsDict['name'] = dbInstitut
        UserDict['name'] = dbName
        UserDict['surname'] = dbSurname
        UserDict['filtr'] = dbFilter
        
        AllDict = {'college':ColDict,'faculty':FacDict,'institute':InsDict,'person':UserDict}
        
        print AllDict
        cDatabase.addUser(self.session,AllDict)
        
        self.ctrl17.SetValue('')
        self.ctrl18.SetValue('')
        self.ctrl19.SetValue('')
        
        
    def SetUserName(self):
        t = cDatabase.getUserName(self.session)
        return t
    
    def SetCollegeName(self):
        t = cDatabase.getCollegeName(self.session)
        return t
    
    def SetFacultyName(self):
        t = cDatabase.getFacultyName(self.session)
        return t
    
    def SetInstituteName(self):
        t = cDatabase.getInstituteName(self.session)
        return t
        
    def SetGroupName(self):
        t = cDatabase.getGroupName(self.session)
        return t
