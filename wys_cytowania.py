# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import os
import wx.xrc
import cDatabase
import webbrowser
import wx.lib.mixins.listctrl as listmix
from wx.lib.pubsub import Publisher
from dodaj_pub import CitePubDialog

###########################################################################
## Class CiteDialog
###########################################################################

class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class CiteDialog ( wx.Dialog ):
    def __init__( self ):
        wx.Dialog.__init__ ( self, None, id = wx.ID_ANY, title = u"Menadźer łączenia publikacji", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.handlerweb = webbrowser.get()
        self.session = cDatabase.connectDatabase()
        
        ico = wx.Icon('icon/citpub.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_toolBar2 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_FLAT  ) 
        addall = self.m_toolBar2.AddLabelTool( 1, u"tool", wx.Bitmap( u"icon/globe.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Wyświetl wszystkie cytowania", wx.EmptyString, None ) 
        addone = self.m_toolBar2.AddLabelTool( 2, u"tool", wx.Bitmap( u"icon/browser.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Wyświetl wybrana publikację", wx.EmptyString, None ) 
        clear = self.m_toolBar2.AddLabelTool( 3, u"tool", wx.Bitmap( u"icon/clear.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Czyść listę", wx.EmptyString, None ) 
        backlist = self.m_toolBar2.AddLabelTool( 6, u"tool", wx.Bitmap( u"icon/back.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Przywróć wybrane publikacje", wx.EmptyString, None ) 
        self.m_toolBar2.AddSeparator()
        
        merge = self.m_toolBar2.AddLabelTool( 4, u"tool", wx.Bitmap( u"icon/merge.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Połacz wybrane publikacje", wx.EmptyString, None ) 
        addpub = self.m_toolBar2.AddLabelTool( 7, u"tool", wx.Bitmap( u"icon/globe.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Dodaj publikację", wx.EmptyString, None ) 
        delpub = self.m_toolBar2.AddLabelTool( 5, u"tool", wx.Bitmap( u"icon/delete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Usuń wybrane publikacje z bazy danych", wx.EmptyString, None ) 
        delpublist = self.m_toolBar2.AddLabelTool( 8, u"tool", wx.Bitmap( u"icon/dellist.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Usuń wybrane publikacje z listy", wx.EmptyString, None ) 
        
        self.m_toolBar2.Realize() 
        
        bSizer1.Add( self.m_toolBar2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Edytuj połączoną publikację:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer3.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.pubcit = cDatabase.getMergePub(self.session)
        self.m_comboBox1Choices = self.pubcit.values()
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, self.m_comboBox1Choices, 0 )
#        self.m_comboBox1.SetSelection( 0 )
        bSizer3.Add( self.m_comboBox1, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        
        bSizer13.Add( bSizer3, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
#        self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
        self.dataList = TestListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, u'ID', format=wx.LIST_FORMAT_CENTER, width=23)
        self.dataList.InsertColumn(1, u'Cytowań', format=wx.LIST_FORMAT_RIGHT, width=60)
        self.dataList.InsertColumn(2, u'Tytuł', format=wx.LIST_FORMAT_LEFT, width=130)
        self.dataList.InsertColumn(3, u'Autor', format=wx.LIST_FORMAT_LEFT, width=100)
        self.dataList.InsertColumn(4, u'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, u'Źródło', format=wx.LIST_FORMAT_LEFT, width=100)
        self.dataList.InsertColumn(6, u'DOI', format=wx.LIST_FORMAT_LEFT, width=100)
        bSizer13.Add( self.dataList, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
##################################################
## Bind
###################################################
        
        self.Bind( wx.EVT_TOOL, self.openLinkCit, addall )
        self.Bind( wx.EVT_TOOL, self.openLinkPub, addone )
        self.Bind( wx.EVT_TOOL, self.clearData, clear )
        self.Bind( wx.EVT_TOOL, self.mergePub, merge )
        self.Bind( wx.EVT_TOOL, self.deletePub, delpub )
        self.Bind( wx.EVT_TOOL, self.backListPub, backlist )
        self.Bind( wx.EVT_TOOL, self.addPub, addpub )
        self.Bind( wx.EVT_TOOL, self.delPub, delpublist )
        self.Bind( wx.EVT_CLOSE, self.close )
        self.m_comboBox1.Bind(wx.EVT_COMBOBOX,  self.editPubCit)
        self.dataList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClickCb)
        self.dataList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.selectOne)

###################################################
## Metody
###################################################
        self.data = []
        self.id = 0
        self.menu_title_by_id = {1:'Zaznacz',2:'Odznacz',3:'Zaznacz wszystko',4:'Odznacz wszystko'}
        
        Publisher().subscribe(self.change_data, 'change_data')
        Publisher().subscribe(self.update_data, 'update_data')
    
    def close(self, event):
        Publisher().unsubAll('update_data')
        self.Destroy()
    
    def update_data(self, msg):
        self.data += msg.data
    
    def editPubCit(self, event):
#        t = cDatabase.getMergePub(self.session)
#        print self.pubcit
#        print len(self.pubcit)
        k = self.pubcit.keys()
        for i in range(len(k)):
            if self.pubcit.get(k[i]) == self.m_comboBox1.GetStringSelection():
                self.id = k[i]
#                print id
                self.data = cDatabase.pubCitMerge(self.session, self.id)
        self.updateRecord()
        self.id
        num = self.dataList.GetItemCount()
        for i in range(num):
            if int(self.dataList.GetItemText(i)) == int(self.id):
                self.dataList.SetItemBackgroundColour(i, "yellow")
    
    def addPub(self, event):
        print Publisher().getMessageCount()
        dlg = CitePubDialog()
        dlg.ShowModal()
        self.updateRecord()
    
    def delPub(self, event):
        tmp = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                print i
                print len(self.data)
                t = self.data[i]
                tmp.append(t)
        for i in range(len(tmp)):
            t = tmp[i]
            self.data.remove(t)
    
    def deletePub(self, event):
        tmp = []
        base = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                print i
                print len(self.data)
                t = self.data[i]
                l = self.dataList.GetItemText(i)
                l = int(l)
                base.append(l)
                tmp.append(t)
        print base
        for i in range(len(tmp)):
            t = tmp[i]
            self.data.remove(t)
        if self.id != 0:
            for i in range(len(base)):
                cDatabase.deleteCite(self.session, base[i], self.id)
        wx.MessageBox(u'Poprawnie usunięto wybrane publikacje', u'Sukces', wx.OK | wx.ICON_INFORMATION)
        self.dataList.DeleteAllItems()
        self.updateRecord()
        
        self.m_comboBox1Choices = cDatabase.getMergePub(self.session).values()
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(self.m_comboBox1Choices)
        
    
    def mergePub(self, event):
        public = []
        result = []
        tmp = []
        allpub = []
        n = 0
        numcit = 0
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                tmp.append(i)
        
        if len(tmp) == 1:
            for i in range(num):
                if self.dataList.IsChecked(i):
                    c = self.dataList.GetItemText(i)
                    c = int(c)
#                    print str(c) + ' check'
                    result.append(c)
            for i in range(num):
                if self.dataList.IsChecked(i):
                    pass
                else:
                    u = self.dataList.GetItemText(i)
                    u = int(u)
#                    print str(u) + ' uncheck'
                    result.append(u)
            
            id_top = result[0]
            print len(result)
            for i in range(len(result)):    #pobieranie wszystkich powiazanych publikacji z bazy
                t = cDatabase.getMergePubData(self.session, result[i])
                numcit += t[1]
                x = (t[7], t[1], result[i], id_top)
                allpub.append(x)
            for i in range(len(allpub)):
                t = allpub[i]
                c = (t[0], numcit, t[2], t[3])
                
                cDatabase.saveCite(self.session, c)
            wx.MessageBox(u'Poprawnie połaczono wybrane publikacje', u'Sukces', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(u'Nie wybrałeś publikacji wiodącej\nbądź wybrałeś więcej niż jedną', u'Błąd', wx.OK | wx.ICON_ERROR)
        
        self.pubcit = cDatabase.getMergePub(self.session)
        
        self.m_comboBox1Choices = cDatabase.getMergePub(self.session).values()
        self.m_comboBox1.Clear()
        self.m_comboBox1.AppendItems(self.m_comboBox1Choices)
#        print result
    
    def change_data(self, msg):
        self.data = msg.data
#        msg = []
#        print '--------------'
#        print self.data
    
    def openLinkCit(self, event):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                self.getLinkCit(i)
            
    def getLinkCit(self, id):
        t = self.dataList.GetItemCount()
        print t
        print id
        for i in range(t):
            if i == id:
                tmp = self.data[i]
                t = 'http://' + tmp[7]
                if tmp[7] == 'Brak':
                    wx.MessageBox(u'Brak adresu URL do artykułu', u'Bład!', wx.OK | wx.ICON_INFORMATION)
                else:
                    self.handlerweb.open_new_tab(t)
    
    def openLinkPub(self, event):
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                self.getLinkPub(i)
            
    def getLinkPub(self, id):
        t = self.dataList.GetItemCount()
        print t
        print id
        for i in range(t):
            if i == id:
                tmp = self.data[i]
                t = 'http://' + tmp[8]
                if tmp[8] == 'Brak':
                    wx.MessageBox(u'Brak adresu URL do artykułu', u'Bład!', wx.OK | wx.ICON_INFORMATION)
                else:
                    self.handlerweb.open_new_tab(t)
    
    def backListPub(self, event):
        self.updateRecord()
    
    def updateRecord(self):
        """
        """
        self.dataList.DeleteAllItems()
        for i in range(len(self.data)):
            self.dataList.Append(self.data[i])
        num = self.dataList.GetItemCount()
        if self.id != 0:
            for i in range(num):
                if int(self.dataList.GetItemText(i)) == int(self.id):
                    self.dataList.SetItemBackgroundColour(i, "yellow")
    
    def clearData(self, event):
        self.dataList.DeleteAllItems()
    
    def RightClickCb(self, event):        
        self.currentItem = event.m_itemIndex
        menu = wx.Menu()
        for (id,title) in self.menu_title_by_id.items():
            menu.Append(id, title)
            wx.EVT_MENU(menu, id, self.MenuSelectionCb)        
        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        self.dataList.PopupMenu(menu, event.GetPoint())
        menu.Destroy()
    
    def MenuSelectionCb(self, event):
        operation = self.menu_title_by_id[event.GetId()]
        print operation
        if operation == 'Zaznacz':
            self.selectOne(self)
        elif operation == 'Odznacz':
            self.deselectOne()
        elif operation == 'Zaznacz wszystko':
            self.selectAll()
        elif operation == 'Odznacz wszystko':
            self.deselectAll()
    
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

if __name__ == "__main__":
    app = wx.App(False)
    controller = CiteDialog()
    controller.Show()
    app.MainLoop()
    
