# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import sys
from Tkinter import *

class Scholar:
    
    def __init__(self):
        self.scholar_glo_url = 'scholar.google.com'
        self.all_item = 0
        self.pobierz()

    def pobierz(self):
        self.query()
        self.all_page()

    def all_page(self):
        #print self.all_item
        if self.all_item > 10:
            for i in range(10,self.all_item,10):
                item_add = {'num': 0}
                self.item.update(item_add)
                self.item['num'] = i
                self.scholar_url = 'http://scholar.google.com/scholar?'+self.s0+self.s1+self.s2+self.s3+self.s4+self.s5+self.s6+self.s7+self.s8+self.s9
                self.query()

    def first_url(self):
        self.s0 = 'start=%(num)s&'
        self.s1 = 'as_q=%(query)s&'
        self.s2 = 'as_epq=%(exact)s&'
        self.s3 = 'as_oq=%(oneof)s&'
        self.s4 = 'as_eq=%(without)s&'
        self.s5 = 'as_occt=any&'
        self.s6 = 'as_sauthors=%(author)s&'
        self.s7 = '&as_publication=%(pub)s&'
        self.s8 = 'as_ylo=%(ylow)s&'
        self.s9 = 'as_yhi=%(yhigh)s&'
        self.item = {'query': "analiza", 'exact': "", 'oneof': "", 'without': "",
                     'author': "Leszek+Wojnar", 'pub': "", 'ylow': "", 'yhigh': ""}
        self.scholar_url = 'http://scholar.google.com/scholar?'+self.s1+self.s2+self.s3+self.s4+self.s5+self.s6+self.s7+self.s8+self.s9
        
    def query(self):
        if self.all_item == 0:
            self.first_url()
        
        url = self.scholar_url % self.item
        #print url
        r = urllib2.Request(url=url,
                            headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
        op = urllib2.urlopen(r)
        html = op.read()
        self.htmlsoup = BeautifulSoup(html)
        if self.all_item == 0:
            self.number_page_sch()
        self.download_all()
        self.test()
        
    def item_in_page(self):
        div_count = self.htmlsoup.find_all('div', {'class': "gs_r", 'style': re.compile("z-index:")})
        self.item_count = len(div_count)
        
    def number_page_sch(self):
        num_page = self.htmlsoup.find('div', {'id': "gs_ab_md"}).get_text()
        num_page = num_page.split()
        num_page[1] = re.sub(r',', '', num_page[1])

        if num_page[0].isdigit() == True:
            self.all_item = int(num_page[0])
        elif num_page[1].isdigit() == True:
            self.all_item = int(num_page[1])

    """Parsery"""

    def page_parse(self):
        self.title_2 = []
        self.title_url_2 = []
        self.text = []
        """ Nazwa artykulu i link do niego """
        for tag in self.htmlsoup.find_all(True):
            if tag.name == 'div' and tag.get('class') and tag.h3:
                #print tag.h3.get_text()
                if tag.h3.span:
                    tag.h3.span.clear()
                self.title_2.append(tag.h3.get_text())
                if tag.h3.a:
                    #print tag.h3.a['href']
                    self.title_url_2.append(tag.h3.a['href'])
                else:
                    self.title_url_2.append("Brak")
                    #print "Nie ma"

        """ Autorzy artykułu """
        for tag in self.htmlsoup.find_all('div','gs_a'):
            #print tag.get_text()
            self.text.append(tag.get_text())

        """ Pobieranie lików do kazdego artykulu """
        l = ['z-index:400','z-index:399','z-index:398','z-index:397',
             'z-index:396','z-index:395','z-index:394','z-index:393',
             'z-index:392','z-index:391']
        self.links = []
        cit_txt = 'Brak'
        cit_url = 'Brak'
        rel_txt = 'Brak'
        rel_url = 'Brak'
        ver_txt = 'Brak'
        ver_url = 'Brak'
        #print self.item_count
        for i in range(self.item_count):
            for tag in self.htmlsoup.find_all('div',{'style': l[i]}):
                for tag2 in (tag.find_all('a')):
                    text = tag2.get_text()
                    if text.startswith('Cited by'):
                        tmp = text.split()
                        cit_txt = tmp[2]
                        cit_url = self.scholar_glo_url + tag2.get('href')
                    elif text.startswith('Related'):
                        rel_txt = text
                        rel_url = self.scholar_glo_url + tag2.get('href')
                    elif text.startswith('All'):
                        tmp = text.split()
                        ver_txt = tmp[1]
                        ver_url = self.scholar_glo_url + tag2.get('href')
                if cit_txt == 'Brak':
                    self.links.append(cit_txt)
                    self.links.append(cit_url)
                else:
                    self.links.append(cit_txt)
                    self.links.append(cit_url)
                if rel_txt == 'Brak':
                    self.links.append(rel_txt)
                    self.links.append(rel_url)
                else:
                    self.links.append(rel_txt)
                    self.links.append(rel_url)
                if ver_txt == 'Brak':
                    self.links.append(ver_txt)
                    self.links.append(ver_url)
                else:
                    self.links.append(ver_txt)
                    self.links.append(ver_url)
                cit_txt = 'Brak'
                cit_url = 'Brak'
                rel_txt = 'Brak'
                rel_url = 'Brak'
                ver_txt = 'Brak'
                ver_url = 'Brak'
        #print self.links

    def download_all(self):
        self.item_in_page()
        self.page_parse()
        self.Title()
        self.Url_title()
        self.Author()
        self.Year()
        self.Publisher()

    def test(self):
        all_items = []
        for i in range(self.item_count):
            print self.title[i]
            all_items.append(self.title[i])
            print self.title_url[i]
            all_items.append(self.title_url[i])
            print self.author[i] + " rok: " + self.year[i]
            all_items.append(self.author[i])
            all_items.append(self.year[i])
            for j in range(i*6,(i*6+6),6):
                print 'Cited by ' + self.links[j] + ' url: ' + self.links[j+1]
                all_items.append(self.links[j])
                all_items.append(self.links[j+1])
                print self.links[j+2] + ' url: ' + self.links[j+3]
                all_items.append(self.links[j+2])
                all_items.append(self.links[j+3])
                print 'All ' + self.links[j+4] + ' version, url: ' + self.links[j+5]
                all_items.append(self.links[j+4])
                all_items.append(self.links[j+5])
            print self.publish[i] +'\n\n'
        print all_items

    def Url_title(self):
        self.title_url = []
        for i in range(0,len(self.title_url_2),2):
            #print self.title_url_2[i]
            self.title_url.append(self.title_url_2[i])
        #print self.title_url
        
    def Title(self):
        self.title = []
        for i in range(0,len(self.title_2),2):
            self.title_2[i] = self.title_2[i].strip()
            #print self.title_2[i]
            self.title.append(self.title_2[i])
        #print self.title
    
    def Year(self):
        self.year = []
        for i in range(len(self.text)):
            d = re.findall(r'\b(?:20|19)\d{2}\b',self.text[i])
            if len(d) == 0:
                d.append('0')
            d = d.pop()
            self.year.append(d)                
        #print self.year

    def Author(self):
        self.author = []
        for i in range(len(self.text)):
            a = self.text[i].split('-',1)
            self.author.append(a[0])

    def Publisher(self):
        self.publish = []
        for i in range(len(self.text)):
            p = self.text[i].split('- ',-1)
            self.publish.append(p[len(p)-1])

    """parser do pobieraniakolejnych stron z danymi"""
            
    """Walidatory"""

class GUI(Frame, Scholar):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master.title("Bibliografie")
        #Scholar.__init__(self)
        self.TworzFormatke()
        #self.Menu()
        Scholar.__init__(self)        
        
    def TworzFormatke(self):
        #label
        #labStrony = Label(self.master, text="Słowa kluczowe")
        #labStrony.grid(row=0, column=0, stick=W+S)
        #labOpis = Label(self.master, text="Autor")
        #labOpis.grid(row=1, column=0, stick=W+S)
        #listbox
        #self.lbTytul = Listbox(self.master, width=40, height=15, selectmode=BROWSE)
        #self.lbTytul.grid(row=4, column=0, columnspan=4, sticky=N+W+S+E)
        #self.lbStrony = Listbox(self.master, width=40, selectmode=SINGLE)
        #self.lbStrony.grid(row=1, column=0, columnspan=4, sticky=N+W+S+E)
        #self.lbOpis = Listbox(self.master)
        #textbox
        #self.txtItem = Text(self.master, font=("Times",12))
        #self.txtItem.grid(row=1, column=4, rowspan=4)
        #self.txtItem.config(state=DISABLED)
        #button
        btWyswietlstrone = Button(self.master, text="Pobierz", command=self.pobierz)
        btWyswietlstrone.grid(row=2, column=0, stick=E)    

if __name__ == "__main__":
    #app = Scholar()
    app = GUI()
    app.mainloop()
