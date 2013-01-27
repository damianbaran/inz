# -*- coding: utf-8 -*-
import wx
import wx.lib.mixins.listctrl as listmix
from modules.sch.schControler import sControler


class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class mView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        self.scontrol = sControler()

        ########################################################################
        #  Panel 1
        ########################################################################
        self.panel1 = wx.Panel(self, -1, pos=(0,0), size=(330,210))
        self.panel2 = wx.Panel(self, -1, pos=(0,210), size=(1024,410))
        self.panel3 = wx.Panel(self, -1, pos=(330,0), size=(330,210))
        self.panel4 = wx.Panel(self, -1, pos=(660,0), size=(360,210))

        
        wx.StaticBox(self.panel1, -1, 'Wyszukiwanie Google Scholar',
                     pos=(5, 5), size=(320, 200))
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
        self.butt = wx.Button(self.panel1, -1, label='Pobierz', pos=(245,177.5))
        
        ########################################################################
        #  Panel 2
        ########################################################################
        
            
        """        
    def updateRecord(self, data):
        """
        """
        #self.dataList.SetObjects(data)
        for i in range(len(data)):
            self.dataList.Append(data[i])
            
    def getChoice(self):
        h = self.ch.GetCurrentSelection()
        if h == -1:
            raise ValueError
        print h
        return self.tmp[h]
        
    def selectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i)
        
    def deselectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i, False)
            
    def selectOne(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i)

    def selectOneClick(self):
        l = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                l.append(i)
        #print l
        return l
            
    def deselectOne(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i, False)
        
    def printWord(self):
        txt1 = self.ctrl1.GetValue()
        txt2 = self.ctrl2.GetValue()
        txt3 = self.ctrl3.GetValue()
        txt4 = self.ctrl4.GetValue()
        txt5 = self.ctrl5.GetValue()
        txt6 = self.ctrl6.GetValue()
        txt7 = self.ctrl7.GetValue()
        txt8 = self.ctrl8.GetValue()
        return (txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8)
        """
