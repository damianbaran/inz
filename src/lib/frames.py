import wx 
from wx.lib.pubsub import Publisher as pub
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
#from plikmvc import View

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)

class MainFrame(wx.Frame):
    def __init__(self, master):
        wx.Frame.__init__(self, None, title="Moja aplikacja", size=(1024,700))

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

        #self.frame_top = wx.Frame(self, None, title='Aaa' size=(320,220))
        #top panel
        #self.panel = wx.Panel(self, pos=(0,0), size=(1024,25))
        #self.title = 'Google Scholar Search'
        #wx.StaticText(self.panel, -1, self.title, pos=(10,5), style=wx.ALIGN_CENTER)
        self.panel1 = wx.Panel(self, -1, pos=(0,0), size=(330,210))
        self.panel2 = wx.Panel(self, -1, pos=(0,220), size=(450,400))
