# -*- coding: utf-8 -*-
import wx
import wx.lib.mixins.listctrl as listmix

from publikacja import PubDialog
from modules.men.menControler import mControler


class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin, listmix.TextEditMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
#        listmix.TextEditMixin.__init__(self)

class mView(wx.Panel, PubDialog):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        self.mcontrol = mControler()

        self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        globalBox = wx.BoxSizer( wx.VERTICAL )
        
        oneBox1 = wx.BoxSizer( wx.HORIZONTAL )
        
        oneBox11 = wx.BoxSizer( wx.VERTICAL )
        
        oneSB1 = wx.StaticBoxSizer( wx.StaticBox( self.panel, wx.ID_ANY, u"Dodaj Publikacje" ), wx.VERTICAL )
        
        oneBox111 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt1 = wx.StaticText( self.panel, wx.ID_ANY, u"Tytył:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt1.Wrap( -1 )
        oneBox111.Add( self.txt1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl1 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox111.Add( self.ctrl1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox111, 0, wx.EXPAND, 5 )
        
        oneBox112 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt2 = wx.StaticText( self.panel, wx.ID_ANY, u"Imie:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt2.Wrap( -1 )
        oneBox112.Add( self.txt2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl2 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 200,20 ), 0 )
        oneBox112.Add( self.ctrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox112, 0, wx.EXPAND, 5 )
        
        oneBox113 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt3 = wx.StaticText( self.panel, wx.ID_ANY, u"Nazwisko:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )
        oneBox113.Add( self.txt3, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl3 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox113.Add( self.ctrl3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox113, 0, wx.EXPAND, 5 )
        
        oneBox114 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt4 = wx.StaticText( self.panel, wx.ID_ANY, u"Rok:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt4.Wrap( -1 )
        oneBox114.Add( self.txt4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl4 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox114.Add( self.ctrl4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox114, 0, wx.EXPAND, 5 )
        
        oneBox115 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txt5 = wx.StaticText( self.panel, wx.ID_ANY, u"Wydawca:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt5.Wrap( -1 )
        oneBox115.Add( self.txt5, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.ctrl5 = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,20 ), 0 )
        oneBox115.Add( self.ctrl5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox115, 0, wx.EXPAND, 5 )
        
        oneBox117 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.but1 = wx.Button( self.panel, wx.ID_ANY, u"Pobierz", wx.DefaultPosition, wx.DefaultSize, 0 )
        oneBox117.Add( self.but1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        oneSB1.Add( oneBox117, 0, wx.ALIGN_RIGHT, 5 )
        
        
        oneBox11.Add( oneSB1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        oneBox1.Add( oneBox11, 0, wx.EXPAND|wx.ALL, 5 )
        
        
        globalBox.Add( oneBox1, 0, wx.EXPAND, 5 )
        
        twoBox1 = wx.BoxSizer( wx.VERTICAL )
        
        twoBox11 = wx.BoxSizer( wx.VERTICAL )
        
#        self.dataList = wx.ListCtrl( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_ICON )
        self.dataList = TestListCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,285 ), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, '', format=wx.LIST_FORMAT_CENTER, width=25)
        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=70)
        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=320)
        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=180)
        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=120)
        twoBox11.Add( self.dataList, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )
        
        
        twoBox1.Add( twoBox11, 1, wx.RIGHT|wx.EXPAND, 5 )
        
        twoBox12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.but5 = wx.Button( self.panel, wx.ID_ANY, u"Wyświetl wybrane", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        twoBox12.Add( self.but5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        self.but6 = wx.Button( self.panel, wx.ID_ANY, u"Przywróć liste", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.but6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        twoBox12.Add( self.but6, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        
        twoBox1.Add( twoBox12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        globalBox.Add( twoBox1, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )
        
        
        self.panel.SetSizer( globalBox )
        self.panel.Layout()
        globalBox.Fit( self.panel )
        
        ########################################################################
        #  Panel 2
        ########################################################################
        
        self.but5.Bind(wx.EVT_BUTTON, self.viewRecord)
#        self.but6.Bind(wx.EVT_BUTTON, self.editRecord)
        self.dataList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClickCb)
        self.dataList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.selectOne)
        
        self.menu_title_by_id = {1:'Zaznacz',2:'Odznacz',3:'Zaznacz wszystko',4:'Odznacz wszystko',5:'Czysc liste', 6:'Zapisz do bazy'}
        
    def test(self, event):
        tmp = self.dataList.GetEditControl()
        print tmp

    def viewRecord(self, event):
        self.dataList.DeleteAllItems()
        t = self.mcontrol.getRecords()
        self.updateRecord(t)
    
    def updateRecord(self, data):
        """
        """
        for i in range(len(data)):
            self.dataList.Append(data[i])
            
#    def editRecord(self, id):
#        t = self.mcontrol.getRecords()
#        for i in range(len(t)):
#            if i == id:
#                print id
#                tmp = self.dataList.GetItem()
#                #nie dziala, trzeba poprawic :P
#                print tmp
#                return id
    
    def RightClickCb(self, event):
        self.currentItem = event.m_itemIndex
        menu = wx.Menu()
        for (id,title) in self.menu_title_by_id.items():
            menu.Append(id, title)
            wx.EVT_MENU(menu, id, self.MenuSelectionCb)        
        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        self.dataList.PopupMenu(menu, event.GetPoint())
        menu.Destroy() # destroy to avoid mem leak
            
    def MenuSelectionCb(self, event):
        operation = self.menu_title_by_id[event.GetId()]
        print operation
        if operation == 'Zaznacz':
            self.selectOne(self)
        elif operation == 'Odznacz':
            self.deselectOne()
        elif operation == 'Czysc liste':
            self.dataList.DeleteAllItems()
        elif operation == 'Zaznacz wszystko':
            self.selectAll()
        elif operation == 'Odznacz wszystko':
            self.deselectAll()
        elif operation == 'Zapisz do bazy':
#            t = self.mcontrol.getRecords()
#            tmp = self.editRecord(self.currentItem)
#            updateList(tmp)
            print self.currentItem
            tmp =  self.mcontrol.updateList(self.currentItem)
#            print tmp
            self.editPubDial(tmp)
    
    def editPubDial(self, data):
        dlg = PubDialog()
#        print data
        dlg.m_textCtrl2.SetValue(data[2])
        dlg.m_textCtrl4.SetValue(data[3])
        dlg.m_textCtrl3.SetValue(str(data[1]))
#        dlg.m_choice1.SetStringSelection(data[4])
        dlg.m_textCtrl5.SetValue(str(data[4]))
#        dlg.m_textCtrl6.SetValue(data[6])
#        dlg.m_textCtrl7.SetValue(data[7])
#        dlg.m_choice2.SetStringSelection(data[8])
#        print data
        dlg.ShowModal()

    def selectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i)
        
    def deselectAll(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            self.dataList.CheckItem(i, False)
            
    def selectOne(self, event):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i)
    
    def deselectOne(self):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsSelected(i):
                self.dataList.CheckItem(i, False)
