import wx 
from wx.lib.pubsub import Publisher as pub
#from plikmvc import View

class MainFrame(wx.Frame):
    def __init__(self, master):
        wx.Frame.__init__(self, None, title="Moja aplikacja", size=(640,480))

        menu = wx.MenuBar()
        files = wx.Menu()
        edit = wx.Menu()
        helps = wx.Menu()
        files.Append(101, '&Open', 'Open document')
        files.Append(102, '&Save', 'Save document')
        files.AppendSeparator()
        quit = wx.MenuItem(files,105,'&Quit\tCtrl+Q','Quit Application')
        files.AppendItem(quit)
        edit.Append(201, 'Edit')
        edit.Append(202, 'Search')
        submenu = wx.Menu()
        submenu.Append(301,'1')
        submenu.Append(302,'2')
        submenu.Append(303,'3')
        edit.AppendMenu(203, 'Lista', submenu)
        helps.Append(401, 'Help')
        helps.Append(402, 'About')

        menu.Append(files, '&File')
        menu.Append(edit, '&Edit')
        menu.Append(helps, '&Help')

        self.SetMenuBar(menu)
        self.CreateStatusBar()

        self.panel1 = wx.Panel(self, pos=(0,0), size=(300,25))
        #self.panel2 = wx.Panel(self, pos=(0,25), size=(300,25))
