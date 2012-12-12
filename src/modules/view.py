import wx
from wx.lib.pubsub import Publisher as pub
from src.lib.frames import MainFrame
from ObjectListView import ObjectListView, ColumnDefn


class View(MainFrame):
    def __init__(self, parent):
        #ListViewFrame.__init__(self, None)
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
        """
        self.list_ctrl = wx.ListCtrl(self.panel2, size=(300,100),
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, 'Tytul')
        self.list_ctrl.InsertColumn(1, 'Tytul')
        self.list_ctrl.InsertColumn(2, 'Tytul')
        self.but2 = wx.Button(self.panel2, -1, label='Pobierz', pos=(10,110), name='btn1')
        """
 
        self.dataList = ObjectListView(self.panel2, -1,
                                      style=wx.LC_REPORT|wx.SUNKEN_BORDER,
                                      pos=(5,5), size=(780,400))
        self.citColumn = ColumnDefn("Cytowan", "right", 70, "cittxt")
        self.titleColumn = ColumnDefn("Tytul", "left", 300, "title")
        self.authorColumn = ColumnDefn("Autor", "left", 150, "author")
        self.yearColumn = ColumnDefn("Rok", "right", 50, "year")        
        self.publishColumn = ColumnDefn("Wydawca", "left", 150, "publish")
        self.setRecord()
        #self.dataList.CreateCheckStateColumn()
        #self.dataOlv.InstallCheckStateColumn(self.titleColumn)
 
        # Allow the cell values to be edited when double-clicked
        self.dataList.cellEditMode = ObjectListView.CELLEDIT_SINGLECLICK

        self.but2 = wx.Button(self.panel2, -1, label='Usun Wszystko',
                              pos=(790,5))
        self.but3 = wx.Button(self.panel2, -1, label='Zaznacz Wszystko',
                              pos=(790,30))
        self.but4 = wx.Button(self.panel2, -1, label='Odznacz Wszystko', pos=(790,55))    

    def setRecord(self, data=None):
        self.dataList.SetColumns([
            self.citColumn,
            self.titleColumn,
            self.authorColumn,
            self.yearColumn,
            self.publishColumn
        ])
 
    def updateRecord(self, data):
        """
        """
        self.dataList.SetObjects(data)
        
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
