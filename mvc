# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import sys
import wx
from bs4 import BeautifulSoup
from wx.lib.pubsub import Publisher as pub

class Model:
    def __init__(self):
        self.item = {'query': "", 'exact': "", 'oneof': "", 'without': "",
                     'author': "Leszek+Wojnar", 'pub': "", 'ylow': "", 'yhigh': ""}

    def addWord(self, value):
        self.item['query'] = value
        #pub.sendMessage("Word", self.item)
        print self.item
        
class View(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Moja aplikacja")

        #panel = wx.Panel(self)
        #sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self, label="Podaj slowo", pos=(10,15))
        ctrl = wx.TextCtrl(self, pos=(80,10))
        butt = wx.Button(self, -1, 'Pobierz', pos=(10,40))
        #sizer.Add(text, 0, wx.EXPAND | wx.ALL)
        #sizer.Add(ctrl, 0, wx.EXPAND | wx.ALL)
        #sizer.Add(butt, 0, wx.EXPAND | wx.ALL)

        self.wordCtrl = ctrl
        #self.SetSizer(sizer)

    def PrintWord(self):
        txt = self.wordCtrl.GetValue()
        self.wordCtrl.SetValue(txt)
        #print txt
        return txt

class Controler:
    def __init__(self, app):
        self.model = Model()
        self.view = View(None)
        #self.view.PrintWord(self.model.item)
        self.view.Bind(wx.EVT_BUTTON, self.AddWord)
        #pub.subscribe(self.WordChange, "Word")

        self.view.Show()

    def AddWord(self, evt):
        self.model.addWord(str(self.view.PrintWord()))

    #def WordChange(self, message):
        #self.view.PrintWord()
"""
    def AddMoney(self, evt):
        self.model.addMoney(10)

    def RemoveMoney(self, evt):
        self.model.removeMoney(10)

    def MoneyChanged(self, message):
        self.view1.SetMoney(message.data)
"""
if __name__ == "__main__":
    app = wx.App(False)
    controller = Controler(app)
    app.MainLoop()
