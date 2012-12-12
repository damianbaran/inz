import wx
from model import Model
from view import View
from wx.lib.pubsub import Publisher as pub

class Controler:
    def __init__(self):
        self.model = Model()
        self.view = View(None)
        #self.view.PrintWord(self.model.item)
        self.view.but1.Bind(wx.EVT_BUTTON, self.AddWord)
        self.view.but2.Bind(wx.EVT_BUTTON, self.clearAll)
        self.view.but3.Bind(wx.EVT_BUTTON, self.selectAll)
        self.view.but4.Bind(wx.EVT_BUTTON, self.deselectAll)
        self.view.Show()

    def clearAll(self, event):
        self.view.dataList.DeleteAllItems()
        self.model.fulllist = []

    def selectAll(self, event):
        self.view.dataList.SelectAll()

    def deselectAll(self, event):
        self.view.dataList.DeselectAll()

    def AddWord(self, event):
        self.model.addWord(self.view.printWord())
        self.model.downloadData()
        self.view.updateRecord(self.model.allRecords())
