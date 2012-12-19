# -*- coding: utf-8 -*-
import wx
from model import Model
from view import View

class Controler:
    def __init__(self):
        self.model = Model()
        self.view = View(None)
        self.view.but1.Bind(wx.EVT_BUTTON, self.AddWord)
        self.view.but2.Bind(wx.EVT_BUTTON, self.ClearAll)
        self.view.but3.Bind(wx.EVT_BUTTON, self.SelectAll)
        self.view.but4.Bind(wx.EVT_BUTTON, self.DeselectAll)
        self.view.but5.Bind(wx.EVT_BUTTON, self.SelectOne)
        self.view.but6.Bind(wx.EVT_BUTTON, self.DeselectOne)
        self.view.Show()

    def ClearAll(self, event):
        self.view.dataList.DeleteAllItems()
        self.model.fulllist = []

    def SelectAll(self, event):
        self.view.selectAll()

    def DeselectAll(self, event):
        self.view.deselectAll()
        
    def SelectOne(self, event):
        self.view.selectOne()
        
    def DeselectOne(self, event):
        self.view.deselectOne()
    
    def AddWord(self, event):
        self.model.addWord(self.view.printWord())
        self.model.downloadData()
        self.view.updateRecord(self.model.allRecords())
        self.model.all_item = 0
