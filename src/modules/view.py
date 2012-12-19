# -*- coding: utf-8 -*-
import wx
from src.lib.frames import MainFrame
import wx.lib.mixins.listctrl as listmix
from ObjectListView import ObjectListView, ColumnDefn

class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class View(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, None)

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
        self.but1 = wx.Button(self.panel1, -1, label='Pobierz', pos=(245,177.5))
        
        
        self.dataList = TestListCtrl(self.panel2, pos=(5,5), size=(780,400),
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, '', format=wx.LIST_FORMAT_CENTER, width=25)
        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=70)
        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=220)
        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=150)
        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=100)
        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=140)

        self.but2 = wx.Button(self.panel2, -1, label='Usun Wszystko', pos=(790,5))
        self.but3 = wx.Button(self.panel2, -1, label='Zaznacz Wszystko', pos=(790,30))
        self.but4 = wx.Button(self.panel2, -1, label='Odznacz Wszystko', pos=(790,55))
        self.but5 = wx.Button(self.panel2, -1, label='Zaznacz Rekord', pos=(790,80))
        self.but6 = wx.Button(self.panel2, -1, label='Odznacz Rekord', pos=(790,105))
        
    def updateRecord(self, data):
        """
        """
        #self.dataList.SetObjects(data)
        for i in range(len(data)):
            self.dataList.Append(data[i])
            
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
