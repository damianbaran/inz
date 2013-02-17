# -*- coding: utf-8 -*-
import wx
from schModel import sModel
from modules.men.menModel import mModel

class sControler(sModel, mModel):
    """Controler dla modules.sch czyli wyszukiwania"""
    def __init__(self):
        self.smodel = sModel()
        self.mmodel = mModel()
    
    def SetFilter(self, r, f, db):
        c = self.smodel.filtruj(r,f,db)
        return c
    
    def SelectAllClick(self, data):
        t = self.smodel.selectingString(data)
        self.mmodel.getData(t)
#        return t
    
    def DataforMen(self):
        return self.smodel.mendata
    
    def SetItems(self):
        r = self.smodel.allRecords()
        return r
        
    def SetSearchItem(self):
        r = self.smodel.schlist
        self.smodel.fulllist = r
        return r
    
    def AddWord(self, data):
        self.smodel.addWord(data)
        self.smodel.fulllist = []
        self.smodel.downloadData()
#        self.smodel.all_item = 0
        
    def AddWordGroup(self,  data):
        self.smodel.searchGroup(data)
        self.smodel.fulllist = []
#        self.smodel.all_item = 0
        self.smodel.downloadDataGroup()
#        self.smodel.all_item = 0
    
#    def getProc(self):
#        t = self.smodel.c
#        return t
