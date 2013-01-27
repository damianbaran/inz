# -*- coding: utf-8 -*-
import wx
import time
from menModel import mModel
#from menView import mView

class mControler():
    """controler dla menadzera publikacji"""
    def __init__(self):
        
        
#        threading.Thread.__init__(self)
#        self.model = Model()
#        self.view = View_men(None)
        """
        self.view.but1.Bind(wx.EVT_BUTTON, self.AddWord)
        #self.view.but2.Bind(wx.EVT_BUTTON, self.ClearAll)
        #self.view.but3.Bind(wx.EVT_BUTTON, self.SelectAll)
        #self.view.but4.Bind(wx.EVT_BUTTON, self.DeselectAll)
        self.view.dataList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.SelectOne)
        self.view.but7.Bind(wx.EVT_BUTTON, self.SelectAllClick)
        self.view.but8.Bind(wx.EVT_BUTTON, self.GetChoice)
        self.view.but9.Bind(wx.EVT_BUTTON, self.backList)
        self.view.but10.Bind(wx.EVT_BUTTON, self.backList)
        self.view.dataList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClickCb)
        """
#        self.view.Centre()
#        self.view.Show()        
        """
    def GetChoice(self, event):
        #self.model.filtruj(self.model.fulllist, self.view.getChoice())
        try:
            self.view.updateRecord(self.model.filtruj(self.model.fulllist, self.view.getChoice()))
        except ValueError:
            wx.MessageBox('Nie zaznaczono wartosci do filtracji', 'Blad', wx.OK | wx.ICON_INFORMATION)
        else:
            self.view.dataList.DeleteAllItems()
            self.view.updateRecord(self.model.filtruj(self.model.fulllist, self.view.getChoice()))

    def backList(self, event):
        self.view.dataList.DeleteAllItems()
        self.view.updateRecord(self.model.allRecords())
        
    def RightClickCb(self, event):        
        ### 2. Launcher creates wxMenu. ###
        menu = wx.Menu()
        for (id,title) in self.view.menu_title_by_id.items():
            ### 3. Launcher packs menu with Append. ###
            menu.Append(id, title)
            ### 4. Launcher registers menu handlers with EVT_MENU, on the menu. ###
            wx.EVT_MENU(menu, id, self.MenuSelectionCb)
    
        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        self.view.dataList.PopupMenu(menu, event.GetPoint())
        menu.Destroy() # destroy to avoid mem leak
        
    def MenuSelectionCb( self, event ):
        operation = self.view.menu_title_by_id[ event.GetId() ]
        print operation
        if operation == 'Zaznacz':
            self.view.selectOne()
        elif operation == 'Odznacz':
            self.view.deselectOne()
        elif operation == 'Czysc liste':
            self.view.dataList.DeleteAllItems()
        elif operation == 'Zaznacz wszystko':
            self.view.selectAll()
        elif operation == 'Odznacz wszystko':
            self.view.deselectAll()
            
    def ClearAll(self, event):
        self.view.dataList.DeleteAllItems()
        #self.model.fulllist = []

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
        #self.view.statusbar.SetStatusText('Trwa pobieranie danch... Prosze czekac')
        self.view.but1.Disable()
        self.model.addWord(self.view.printWord())
        self.model.fulllist = []
        time.sleep(1)
        self.model.downloadData()
        self.view.updateRecord(self.model.allRecords())
        self.model.all_item = 0
        self.view.but1.Enable()
        #self.view.statusbar.SetStatusText('Dane zostaly pobrane')
        """
        
