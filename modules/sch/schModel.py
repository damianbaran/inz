# -*- coding: utf-8 -*-

################################################
##    Aplikacja wspomagajaca tworzenie bazy publikacji naukowych wpsółpracujaca z Google Scholar
##    Copyright (C) 2013  Damian Baran
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################

import wx
import re
import os
import sys
import time
import pickle
import random
import urllib2
from bs4 import BeautifulSoup

## Dokumentacja dla klasy
#
# Klasa zawiera wszystkie zmienne i metody do pobierania danych z wyszukiwarki Google Scholar
class sModel:
    ##Konstruktor
    def __init__(self):
        self.item = {'num': 0, 'query': "", 'exact': "", 'oneof': "", 'without': "",
                     'author': "", 'pub': "", 'ylow': "", 'yhigh': ""}
        self.scholar_glo_url = 'scholar.google.com'
        self.fulllist = []
        self.selectlist = []
        self.all_item = 0
        self.all_item_group = 0
        self.mendata = []
        self.allgroupitems = []
        self.listauthor = []
        self.schlist = []
        self.all_items_id = 0 #dodawanie unikatowego id do kazdego rekordu
        self.all_url = [] #w zmienionym modelu odpowiada z przechowywanie wszystkich linkow do wyszukania
        self.all_number_query = 0 #zlicza ilosc rzadan do serwera googla
#        self.c = float(0) 
        
    ## Dokumentacja addWord
    # @param self Wskaźnik obiektu
    # @param value Lista danych z wartościami do generowania url
    #
    # @return void
    # Funkcja pobiera dane wprowadzone przez uzytkownika wyszukania danych
    def addWord(self, value):
        value = self.replString(value)
        self.item['query'] = value[0]
        self.item['exact'] = value[1]
        self.item['oneof'] = value[2]
        self.item['without'] = value[3]
        self.item['author'] = value[4]
        self.item['pub'] = value[5]
        self.item['ylow'] = value[6]
        self.item['yhigh'] = value[7]
    
    ##Dokumentacja replString
    # @param self Wskaźnik obiektu
    # @param data Lista danych do sprawdzenia
    #
    # @return tuple Lista zmodyfikowanych wartości wprowadzonych przez użytkownika
    # Funkcja sprawdza czy string podany przez uzytkownika nie zawiera spacji, jesli tak to zamienia na '+'
    def replString(self, data):
        tmp = []
        for i in range(len(data)):
            s = re.sub(u' ','+', data[i])
            s = s.encode('utf-8')
            tmp.append(s)
        tuple(tmp)
        return tmp
    
    ## Dokumentacja searchGroup
    # @param self Wskaźnik obiektu
    # @param data Lista danych z autorami
    #
    # @return void
    # Funkcja pobiera dane do wyszukiwania grupowego
    def searchGroup(self, data):
        self.listauthor = data
    
    ## Dokumentacja urlScholar
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja zawiera url wyszukiwania do ktorego można wprowadzic dane uzytkownika
    def urlScholar(self):
        self.s0 = 'start=%(num)s&'
        self.s1 = 'as_q=%(query)s&'
        self.s2 = 'as_epq=%(exact)s&'
        self.s3 = 'as_oq=%(oneof)s&'
        self.s4 = 'as_eq=%(without)s&'
        self.s5 = 'as_occt=any&'
        self.s6 = 'as_sauthors=%(author)s&'
        self.s7 = 'as_publication=%(pub)s&'
        self.s8 = 'as_ylo=%(ylow)s&'
        self.s9 = 'as_yhi=%(yhigh)s&'
        self.scholar_url = 'http://scholar.google.com/scholar?'+self.s0+self.s1+self.s2+self.s3+self.s4+self.s5+self.s6+self.s7+self.s8+self.s9
    
    ## .Dokumentacja firstQuery
    # @param self Wskaźnik obiektu
    #
    # @return number Liczba wyszukanych publikacji
    # Funkcja pobiera liczbę wszystkich publikacji
    def firstQuery(self):
        self.urlScholar()
        if self.all_item == 0:
            self.item['num'] = 0

        url = self.scholar_url % self.item
        r = urllib2.Request(url=url,
            headers={'User-Agent': 
                'Mozilla/5.0 (Windows NT 6.1) \
                AppleWebKit/535.7 (KHTML, like Gecko) \
                Chrome/16.0.912.77 Safari/535.7'})
        op = urllib2.urlopen(r)
        html = op.read()

        self.htmlsoup = BeautifulSoup(html)
        self.numberPageSearch()
        self.generateLinks(self.all_item, self.item)
        return self.all_item

    ## .Dokumentacja firstQueryGroup
    # @param self Wskaźnik obiektu
    # @param data Lista autorów do wyszukiwania grupowego
    #
    # @return void
    # Funkcja zlicza ilość publikacji do pobrania w wyszukiwaniu grupowym
    def firstQueryGroup(self, data):
        self.item['query'] = ''
        self.item['exact'] = ''
        self.item['oneof'] = ''
        self.item['without'] = ''
        self.item['author'] = ''
        self.item['pub'] = ''
        for i in range(len(data)):
            self.item['author'] = data[i]
            self.item['num'] = 0
            l = self.firstQuery()

    ## .Dokumentacja generateLinks
    # @param self Wskaźnik obiektu
    # @param n Liczba wszystkich publikacji
    # @param rec Atrybuty do wstawienia w wygenerowany link
    #
    # @return void
    # Funkcja generuje wszystkie linki do pobrani publikacji danego wyszukiwnaia
    def generateLinks(self, n, rec):
        d = 0
        for i in range(0,n,10):
            rec['num'] = i
            url = self.scholar_url % rec
            self.all_url.append(url)
            d += 1
        self.all_number_query += d

    ## .Dokumentacja queryScholar
    # @param self Wskaźnik obiektu
    # @param link Wygenerowany adres url
    #
    # @return string Strone html w postaci cigu znaków
    # Funkcja pobiera wszystkie strony z wynikami wyszukiwania
    def queryScholar(self, link):
        url = link
        r = urllib2.Request(url=url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) \
            AppleWebKit/535.7 (KHTML, like Gecko) \
            Chrome/16.0.912.77 Safari/535.7'})
        op = urllib2.urlopen(r)
        html = op.read()

        return html
    
    ## .Dokumentacja numberRecordsOnPage
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja zlicza liczbę rekordów na stronie
    def numberRecordsOnPage(self):
        div_count = self.htmlsoup.find_all('div', {'class': "gs_r", 'style': re.compile("z-index:")})
        self.item_count = len(div_count)
    
    ## .Dokumentacja numberPageSearch
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja pobiera liczbę wszystkich rekordów wyszukania
    def numberPageSearch(self):
        num_page = self.htmlsoup.find('div', {'id': "gs_ab_md"}).get_text()
        num_page = num_page.split()
        
        try:
            num_page[1] = re.sub(r',', '', num_page[1])
            if num_page[0].isdigit() == True:
                self.all_item = int(num_page[0])
            elif num_page[1].isdigit() == True:
                self.all_item = int(num_page[1])
            self.all_item_group += self.all_item
        except IndexError:
            pass

    ## .Dokumentacja findData
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja przeszkuje html'a w celu wyciągnięcia poptrzebnych danych
    def findData(self):
        self.title_2 = []
        self.title_url_2 = []
        self.text = []
        
        for tag in self.htmlsoup.find_all(True):
            if tag.name == 'div' and tag.get('class') and tag.h3:
                if tag.h3.span:
                    tag.h3.span.clear()
                t = tag.h3.get_text()
                if t.find('User profiles for author') == -1:
                    self.title_2.append(tag.h3.get_text())
                if tag.h3.a:
                    self.title_url_2.append(tag.h3.a['href'])
                else:
                    self.title_url_2.append("Brak")

        for tag in self.htmlsoup.find_all('div','gs_a'):
            self.text.append(tag.get_text())

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
    
    ## .Dokumentacja doThis
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja wywołuje kolejne funkcje
    def doThis(self):
        self.numberRecordsOnPage()
        self.findData()
        self.parseTitle()
        self.parseUrlTitle()
        self.parseAuthor()
        self.parseYear()
        self.parsePublisher()

    ## .Dokumentacja onePage
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja zapisuje końcowe dane z jednej strony do listy
    def onePage(self):
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
            for j in range(i*6,(i*6+6),6):
                records['cittxt'] = self.links[j]
                records['citurl'] = self.links[j+1]
                records['reltxt'] = self.links[j+2]
                records['relurl'] = self.links[j+3]
                records['vertxt'] = self.links[j+4]
                records['verurl'] = self.links[j+5]
            one = (self.all_items_id, self.links[j], self.title[i], self.author[i], self.year[i], self.publish[i], '', self.title_url[i], self.links[j+1])
            self.all_items_id += 1
            self.all_items.append(one)
        self.fulllist += self.all_items
    
    ## .Dokumentacja filtruj
    # @param self Wskaźnik obiektu
    # @param record Lista wszystkich pobranych publikacji
    # @param filtr Imie i Nazwisko autora do filtracji
    # @param dbDane Klucze filtrujace dla wybranego autora
    #
    # @return list Listę wszystkich przefiltrowanych publikacji
    # Funkcja filtruje cała listę wyszukanych publikacji
    def filtruj(self, record, filtr, dbDane):
        d = []
        dict = dbDane
        c = dict[filtr].split(', ')
        t = len(c)
        for i in range(len(record)):
            a = record[i]
            c = dict[filtr].split(', ')
            for j in range(len(c)):
                if re.findall(c[j],a[3]):
                    d.append(a)
        self.fulllist = d
        return d
    
    ## .Dokumentacja allRecords
    # @param self Wskaźnik obiektu
    #
    # @return list Lista wyszukanych publikacji
    # Funkcja zwraca pełna liste wyszukanych publikacji
    def allRecords(self):
        return self.fulllist
    
    ## .Dokumentacja searchList
    # @param self Wskaźnik obiektu
    # @param data Lista z publikacjami
    #
    # @return list Lista odfiltrowanych publikacji
    # Funkcja zwraca liste odfiltrowanych publikacji
    def searchList(self, data):
        self.schlist = data
        return self.schlist
    
    ## .Dokumentacja saveResult
    # @param self Wskaźnik obiektu
    # @param data Lista wszystkich publikacji
    #
    # @return void
    # Funkcja zapisuje wyszukane publikacje do pliku
    def saveResult(self, data):
        home = os.getcwd()
        os.chdir('raport')
        r = random.random()
        r = str(r)
        q = e = o = w = a = p = yl = yh = ''
        if self.item['query'] != '':
            q = self.item['query'] + ','
        if self.item['exact'] != '':
            e = self.item['exact'] + ','
        if self.item['oneof'] != '':
            o = self.item['oneof'] + ','
        if self.item['without'] != '':
            w = self.item['without'] + ','
        if self.item['author'] != '':
            a = self.item['author'] + ','
        if self.item['pub'] != '':
            p = self.item['pub'] + ','
        if self.item['ylow'] != '':
            yl = self.item['ylow'] + ','
        if self.item['yhigh'] != '':
            yh = self.item['yhigh'] + ','
        t = '%s%s%s%s%s%s%s%s%s' % (q, e, o, w, a, p, yl, yh, r)

        fo = open(t+'.txt', 'w')
        pickle.dump(data, fo)
        fo.close()
        os.chdir(home)
    
    ## .Dokumentacja parseUrlTitle
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja odfiltrowuje niepotrzebne dane dla hieprłącza tytulu rekordu
    def parseUrlTitle(self):
        self.title_url = []
        for i in range(0,len(self.title_url_2),2):
            self.title_url.append(self.title_url_2[i])
    
    ## .Dokumentacja parseTitle
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja odfiltrowuje niepotrzebne dane dla tytulu rekordu
    def parseTitle(self):
        self.title = []
        for i in range(0,len(self.title_2),2):
            self.title_2[i] = self.title_2[i].strip()
            self.title.append(self.title_2[i])
    
    ## .Dokumentacja parseYear
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja odfiltrowuje rok z pobranego ciągu znaków
    def parseYear(self):
        self.year = []
        for i in range(len(self.text)):
            d = re.findall(r'\b(?:20|19)\d{2}\b',self.text[i])
            if len(d) == 0:
                d.append(' ')
            d = d.pop()
            self.year.append(d)                
    
    ## .Dokumentacja parseAuthor
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja odfiltrowuje autorów z pobranego ciągu znaków
    def parseAuthor(self):
        self.author = []
        for i in range(len(self.text)):
            a = self.text[i].split('-',1)
            self.author.append(a[0])
    
    ## .Dokumentacja parsePublisher
    # @param self Wskaźnik obiektu
    #
    # @return void
    # Funkcja odfiltrowuje wydawce z pobranego ciągu znaków
    def parsePublisher(self):
        self.publish = []
        for i in range(len(self.text)):
            p = self.text[i].split('- ',-1)
            self.publish.append(p[len(p)-1])
