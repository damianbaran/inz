import wx
from model import Model
from view import View
from wx.lib.pubsub import Publisher as pub

class Controler:
    def __init__(self):
        self.model = Model()
        self.view = View(None)
        #self.view.PrintWord(self.model.item)
        self.view.Bind(wx.EVT_BUTTON, self.AddWord)
        #self.view.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        #pub.subscribe(self.WordChange, "Word")

        self.view.Show()

    #def OnKeyDown(self, event):
    #    keycode = event.GetKeyCode()
    #    if keycode == wx.WXK_ENTER:
    #        self.AddWord()
    #    event.Skip()

    def AddWord(self, event):
        button = event.GetEventObject()
        b = button.GetName()
        if b =="btn1":
            self.model.addWord(self.view.PrintWord())
            self.model.downloadData()

    #def WordChange(self, message):
    #    self.view.PrintWord()
