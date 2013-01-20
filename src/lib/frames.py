# -*- coding: utf-8 -*-
import wx

class MainFrame(wx.Frame):
    def __init__(self, master):
        wx.Frame.__init__(self, None, title="Moja aplikacja", size=(1024,700))

        menu = wx.MenuBar()
        files = wx.Menu()
        edit = wx.Menu()
        helps = wx.Menu()
        files.Append(101, '&Otworz', 'Open document')
        files.Append(102, '&Zapisz', 'Save document')
        files.AppendSeparator()
        quit = wx.MenuItem(files,105,'&Wyjdz\tCtrl+Q','Quit Application')
        files.AppendItem(quit)
        edit.Append(201, 'Edytuj')
        edit.Append(202, 'Szukaj')
        submenu = wx.Menu()
        submenu.Append(301,'1')
        submenu.Append(302,'2')
        submenu.Append(303,'3')
        edit.AppendMenu(203, 'Lista', submenu)
        helps.Append(401, 'Pomoc')
        helps.Append(402, 'O aplikacji')

        menu.Append(files, '&Plik')
        menu.Append(edit, '&Edycja')
        menu.Append(helps, '&Pomoc')

        self.SetMenuBar(menu)
        self.CreateStatusBar()

        #self.frame_top = wx.Frame(self, None, title='Aaa' size=(320,220))
        #top panel
        #self.panel = wx.Panel(self, pos=(0,0), size=(1024,25))
        #self.title = 'Google Scholar Search'
        #wx.StaticText(self.panel, -1, self.title, pos=(10,5), style=wx.ALIGN_CENTER)
        
        self.panel1 = wx.Panel(self, -1, pos=(0,0), size=(330,210))
        self.panel2 = wx.Panel(self, -1, pos=(0,210), size=(1024,410))
        self.panel3 = wx.Panel(self, -1, pos=(330,0), size=(330,210))
        

