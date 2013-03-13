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

import re
import wx
import unicodedata
from sqlalchemy import create_engine, or_, and_
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
#### wyjatki
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm.interfaces
import sqlalchemy.exc
import sqlalchemy.orm.exc

from mDatabase import Person, College, Faculty, Institute, Group, ColPer, GroPer, Publication, Journal, PerPub, Cite, metadata

## Dokumentacja createDatabase
# @return void
# Funkcja tworzy baze danych jesli nie istnieje
def createDatabase():
    """Tworzy baze danych jesli nie istnieje"""
    metadata.create_all()

## Dokumentacja connectDatabase
# @return void
# Funkcja tworzy sesje dla użytkownika
def connectDatabase():
    """Łaczy z baza danych"""
    engine = create_engine("sqlite:///schdatabase.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

## Dokumentacja getCollegeName
# @param session Sesja uzytkownika
#
# @return list Nazwy afiliacji
# Funkcja pobiera wszystkie nazwy afiliacji
def getCollegeName(session):
    c = []
    for name in session.query(College.name).group_by(College.name):
        c.append(name[0])
    result = c
    return result

## Dokumentacja getFacultyName
# @param session Sesja uzytkownika
#
# @return list Nazwy wydziałów
# Funkcja pobiera wszystkie nazwy wydziałów
def getFacultyName(session):
    c = []
    for name in session.query(Faculty.name).group_by(Faculty.name):
        c.append(name[0])
    result = c
    return result

## Dokumentacja getInstituteName
# @param session Sesja uzytkownika
#
# @return list Nazwy instytutów
# Funkcja pobiera wszystkie nazwy instytutów
def getInstituteName(session):
    c = []
    for name in session.query(Institute.name).group_by(Institute.name):
        c.append(name[0])
    result = c
    return result

## Dokumentacja getAllRecord
# @param session Sesja uzytkownika
#
# @return list lista autorów
# Funkcja zwraca liste autorów
def getAllRecord(session):
    d = []
    for per in session.query(Person):
        c = (str(per.id)+ ' ' + per.name + ' ' + per.surname)
        d.append(c)
    return d
    
## Dokumentacja getGroupName
# @param session Sesja uzytkownika
#
# @return list Nazwy grup
# Funkcja pobiera wszystkie nazwy grup
def getGroupName(session):
    result = []
    for name in session.query(Group.name).group_by(Group.id):
        result.append(name[0])
    return result
    
## Dokumentacja getUserInGroup
# @param session Sesja uzytkownika
# @param gname Nazwa grupy
#
# @return list Nazwy autorów
# Funkcja pobiera wszsytkich autorów należacych do wybranej grupy
def getUserInGroup(session, gname):
    result = []
    for g, p, l in session.query(Group, Person, GroPer).\
                filter(GroPer.person_id == Person.id).\
                filter(GroPer.group_id == Group.id).\
                filter(Group.name == gname).group_by(Person.id):
        t = p.surname.encode('utf-8')
        result.append(t)
    return result
    
## Dokumentacja getCheckedUser
# @param session Sesja uzytkownika
# @param gname Nazwa grupy
#
# @return list ID autora
# Funkcja sprawdza czy ID wybranego autora, naleze do wybranej grupy
def getCheckedUser(session, gname):
    result = []
    for g, p, pg in session.query(Group, Person, GroPer).\
                filter(Group.id == GroPer.group_id).\
                filter(Person.id == GroPer.person_id).\
                filter(Group.name == gname).group_by(Person.id):
        result.append(p.id)
    return result

## Dokumentacja editUserGroup
# @param session Sesja uzytkownika
# @param gname Nazwa grupy
#
# @return void 
# Funkcja usuwa wszystkie powiazania pomiedzy wybrana grupa a autorami
def editUserGroup(session, gname):
    result = []
    for g, p, pg in session.query(Group, Person, GroPer).\
                filter(Group.id == GroPer.group_id).\
                filter(Person.id == GroPer.person_id).\
                filter(Group.name == gname).group_by(Person.id):
        session.delete(pg)
    session.commit()

## Dokumentacja getHtmlData
# @param session Sesja uzytkownika
# @param id ID wybranej publikacji
#
# @return list Wybrane publikacje
# Funkcja zwraca wartości wybranych publikacji do stworzenia plików bibliograficznych
def getHtmlData(session, id):
    tmp = []
    for pub, jou in session.query(Publication, Journal).\
            filter(Publication.id == id).\
            filter(Journal.id == Publication.journal_id).\
            group_by(Publication.id):
        c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root)
        tmp.append(c)
    for pub, jou in session.query(Publication, Journal).\
            filter(Publication.id == id).\
            filter(Publication.journal_id == None).\
            group_by(Publication.id):
        c = (pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root)
        tmp.append(c)
    return tmp

## Dokumentacja deleteCite
# @param session Sesja uzytkownika
# @param id ID polaczonej publikacji
# @param idp ID wiodacej publikacji
#
# @return void
# Funkcja usuwa wszystkie polaczenia pomiedzy wybranymi polaczonymi publikacjami
def deleteCite(session, id, idp):
    for c in session.query(Cite).filter(Cite.pub_ids == idp).filter(Cite.id_pub_m == id):
        session.delete(c)
    session.commit()

## Dokumentacja saveCite
# @param session Sesja uzytkownika
# @param data Wartosci dla tabeli Cite
#
# @return void
# Funkcja zapisuje do bazy nowe polaczenie pomiedzy publikacjami
def saveCite(session, data):
    cit = Cite(data[0], data[1], data[2], data[3])
    session.add(cit)
    session.commit()

## Dokumentacja getMergePub
# @param session Sesja uzytkownika
#
# @return list Wiodacych publikacji
# Funkcja pobiera wszystkie wiodace polaczone publikacje
def getMergePub(session):
    result = {}
    id_pub = []
    for c in session.query(Cite).group_by(Cite.pub_ids):
        id_pub.append(c.pub_ids)
    
    for i in range(len(id_pub)):
        pub = session.query(Publication).filter(Publication.id == id_pub[i]).first()
        if pub != None:
            tmp = pub.title +' - '+ pub.author +' - '+ str(pub.citation) +' - '+ str(pub.year) +' - '+ pub.root
            d = {id_pub[i]:tmp}
            result.update(d)
    return result

## Dokumentacja getCitPubData
# @param session Sesja uzytkownika
#
# @return list Publikacje do łaczenia
# Funkcja pobiera wszystkie publikacje jakie sa w bazie danych. Wykorzystywane przy dodawaniu publikacji do łaczenia
def getCitPubData(session):
    result = []
    for pub in session.query(Publication):
        jouID = pub.journal_id
        if jouID != None:
            jou = session.query(Journal).filter(pub.journal_id == Journal.id).first()
            tmp = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root, pub.urlcit, pub.urlpub)
            result.append(tmp)
        else:
            tmp = (pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root, pub.urlcit, pub.urlpub)
            result.append(tmp)
    return result

## Dokumentacja pubCitMerge
# @param session Sesja uzytkownika
# @param id
#
# @return list Publikacje polaczone
# Funkcja pobiera wszystkie powiazane publikacje z wiodaca
def pubCitMerge(session, id):
    result = []
    idm = []
    for c in session.query(Cite).filter(Cite.pub_ids == id).group_by(Cite.id_pub_m):
        idm.append(c.id_pub_m)
    for i in range(len(idm)):
        pub = session.query(Publication).filter(Publication.id == idm[i]).first()
        tmp = (pub.id, pub.citation, pub.title, pub.author, pub.year, pub.root, pub.doi, pub.urlcit, pub.urlpub)
        result.append(tmp)
    return result

## Dokumentacja addJournalData
# @param session Sesja uzytkownika
# @param data Wartosci dla tabeli Journal
#
# @return void
# Funkcja dodaje nowego wydawce
def addJournalData(session, data):
    tmp =[]
    for t in session.query(Journal).filter(Journal.full_name == data[0]).group_by(Journal.id):
        tmp.append(t)
    if tmp == []:
        jou = Journal(data[0], data[1], data[2], data[3])
        session.add(jou)
        session.commit()
    else:
        wx.MessageBox(u'Nazwa wydawcy jest unikatowa.\n Nie można dodać drugiego takiego wydawcy.', u'Wydawca istnieje!', wx.OK | wx.ICON_INFORMATION)

## Dokumentacja editJournalData
# @param session Sesja uzytkownika
# @param data Wartosci do edycji wydawcy
# @param id ID wydawcy
#
# @return void
# Funkcja edytuje wybranego wydawce
def editJournalData(session, data, id):
    jou = session.query(Journal).filter(Journal.id == id).group_by(Journal.id).first()
    jou.full_name = data[0]
    jou.short_name = data[1]
    jou.address = data[2]
    jou.note = data[3]
    session.add(jou)
    session.commit()

## Dokumentacja delJournalData
# @param session Sesja uzytkownika
# @param name Nazwa wydawcy
#
# @return void
# Funkcja usuwa wybranego wydawce
def delJournalData(session, name):
    jou = session.query(Journal).filter(Journal.full_name == name).one()
    print jou.id
    jouID = jou.id
    session.delete(jou)
    
    for pub in session.query(Publication).\
            filter(Publication.journal_id == jouID):
        pub.journal_id == None
        session.add(pub)
    
    session.commit()

## Dokumentacja getJournalName
# @param session Sesja uzytkownika
#
# @return list Nazwy wydawców
# Funkcja pobiera wszystkie nazwy wydawców
def getJournalName(session):
    result = []
    for jou in session.query(Journal):
        result.append(jou.full_name)
    return result

## Dokumentacja getJournalNameID
# @param session Sesja uzytkownika
#
# @return dictionary Nazwy wydawców z ich ID
# Funkcja pobiera wszystkich wydaawców wraz z ich ID w bazie danych
def getJournalNameID(session):
    result = {}
    for jou in session.query(Journal):
        d = (jou.full_name)
        id = jou.id
        tmp = {d:id}
        result.update(tmp)
    return result

## Dokumentacja getJournalData
# @param session Sesja uzytkownika
# @param name Nazwa wydawcy
#
# @return list Wartosci dla wybranego wydawcy
# Funkcja zwraca wartości dla wybranego wydawcy
def getJournalData(session, name):
    for jou in session.query(Journal).\
            filter(Journal.full_name == name):
        t = (jou.short_name, jou.address, jou.note)
    return t

## Dokumentacja addEmptyString
# @param session Sesja uzytkownika
#
# @return void
# Funckja dodaje pusty rekord do tabeli Journal
def addEmptyString(session):
    jou = Journal('', '', '', '')
    session.add(jou)
    session.commit()

## Dokumentacja getMergePubData
# @param session Sesja uzytkownika
# @param id ID wybranej publikacji
#
# @return tuple Lista z wartosciami wybranej publikacji
# Funkcja pobiera wartosci wybranej publikacji do laczenia
def getMergePubData(session, id):
    pub = session.query(Publication).filter(Publication.id == id).one()
    result = (pub.id, pub.citation, pub.title, pub.author, pub.year, pub.root, pub.doi, pub.urlcit, pub.urlpub)
    return result

## Dokumentacja getPubData
# @param session Sesja uzytkownika
# @param id ID publikacji
#
# @return tuple Lista z wartosciami do wyświetlenia w okienku zarzadzania publikacjami
def getPubData(session, id):
    pub = session.query(Publication).filter(Publication.id == id).one()
    jouID = pub.journal_id
    
    if jouID != None:
        jou = session.query(Journal).filter(pub.journal_id == Journal.id).first()
        result = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root, pub.urlcit, pub.urlpub)
    else:
        result = (pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root, pub.urlcit, pub.urlpub)
    return result

## Dokumentacja delPubData
# @param session Sesja uzytkownika
# @param id ID wybranej publikacji
#
# @return void
# Funkcja usuwa wszystkie wybrane publikacje z bazy danych oraz powiazanie z autorami
def delPubData(session, id):
    pub = session.query(Publication).filter(Publication.id == id).one()
    for pub, perpub in session.query(Publication, PerPub).\
            filter(Publication.id == id).\
            filter(PerPub.pub_id == id):
        session.delete(perpub)

    session.delete(pub)
    session.commit()
    
## Dokumentacja addPubData 
# @param session Sesja uzytkownika
# @param data Wartosci dla tabeli Publication
#
# @return void
# Funkcja dodaje nowa publikacje do bazy danych
def addPubData(session, data):
    pub = Publication(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[9], data[10], data[11], data[12], data[13], data[14])
    session.add(pub)
    session.commit()
    
    id = data[8]
    for i in range(len(id)):
        tmp = PerPub(int(id[i]), pub.id)
        session.add(tmp)
    
    session.commit()

## Dokumentacja addPubMultiData
# @param session Sesja uzytkownika
# @param data Wartosci dla tabeli Publication
#
# @return void
# Funkcja zapisuje do bazy nowa publikacje, wykorzystywana do dodawania bez edycji
def addPubMultiData(session, data):
    pub = Publication(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13])
    session.add(pub)
    session.commit()

## Dokumentacja geteditPubData
# @param session Sesja uzytkownika
# @param id ID wybranej publikacji
#
# @return tuple
# Funkcja pobiera dane publikacji do pozniejszej edycji
def geteditPubData(session, id):
    t = []
    pub = session.query(Publication).filter(Publication.id == id).first()
    jouID = pub.journal_id
    
    for pub, per, perpub in session.query(Publication, Person, PerPub).\
            filter(Person.id == PerPub.person_id).\
            filter(Publication.id == PerPub.pub_id).\
            filter(Publication.id == id):
        t.append(per.id)
    
    if jouID != None:
        jou = session.query(Journal).filter(Journal.id == jouID).first()
        result = (str(pub.id), pub.title, pub.author, pub.citation, pub.type, pub.year, pub.doi, pub.ident, jou.full_name, t, pub.urlpub, pub.urlcit, pub.root, pub.lmcp, pub.jcr, pub.note)
        return result
    else:
        result = (str(pub.id), pub.title, pub.author, pub.citation, pub.type, pub.year, pub.doi, pub.ident, '', t, pub.urlpub, pub.urlcit, pub.root, pub.lmcp, pub.jcr, pub.note)
        return result
    
## Dokumentacja editPubData
# @param session Sesja uzytkownika
# @param data Wartosci dla tabeli Publication
# @param id ID wybranej publikacji
#
# @return void
# Funkcja edytuje wybrana publikacje o wartosci podane przez uzytkownika
def editPubData(session, data, id):
    print data, id
    pub = session.query(Publication).filter(Publication.id == id).first()
    
    pub.title = data[0]
    pub.author = data[1]
    pub.citation = data[2]
    pub.type = data[3]
    pub.year = data[4]
    pub.doi = data[5]
    pub.ident = data[6]
    pub.journal_id = data[7]
    pub.root = data[9]
    pub.lmcp = data[10]
    pub.jcr = data[11]
    pub.note = data[12]
    session.add(pub)
    
    tmpid = data[8]
    for i in range(len(tmpid)):
        tmp = PerPub(tmpid[i], id)
        session.add(tmp)
    
    session.commit()

## Dokumentacja getCheckItemAuthor
# @param session Sesja uzytkownika
# @param id ID publikacji
#
# @return list ID autorów
# Funckja zwraca wszystkie ID autorów którzy s powiazani z wybrana publikacja
def getCheckItemAuthor(session, id):
    t = []
    for pub, jou, per, perpub in session.query(Publication, Journal, Person, PerPub).\
            filter(Person.id == PerPub.person_id).\
            filter(Publication.id == PerPub.pub_id).\
            filter(Publication.id == id).group_by(Person.id):
        t.append(per.id)
    return t

## Dokumentacja editItemAuthor
# @param session Sesja uzytkownika
# @param id
#
# @return void
# Funkcja usuwa wszystkich powiazanych autorów z wybrana publikacja
def editItemAuthor(session, id):
    t = []
    for pub, per, perpub in session.query(Publication, Person, PerPub).\
            filter(Person.id == PerPub.person_id).\
            filter(Publication.id == PerPub.pub_id).\
            filter(Publication.id == id).group_by(Person.id):
        session.delete(perpub)
    session.commit()

## Dokumentacja getLinkPub
# @param session Sesja uzytkownika
# @param id ID wybranej publikacji
#
# @return string Adres url
# Funkcja pobiera adres url do publikacji
def getLinkPub(session, id):
    link = session.query(Publication).filter(Publication.id == id).one()
    return link.urlpub

## Dokumentacja getLinkCit
# @param session Sesja uzytkownika
# @param id ID wybraej publikacji
#
# @return string Adres url do cytowań
# Funkcja pobiera adres url do cytowan wybranej publikacji
def getLinkCit(session, id):
    link = session.query(Publication).filter(Publication.id == id).one()
    return link.urlcit

## Dokumentacja getPerPubID
# @param session Sesja uzytkownika
#
# @return list Lista ID 
# Funkcja pobiera ID wszystkich powiazanych publikacji z autorami
def getPerPubID(session):
    result = []
    for perpub in session.query(PerPub).group_by(PerPub.pub_id):
        result.append(perpub.pub_id)
    return result

## Dokumentacja getCiteID
# @param session Sesja uzytkownika
#
# @return list ID z iloscia cytowan
# Funkcja pobiera wszystkie wiodace publikacje wraz z liczba lacznych cytowan
def getCiteID(session):
    result = []
    for cit in session.query(Cite).group_by(Cite.pub_ids):
        t = (cit.pub_ids, cit.allcit)
        result.append(t)
    return result

## Dokumentacja getRecords
# @param session Sesja uzytkownika
# @param key Klucz do wyszukiwania
# @param search Wartosc podana przez użytkownika
#
# @return list Listwa wyszukanych publikacji
# Funcka wyszukuje wszystkie publikacje w bazie danych, ktore odpowiadaja zadaniu uzytkownika
def getRecords(session, key, search):
    if search == '*' and key != '':
        tmp = []
        for pub, jou in session.query(Publication, Journal).\
                        filter(or_(Journal.id == Publication.journal_id,  Publication.journal_id == None)).\
                        group_by(Publication.id):
            if pub.journal_id == None:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root]
            else:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root]
            tmp.append(c)
        return tmp
    elif key == 'AutorID':
        tmp = []
        for pub, jou, per, perpub in session.query(Publication, Journal, Person, PerPub).\
                        filter(PerPub.person_id == Person.id).\
                        filter(PerPub.pub_id == Publication.id).\
                        filter(or_(Journal.id == Publication.journal_id,  Publication.journal_id == None)).\
                        filter(or_(Person.name.like('%' + search + '%'), Person.surname.like('%' + search + '%'))).\
                        group_by(Publication.id):
            if pub.journal_id == None:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root]
            else:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root]
            tmp.append(c)
        return tmp
    elif key == 'Autor':
        tmp =[]
        for pub, jou in session.query(Publication, Journal).\
                        filter(Publication.author.like('%' + search + '%')).\
                        filter(or_(Journal.id == Publication.journal_id,  Publication.journal_id == None)).\
                        group_by(Publication.id):
            if pub.journal_id == None:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root]
            else:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root]
            tmp.append(c)
        return tmp
    elif key == 'Tytul':
        tmp =[]
        for pub, jou in session.query(Publication, Journal).\
                        filter(Publication.title.like('%' + search + '%')).\
                        filter(or_(Journal.id == Publication.journal_id,  Publication.journal_id == None)).\
                        group_by(Publication.id):
            if pub.journal_id == None:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root]
            else:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root]
            tmp.append(c)
        return tmp
    elif key == 'Rok':
        tmp =  []
        for pub, jou in session.query(Publication, Journal).\
                        filter(Publication.year.like('%' + search + '%')).\
                        filter(or_(Journal.id == Publication.journal_id,  Publication.journal_id == None)).\
                        group_by(Publication.id):
            if pub.journal_id == None:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root]
            else:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root]
            tmp.append(c)
        return tmp
    elif key == 'Wydawca':
        tmp =[]
        for pub, jou in session.query(Publication, Journal).\
                        filter(Journal.id == Publication.journal_id).\
                        filter(Journal.full_name.like('%' + search + '%')).group_by(Publication.id):
            c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name]
            tmp.append(c)
        return tmp
    elif key == 'DOI':
        tmp =[]
        for pub, jou in session.query(Publication, Journal).\
                        filter(Publication.doi.like('%' + search + '%')).\
                        filter(or_(Journal.id == Publication.journal_id,  Publication.journal_id == None)).\
                        group_by(Publication.id):
            if pub.journal_id == None:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root]
            else:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root]
            tmp.append(c)
        return tmp
    elif key == 'Grupa':
        tmp = []
        for pub, jou in session.query(Publication, Journal).\
                        filter(GroPer.group_id == Group.id).\
                        filter(GroPer.person_id == Person.id).\
                        filter(PerPub.person_id == Person.id).\
                        filter(PerPub.pub_id == Publication.id).\
                        filter(Group.name.like('%' + search + '%')).\
                        filter(or_(Journal.id == Publication.journal_id,  Publication.journal_id == None)).\
                        group_by(Publication.id):
            if pub.journal_id == None:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root]
            else:
                c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root]
            tmp.append(c)
        
        return tmp
    elif key == 'Adres':
        tmp = []
        for pub, jou in session.query(Publication, Journal).\
                        filter(Journal.id == Publication.journal_id).\
                        filter(Journal.address.like('%' + search + '%')).group_by(Publication.id):
            c = [pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name]
            tmp.append(c)
        return tmp
    else:
        pass
    
## Dokumentacja deleteMultiRecord
# @param session Sesja uzytkownika
# @param data Wartosci wybranej publikacji
#
# @return void
# Funkcja usuwa wszystkie wybrane polaczone publikacje przez uzytkownika
def deleteMultiRecord(session, data):
    for i in range(len(data)):
        id = data[i]
        delPubData(session, id)
    for i in range(len(data)):
        id = data[i]
        for c in session.query(Cite).filter(Cite.pub_ids == id):
            print (c.id_pub_m, c.id)
            session.delete(c)
    session.commit()

## Dokumentacja addUser
# @param session Sesja uzytkownika
# @param data Wartosci dla autora
#
# @return void
# Funkcja dodaje nowego autora do bazy danych
def addUser(session, data):
    user = Person(data['person']['name'],data['person']['surname'], data['person']['filtr'], data['person']['note'])
    session.add(user)
    session.commit()
    tmpPersonID = user.id

    uni = College(data['college']['name'])
    session.add(uni)
    session.commit()

    tmpCollegeID = uni.id
    
    fac = Faculty(tmpCollegeID,  data['faculty']['name'])
    session.add(fac)
    session.commit()

    tmpFacultyID = fac.id

    ins = Institute(tmpFacultyID,  data['institute']['name'])
    session.add(ins)
    session.commit()

    tmpInsID = ins.id

    tmp = ColPer(tmpCollegeID, tmpPersonID)
    session.add(tmp)
    session.commit()
    
## Dokumentacja getUserName
# @param session Sesja uzytkownika
#
# @return list Imie i Nazwisko autora
# Funkcja pobiera wszystkie Imiona i Nazwiska autorów
def getUserName(session):
    result = []
    for per in session.query(Person):
        d = (per.name + ' ' + per.surname)
        result.append(d)
    return result

## Dokumentacja getUserNameID
# @param session Sesja uzytkownika
#
# @return dictioinary Imie i Nazwisko i ID autora
# Funkcja pobiera wszsytkie imiona i nazwiska autorów wraz z ich id w bazie danych
def getUserNameID(session):
    result = {}
    for per in session.query(Person):
        d = (per.name + ' ' + per.surname)
        id = per.id
        tmp = {d:id}
        result.update(tmp)
    return result

## Dokumentacja getUserFilter
# @param session Sesja uzytkownika
#
# @return dictionary Imie, Nazwisko i Filtr autora
# Funkcja pobiera Imie i Nazwisko autora, wraz z wartosciami do filtracji
def getUserFilter(session):
    result = {}
    for per in session.query(Person):
        a = (per.name + ' ' + per.surname)
        b = per.filtr
        d = {a:b}
        result.update(d)
    return result
    
## Dokumentacja addGroup
# @param session Sesja uzytkownika
# @param data Wartosci dla tabeli Group
# @param note Notatka
#
# @return void
# Funkcja dodaje nowa grupe do bazy lub edytuje juz istniejaca
def addGroup(session,  data, note):
    tmp = data[0]
    qGro = session.query(Group).filter(Group.name == tmp[1]).first()
    if qGro == None:
        gro = Group(tmp[1], note)
        session.add(gro)
    if note != '':
        qGro.note = note
    session.commit()
    
    if qGro == None:
        tmpGroID = gro.id
    else:
        tmpGroID = qGro.id
    
    for i in range(len(data)):
        t = data[i]
        g = GroPer(tmpGroID,  int(t[0]))
        session.add(g)
    
    session.commit()
    
## Dokumentacja delGroup
# @param session Sesja uzytkownika
# @param data Nazwa grupy
#
# @return void
# Funkcja usuwa wybrana grupe z bazy danych
def delGroup(session, data):
    gro = session.query(Group).filter(Group.name == data).one()

    for grup, groper in session.query(Group, GroPer).\
            filter(Group.id == gro.id).\
            filter(GroPer.group_id == gro.id):
        print groper
        session.delete(groper)
    
    session.delete(gro)
    session.commit()

## Dokumentacja getGroup
# @param session Sesja uzytkownika
# @param data Nazwa grupy
#
# @return string
# Funkcja pobiera notatke dla wybranej grupy
def getGroup(session, data):
    qGro = session.query(Group).filter(Group.name == data).first()
    result = qGro.note
    return result

## Dokumentacja sendGroupSurname
# @param session Sesja uzytkownika
# @param gname
#
# @return list Lista uzytkowników nalezacej do danej grupy
# Funkcja korzysta z funkcji getUserInGroup
def sendGroupSurname(session, gname):
    data = getUserInGroup(session, gname)
    return data

## Dokumentacja getUserDialog
# @param session Sesja uzytkownika
# @param id ID autora
#
# @return list Dane wybranego autora
# Funkcja pobiera wartosci dla wybranego autora
def getUserDialog(session, id):
    for per, col, fac, ins, colper in session.query(Person, College, Faculty, Institute, ColPer).\
            filter(Person.id == id).\
            filter(ColPer.person_id == Person.id).\
            filter(ColPer.college_id == College.id).\
            filter(College.id == Faculty.college_id).\
            filter(Faculty.id == Institute.faculty_id):
        t = col.name, fac.name, ins.name, per.name, per.surname, per.filtr, per.note
    return t
    
## Dokumentacja editUserDialog
# @param session Sesja uzytkownika
# @param data Wartosci do edycji
# @param id ID wybranego autora
#
# @return void
# Funkcja edytuje wybranego autora o wartosci podane przez uzytkownika
def editUserDialog(session, data, id):
    for per, col, fac, ins, colper in session.query(Person, College, Faculty, Institute, ColPer).\
            filter(Person.id == id).\
            filter(ColPer.person_id == Person.id).\
            filter(ColPer.college_id == College.id).\
            filter(College.id == Faculty.college_id).\
            filter(Faculty.id == Institute.faculty_id):
        t = col.name, fac.name, ins.name, per.name, per.surname, per.filtr, per.note
    
    col.name = data[0]
    fac.name = data[1]
    ins.name = data[2]
    per.name = data[3]
    per.surname = data[4]
    per.filtr = data[5]
    per.note = data[6]
    session.add(col)
    session.add(fac)
    session.add(ins)
    session.add(per)
    session.commit()
    
## Dokumentacja delUserDialog
# @param session Sesja uzytkownika
# @param id ID autora
#
# @return void
# Funkcja usuwa wybranego autora z bay danych ze wszystkimi powiazaniami
def delUserDialog(session, id):
    for perpub in session.query(PerPub).\
            filter(PerPub.person_id == id):
        session.delete(perpub)
    
    for groper in session.query(GroPer).\
            filter(GroPer.person_id == id):
        session.delete(groper)
    
    for per, col, fac, ins, colper in session.query(Person, College, Faculty, Institute, ColPer).\
            filter(Person.id == id).\
            filter(ColPer.person_id == Person.id).\
            filter(ColPer.college_id == College.id).\
            filter(College.id == Faculty.college_id).\
            filter(Faculty.id == Institute.faculty_id):
        t =  col.name, fac.name, ins.name, per.name, per.surname, per.filtr
        session.delete(colper)
        session.delete(col)
        session.delete(fac)
        session.delete(ins)
        session.delete(per)
    
    session.commit()
