import wx
import re
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
from wx.lib.pubsub import Publisher as pub

class Record(object):
    """"""
    def __init__(self, cittxt, title, author, year, publish):
        self.cittxt = cittxt
        self.year = year
        self.author = author
        self.publish = publish
        self.title = title

class Model(Record):
    def __init__(self):
        """Konstruktor"""
        self.item = {'query': "", 'exact': "", 'oneof': "", 'without': "",
                     'author': "", 'pub': "", 'ylow': "", 'yhigh': ""}
        self.scholar_glo_url = 'scholar.google.com'
        self.fulllist = []
        self.all_item = 0

    def addWord(self, value):
        """
        Funkcja pobiera dane wprowadzone przez użytkownika
        wyszukania dancyh
        """
        value = self.replString(value)
        self.item['query'] = str(value[0])
        self.item['exact'] = str(value[1])
        self.item['oneof'] = str(value[2])
        self.item['without'] = str(value[3])
        self.item['author'] = str(value[4])
        self.item['pub'] = str(value[5])
        self.item['ylow'] = str(value[6])
        self.item['yhigh'] = str(value[7])

    def replString(self, data):
        """
        Funkcja sprawdza czy string podany przez użytkownika
        nie zawiera spacji, jeśli tak to zamienia na '+'
        """
        tmp = []
        for i in range(len(data)):
            s = re.sub(r' ','+', str(data[i]))
            tmp.append(s)
        tuple(tmp)
        return tmp
        

    def downloadData(self):
        """Funkcja pobiera wszystkie dane wyszukiwania"""
        self.queryScholar()
        self.allPages()
        self.allRecords()

    def allPages(self):
        """Funkcja przechodzi po wszystkich stronach wyszukiwania"""
        if self.all_item > 10:
            for i in range(10,self.all_item,10):
                item_add = {'num': 0}
                self.item.update(item_add)
                self.item['num'] = i
                self.scholar_url = 'http://scholar.google.com/scholar?'+self.s0+self.s1+self.s2+self.s3+self.s4+self.s5+self.s6+self.s7+self.s8+self.s9
                self.queryScholar()

    def urlScholar(self):
        """
        Funkcja zawiera url wyszukiwania do którego można wprowadzić
        dane użytkownika
        """
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
        self.scholar_url = 'http://scholar.google.com/scholar?'+self.s1+self.s2+self.s3+self.s4+self.s5+self.s6+self.s7+self.s8+self.s9

    def queryScholar(self):
        """
        Funkcja pobiera jedną stonę wyszukiwania. Zamienia na format do
        przeszkiwania html'a. Pobiera wszystkie dane z tej strony do
        kolejnych działań
        """
        if self.all_item == 0:
            self.urlScholar()
        
        url = self.scholar_url % self.item
        r = urllib2.Request(url=url,
                            headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
        op = urllib2.urlopen(r)
        html = op.read()
        self.htmlsoup = BeautifulSoup(html)
        if self.all_item == 0:
            self.numberPageSearch()
        self.doThis()
        self.onePage()
        
    def numberRecordsOnPage(self):
        """Funkcja zlicza liczbę rekordów na stronie"""
        div_count = self.htmlsoup.find_all('div', {'class': "gs_r",
                                                   'style': re.compile("z-index:")})
        self.item_count = len(div_count)
        print self.item_count
        
    def numberPageSearch(self):
        """Funkcja pobiera liczbę wszystkich rekordów wyszukania"""
        num_page = self.htmlsoup.find('div', {'id': "gs_ab_md"}).get_text()
        num_page = num_page.split()
        
        try:
            num_page[1] = re.sub(r',', '', num_page[1])
            if num_page[0].isdigit() == True:
                self.all_item = int(num_page[0])
                print self.all_item
            elif num_page[1].isdigit() == True:
                self.all_item = int(num_page[1])
                print self.all_item
        except IndexError:
            wx.MessageBox('Brak danych dla tego wyszukiwania', 'Blad',
                          wx.OK | wx.ICON_INFORMATION)

    def findData(self):
        """Funkcja przeszkuje html'a w celu wyciągnięcia poptrzebnych danych"""
        self.title_2 = []
        self.title_url_2 = []
        self.text = []
        
        """ Nazwa artykulu i link do niego """
        for tag in self.htmlsoup.find_all(True):
            if tag.name == 'div' and tag.get('class') and tag.h3:
                if tag.h3.span:
                    tag.h3.span.clear()
                self.title_2.append(tag.h3.get_text())
                if tag.h3.a:
                    self.title_url_2.append(tag.h3.a['href'])
                else:
                    self.title_url_2.append("Brak")

        """ Autorzy artykułu """
        for tag in self.htmlsoup.find_all('div','gs_a'):
            self.text.append(tag.get_text())

        """ Pobieranie lików do kazdego artykulu i odfiltorwanie ich z opcją dodanie brakującego fragmentu sdresu url"""
        l = ['z-index:400','z-index:399','z-index:398','z-index:397',
             'z-index:396','z-index:395','z-index:394','z-index:393',
             'z-index:392','z-index:391']
        self.links = []
        cit_txt = 0
        cit_url = 'Brak'
        rel_txt = 'Brak'
        rel_url = 'Brak'
        ver_txt = 'Brak'
        ver_url = 'Brak'
        for i in range(self.item_count):
            for tag in self.htmlsoup.find_all('div',{'style': l[i]}):
                for tag2 in (tag.find_all('a')):
                    text = tag2.get_text()
                    if text.startswith('Cited by'):
                        tmp = text.split()
                        cit_txt = int(tmp[2])
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
                cit_txt = 0
                cit_url = 'Brak'
                rel_txt = 'Brak'
                rel_url = 'Brak'
                ver_txt = 'Brak'
                ver_url = 'Brak'

    def doThis(self):
        """Funkcja wywołuje kolejne funkcje"""
        self.numberRecordsOnPage()
        self.findData()
        self.parseTitle()
        self.parseUrlTitle()
        self.parseAuthor()
        self.parseYear()
        self.parsePublisher()

    def onePage(self):
        """Funkcja zapisuje końcowe dane z jednej strony do listy"""
        self.all_items = []
        for i in range(self.item_count):
            records = {'title':'','titleurl':'','author':'','year':'',
                       'publish':'','cittxt':'','citurl':'','reltxt':'',
                       'relurl':'','vertxt':'','verurl':''}
            records['title'] = self.title[i]
            records['titleurl'] = self.title_url[i]
            records['author'] = self.author[i]
            records['year'] = self.year[i]
            records['publish'] = self.publish[i]
            #print self.title[i]
            #print self.title_url[i]
            #print self.author[i] + " rok: " + self.year[i]
            for j in range(i*6,(i*6+6),6):
                records['cittxt'] = self.links[j]
                records['citurl'] = self.links[j+1]
                records['reltxt'] = self.links[j+2]
                records['relurl'] = self.links[j+3]
                records['vertxt'] = self.links[j+4]
                records['verurl'] = self.links[j+5]
                #print 'Cited by ' + self.links[j] + ' url: ' + self.links[j+1]
                #print self.links[j+2] + ' url: ' + self.links[j+3]
                #print 'All ' + self.links[j+4] + ' version, url: ' + self.links[j+5]
            #print 'Publish' + self.publish[i] +'\n\n'
            one = Record(self.links[j], self.title[i],
                         self.author[i], self.year[i], self.publish[i])
            self.all_items.append(one)
        self.fulllist += self.all_items
        
    def allRecords(self):
        """Funckja sumuje wszystkie pobrane listy"""
        #print self.full
        return self.fulllist

    def parseUrlTitle(self):
        """Funkcja odfiltrowuje niepotrzebne dane dla hieprłącza tytulu rekordu"""
        self.title_url = []
        for i in range(0,len(self.title_url_2),2):
            self.title_url.append(self.title_url_2[i])
        
    def parseTitle(self):
        """Funkcja odfiltrowuje niepotrzebne dane dla tytulu rekordu"""
        self.title = []
        for i in range(0,len(self.title_2),2):
            self.title_2[i] = self.title_2[i].strip()
            self.title.append(self.title_2[i])
    
    def parseYear(self):
        """Funkcja odfiltrowuje rok z pobranego ciągu znaków"""
        self.year = []
        for i in range(len(self.text)):
            d = re.findall(r'\b(?:20|19)\d{2}\b',self.text[i])
            if len(d) == 0:
                d.append(' ')
            d = d.pop()
            self.year.append(d)                

    def parseAuthor(self):
        """Funkcja odfiltrowuje autorów z pobranego ciągu znaków"""
        self.author = []
        for i in range(len(self.text)):
            a = self.text[i].split('-',1)
            self.author.append(a[0])

    def parsePublisher(self):
        """Funkcja odfiltrowuje wydawce z pobranego ciągu znaków"""
        self.publish = []
        for i in range(len(self.text)):
            p = self.text[i].split('- ',-1)
            self.publish.append(p[len(p)-1])
            
