# -*- coding: utf-8 -*-
import wx
import re
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
#from src.lib.process import MainProcess
#from threading import *

class mModel():
    def __init__(self):
        """Konstruktor""" 
        self.data = []
        
    def getData(self,  data):
        self.data = data
        print self.data
        print 'dziala model menadzera'

