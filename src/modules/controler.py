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
        self.view.but7.Bind(wx.EVT_BUTTON, self.SelectAllClick)
        self.view.but8.Bind(wx.EVT_BUTTON, self.GetChoice)
        self.view.Show()
        
    def GetChoice(self, event):
        #self.model.filtruj(self.model.fulllist, self.view.getChoice())
        self.view.dataList.DeleteAllItems()
        self.view.updateRecord(self.model.filtruj(self.model.fulllist, self.view.getChoice()))

    def ClearAll(self, event):
        self.view.dataList.DeleteAllItems()
        self.model.fulllist = []

    def SelectAll(self, event):
        self.view.selectAll()
        #self.model.addSelectAllList(self.view.selectAll())

    def DeselectAll(self, event):
        self.view.deselectAll()
        #self.model.remSelectAllList(self.view.deselectAll())
        
    def SelectOne(self, event):
        self.view.selectOne()
        #self.model.addSelectList(self.view.selectOne())
        
    def DeselectOne(self, event):
        self.view.deselectOne()
        #self.model.remSelectList(self.view.deselectOne())
        
    def SelectAllClick(self, event):
        #self.view.selectOneClick()
        self.model.selectingString(self.view.selectOneClick())
    
    def AddWord(self, event):
        self.model.addWord(self.view.printWord())
        self.model.downloadData()
        self.view.updateRecord(self.model.allRecords())
        self.model.all_item = 0
