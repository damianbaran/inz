# -*- coding: utf-8 -*-
import wx
import re
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
#from src.lib.process import MainProcess
#from threading import *

class bModel():
    def __init__(self):
        """Konstruktor""" 
        self.item = {'query': "", 'exact': "", 'oneof': "", 'without': "",
                     'author': "", 'pub': "", 'ylow': "", 'yhigh': ""}
        self.scholar_glo_url = 'scholar.google.com'
        self.fulllist = []
        self.selectlist = []
        self.all_item = 0
        self.c = float(0)
        print "cos tam"
            
