import wx 
from wx.lib.pubsub import Publisher as pub
from src.lib.frames import MainFrame

class View(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, None)

        #1
        text1 = wx.StaticText(self.panel1, label="Wszystkie slowa:", pos=(5,5))
        self.ctrl1 = wx.TextCtrl(self.panel1, size=(200,20), pos=(95,2.5))
        #2
        text2 = wx.StaticText(self.panel1, label="Wyrazenie:", pos=(5,30))
        self.ctrl2 = wx.TextCtrl(self.panel1, size=(200,20), pos=(95,27.5))
        #3
        text3 = wx.StaticText(self.panel1, label="Jedno ze slow:", pos=(5,55))
        self.ctrl3 = wx.TextCtrl(self.panel1, size=(200,20), pos=(95,52.5))
        #4
        text4 = wx.StaticText(self.panel1, label="Bez slow:", pos=(5,80))
        self.ctrl4 = wx.TextCtrl(self.panel1, size=(200,20), pos=(95,77.5))
        #5
        text5 = wx.StaticText(self.panel1, label="Autor:", pos=(5,105))
        self.ctrl5 = wx.TextCtrl(self.panel1, size=(200,20), pos=(95,102.5))
        #6
        text6 = wx.StaticText(self.panel1, label="Dziedzina:", pos=(5,130))
        self.ctrl6 = wx.TextCtrl(self.panel1, size=(200,20), pos=(95,127.5))
        #7
        text7 = wx.StaticText(self.panel1, label="Rok od:", pos=(5,155))
        self.ctrl7 = wx.TextCtrl(self.panel1, size=(50,20), pos=(95,152.5))
        text8 = wx.StaticText(self.panel1, label=" do ", pos=(155,155))
        self.ctrl8 = wx.TextCtrl(self.panel1, size=(50,20), pos=(175,152.5))
        #button
        butt = wx.Button(self.panel1, -1, 'Pobierz', pos=(220,185))

        #self.wordCtrl = ctrl1
        
    def PrintWord(self):
        txt1 = self.ctrl1.GetValue()
        txt2 = self.ctrl2.GetValue()
        txt3 = self.ctrl3.GetValue()
        txt4 = self.ctrl4.GetValue()
        txt5 = self.ctrl5.GetValue()
        txt6 = self.ctrl6.GetValue()
        txt7 = self.ctrl7.GetValue()
        txt8 = self.ctrl8.GetValue()
        return (txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8)
