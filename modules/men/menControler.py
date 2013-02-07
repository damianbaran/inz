# -*- coding: utf-8 -*-
import wx
import time
from menModel import mModel
#from menView import mView

class mControler():
    """controler dla menadzera publikacji"""
    def __init__(self):
        self.mmodel = mModel()
    
    def getRecords(self):
        tmp = self.mmodel.allChoiceRekord()
        return tmp
