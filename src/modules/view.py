import wx 
from wx.lib.pubsub import Publisher as pub
from src.lib.frames import MainFrame
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)

class View(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, None)

        wx.StaticBox(self.panel1, -1, 'Wyszukiwanie Google Scholar', pos=(5, 5), size=(320, 200))
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
        butt = wx.Button(self.panel1, -1, label='Pobierz', pos=(245,177.5), name='btn1')

        self.list_ctrl = wx.ListCtrl(self.panel2, size=(300,100),
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, 'Tytul')
        self.list_ctrl.InsertColumn(1, 'Tytul')
        self.list_ctrl.InsertColumn(2, 'Tytul')
        
    def PrintWord(self):
        txt1 = self.ctrl1.GetValue()
        txt2 = self.ctrl2.GetValue()
        txt3 = self.ctrl3.GetValue()
        txt4 = self.ctrl4.GetValue()
        txt5 = self.ctrl5.GetValue()
        txt6 = self.ctrl6.GetValue()
        txt7 = self.ctrl7.GetValue()
        txt8 = self.ctrl8.GetValue()
        t = (txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8)
        return t
