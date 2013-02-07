# -*- coding: utf-8 -*-
import wx
import wx.lib.mixins.listctrl as listmix
import cDatabase
from publikacja import PubDialog
from grupa import GroupDialog
from wydawca import JourDialog


class TestListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class bView(wx.Panel, PubDialog):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        self.session = cDatabase.connectDatabase()
        listSearch = [u'Autor', u'AutorID', u'DOI', u'Grupa', u'ISSN', u'Rok', u'Tytul', u'Wydawca']

        ########################################################################
        #  Panel 1
        ########################################################################
        self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        globalBox = wx.BoxSizer( wx.VERTICAL )
        
        twoBox1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText12 = wx.StaticText( self.panel, wx.ID_ANY, u"Wyszukaj", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer24.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice31Choices = listSearch
        self.m_choice31 = wx.Choice( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice31Choices, 0 )
        self.m_choice31.SetSelection( 0 )
        bSizer24.Add( self.m_choice31, 0, wx.ALL, 5 )
        
        self.m_searchCtrl1 = wx.SearchCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.m_searchCtrl1.ShowSearchButton( True )
        self.m_searchCtrl1.ShowCancelButton( False )
        bSizer24.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )
        
        
        twoBox1.Add( bSizer24, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )
        
        twoBox11 = wx.BoxSizer( wx.VERTICAL )
        
#        self.dataList = wx.ListCtrl( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_ICON )
        self.dataList = TestListCtrl(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 995,490 ), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.dataList.InsertColumn(0, 'ID', format=wx.LIST_FORMAT_CENTER, width=50)
        self.dataList.InsertColumn(1, 'Cytowan', format=wx.LIST_FORMAT_LEFT, width=70)
        self.dataList.InsertColumn(2, 'Tytul', format=wx.LIST_FORMAT_LEFT, width=320)
        self.dataList.InsertColumn(3, 'Autor', format=wx.LIST_FORMAT_LEFT, width=180)
        self.dataList.InsertColumn(4, 'Rok', format=wx.LIST_FORMAT_RIGHT, width=50)
        self.dataList.InsertColumn(5, 'Wydawca', format=wx.LIST_FORMAT_LEFT, width=120)
        twoBox11.Add( self.dataList, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
        
        
        twoBox1.Add( twoBox11, 1, wx.EXPAND, 5 )
        
        twoBox12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.but5 = wx.Button( self.panel, wx.ID_ANY, u"Dodaj wybrane", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        twoBox12.Add( self.but5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.RIGHT, 5 )
        
        self.but6 = wx.Button( self.panel, wx.ID_ANY, u"Przywróć liste", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.but6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        twoBox12.Add( self.but6, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.RIGHT, 5 )
        
        
        twoBox1.Add( twoBox12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        globalBox.Add( twoBox1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.panel.SetSizer( globalBox )
        self.panel.Layout()
        globalBox.Fit( self.panel )
        
#############################################################
## Bindowanie
#############################################################
        
        self.m_searchCtrl1.Bind(wx.EVT_TEXT_ENTER, self.searchPub)
        self.dataList.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.selectOne)
        self.dataList.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClickCb)
        self.but5.Bind(wx.EVT_BUTTON, self.GetItem)
#        PubDialog().m_button3.Bind(wx.EVT_BUTTON, self.getEditRecord)

        #Pozycje dal popmenu
        self.menu_title_by_id = {1:'Zaznacz',2:'Odznacz', 3:'Edytuj rekord', 4:u'Usuń rekord',5:'Zaznacz wszystko',6:'Odznacz wszystko',7:'Czysc liste'}

#############################################################
## Przekazywanie rekordow do modelu menadzera
#############################################################

    def getItem(self):
        """Pobiera ID wybranych rekordow do przeniesienia do menadzera zadan"""
        l = []
        num = self.dataList.GetItemCount()
        for i in range(num):
            if self.dataList.IsChecked(i):
                t = self.dataList.GetItemText(i)
                l.append(t)
        return l
        
    def GetItem(self, event):
        """Pobieranie danych z wyszukiwania bazy i tworzenie listy do przekazania dla menadzera publikacji"""
        cDatabase.getChoiceRecord(self.session, self.getItem())
        
#############################################################
## Metody
#############################################################

        
    def searchPub(self,  event):
        """Funkcja wyszukuje wartości w bazie podane przez użytkownika"""
        self.dataList.DeleteAllItems() #Ksowanie listy w wx.ListCtrl
        t = self.m_searchCtrl1.GetValue() #Pobieranie wartości wpisanej przez użytkownika
        d = self.m_choice31.GetStringSelection() #pobieranie wartości z listy wybranej przez użytkownika
        tmp = cDatabase.getRecords(self.session, d, t) #zapytanie do bazy, zwracajace szukane elementy
        self.updateRecord(tmp) #wyswietlenie wartosci w ListCtrl
        
#    def getEditRecord(self, event):
#        dlg = PubDialog()
#        t1 = dlg.m_textCtrl2.GetValue()
#        print t1

       
    def editRecord(self, id, data):
        """Ustawienia wartości z zapytania w kontrolkach do edycji wybranej publikacji"""
        dlg = PubDialog()
        dlg.m_staticText1.SetLabel('Edytujesz rekord o nr. '+str(data[0]))
        dlg.m_textCtrl2.SetValue(data[1])
        dlg.m_textCtrl4.SetValue(data[2])
        dlg.m_textCtrl3.SetValue(str(data[3]))
        dlg.m_choice1.SetStringSelection(data[4])
        dlg.m_textCtrl5.SetValue(str(data[5]))
        dlg.m_textCtrl6.SetValue(data[6])
        dlg.m_textCtrl7.SetValue(data[7])
        dlg.m_choice2.SetStringSelection(data[8])
        
        u = data[9]
#        print u

        #Ustawianie wartości w checklist dla powiazanych autorów z publikacja
        if len(u) == 1:
            dlg.m_checkList3.Check(int(u[0])-1)
        elif len(u) == 0:
            print 'nie ma powiazanych danych'
        else:
            for i in range(len(u)):
                dlg.m_checkList3.Check(u[i]-1)
        dlg.ShowModal()
    
    def updateRecord(self, data):
        """Funkcja uaktualnia wartości listctrl o podane wartosci"""
        try:
            for i in range(len(data)):
                self.dataList.Append(data[i])
        except TypeError:
            wx.MessageBox(u'Brak wyszukanych danych', 'Brak danych', wx.OK | wx.ICON_INFORMATION)
    
    def RightClickCb(self, event):
        self.currentItem = event.m_itemIndex
#        print self.currentItem
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
        elif operation == 'Edytuj rekord':
            t = self.dataList.GetItemText(self.currentItem)
            self.editRecord(t, cDatabase.geteditPubData(self.session, t))
        elif operation == u'Usuń rekord':
            """usuwanie wybranego rekordu z bazy wraz z powiazaniami autorów"""
            t = self.dataList.GetItemText(self.currentItem)
            cDatabase.delPubData(self.session, t)
    
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
