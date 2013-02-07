# -*- coding: utf-8 -*-
import wx
import re
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
#from src.lib.process import MainProcess
#from threading import *

dataS = []
dataB = []

class mModel:
    def __init__(self):
        """Konstruktor""" 
#        self.dataS = []
#        self.dataB = []
        
    def getData(self,  data):
#        self.dataS = []
        dataS.extend(data)
#        print self.dataS
        print 'dziala model menadzera'
    
    def getBaseData(self, data):
#        dataB = []
        dataB.extend(data)
#        print self.dataB
        print 'dziala model menadzera'
        
    def allChoiceRekord(self):
        all = dataS + dataB
        print all
        print 'wszystkie wyniki'
        return all
