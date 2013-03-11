# -*- coding: utf-8 -*-
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

###################################################
## Polaczone z baza danych
###################################################

def createDatabase():
    """Tworzy baze danych jesli nie istnieje"""
    metadata.create_all()
    
def connectDatabase():
    """Łaczy z baza danych"""
    engine = create_engine("sqlite:///schdatabase.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def getCollegeName(session):
    """Pobiera wszystkie nazwy Uczelni.
    Wykorzystywane przy dodawaniu użytkownika."""
    c = []
    for name in session.query(College.name).group_by(College.name):
        c.append(name[0])
    result = c
    return result

def getFacultyName(session):
    """Pobiera wszystkie nazwy wydziałów.
    Wykorzystywane przy dodawaniu użytkownika."""
    c = []
    for name in session.query(Faculty.name).group_by(Faculty.name):
        c.append(name[0])
    result = c
    return result

def getInstituteName(session):
    """Pobiera wszystkie nazwy Instytutów.
    Wykorzystywane przy dodawaniu użytkownika."""
    c = []
    for name in session.query(Institute.name).group_by(Institute.name):
        c.append(name[0])
    result = c
    return result

def getAllRecord(session):
    """Pobiera z bazy ID, Imie, Nazwisko autorów.
    Zapytanie używane przy dodawaniu autorów do grupy"""
    d = []
    for per in session.query(Person):
        c = (str(per.id)+ ' ' + per.name + ' ' + per.surname)
        d.append(c)
    return d
    
def getGroupName(session):
    """Pobiera wszystkie nazwy grup."""
    result = []
    for name in session.query(Group.name).group_by(Group.id):
        result.append(name[0])
    return result
    
def getUserInGroup(session, gname):
    """Pobiera nazwiska autorów z bazy danych dla odpowiedniej grupy.
    Wykorzystywane przy wyszukiwaniu grupowym."""
    result = []
    for g, p, l in session.query(Group, Person, GroPer).\
                filter(GroPer.person_id == Person.id).\
                filter(GroPer.group_id == Group.id).\
                filter(Group.name == gname).group_by(Person.id):
#        e = unichr(380)
        t = p.surname.encode('utf-8')
        result.append(t)
    return result
    
def getCheckedUser(session, gname):
    """Sprawdza któryz autorzy należa do wybarnej grupy"""
    result = []
    for g, p, pg in session.query(Group, Person, GroPer).\
                filter(Group.id == GroPer.group_id).\
                filter(Person.id == GroPer.person_id).\
                filter(Group.name == gname).group_by(Person.id):
        result.append(p.id)
    return result

def editUserGroup(session, gname):
    """Sprawdza któryz autorzy należa do wybarnej grupy"""
    result = []
    for g, p, pg in session.query(Group, Person, GroPer).\
                filter(Group.id == GroPer.group_id).\
                filter(Person.id == GroPer.person_id).\
                filter(Group.name == gname).group_by(Person.id):
        session.delete(pg)
    session.commit()

###############################################
## zapytania dla generatorów
###############################################

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
    print tmp
    return tmp
    
    
###############################################
## zapytania dla tabeli Cite
###############################################

def deleteCite(session, id, idp):
    for c in session.query(Cite).filter(Cite.pub_ids == idp).filter(Cite.id_pub_m == id):
        session.delete(c)
    session.commit()

def saveCite(session, data):
    """Zapisuje łaczone publikacje do bazy"""
    cit = Cite(data[0], data[1], data[2], data[3])
    session.add(cit)
    session.commit()

def getMergePub(session):
    """Pobiera wszystkie wiodace polaczone publikacje"""
    result = {}
    id_pub = []
    for c in session.query(Cite).group_by(Cite.pub_ids):
        id_pub.append(c.pub_ids)
    
    for i in range(len(id_pub)):
        pub = session.query(Publication).filter(Publication.id == id_pub[i]).first()
#        print pub
        if pub != None:
            tmp = pub.title +' - '+ pub.author +' - '+ str(pub.citation) +' - '+ str(pub.year) +' - '+ pub.root
            d = {id_pub[i]:tmp}
            result.update(d)
#    print result
    return result



def getCitPubData(session):
    """Pobiera wszystkie publikacje jakie sa w bazie danych. Wykorzystywane przy dodawaniu publikacji do łaczenia"""
    result = []
    for pub in session.query(Publication):
        jouID = pub.journal_id
#        print pub.title
    
        if jouID != None:
            jou = session.query(Journal).filter(pub.journal_id == Journal.id).first()
            tmp = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root, pub.urlcit, pub.urlpub)
            result.append(tmp)
        else:
            tmp = (pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root, pub.urlcit, pub.urlpub)
            result.append(tmp)
    return result

def pubCitMerge(session, id):
    """Zapytanie pobiera wszystkie powiazane publikacje z wiodaca"""
    result = []
    idm = []
    for c in session.query(Cite).filter(Cite.pub_ids == id).group_by(Cite.id_pub_m):
        idm.append(c.id_pub_m)
    for i in range(len(idm)):
        pub = session.query(Publication).filter(Publication.id == idm[i]).first()
        tmp = (pub.id, pub.citation, pub.title, pub.author, pub.year, pub.root, pub.doi, pub.urlcit, pub.urlpub)
        result.append(tmp)
#    print result
    return result

###############################################
## zapytania dla tabeli Journal
###############################################

def addJournalData(session, data):
    """Dodawanie nowego wydawcy"""
    tmp =[]
    for t in session.query(Journal).filter(Journal.full_name == data[0]).group_by(Journal.id):
        tmp.append(t)
#    print tmp
    if tmp == []:
        jou = Journal(data[0], data[1], data[2], data[3])
        session.add(jou)
        session.commit()
    else:
        wx.MessageBox(u'Nazwa wydawcy jest unikatowa.\n Nie można dodać drugiego takiego wydawcy.', u'Wydawca istnieje!', wx.OK | wx.ICON_INFORMATION)

def editJournalData(session, data, id):
    """Edytuje wybranego wydawcę"""
    jou = session.query(Journal).filter(Journal.id == id).group_by(Journal.id).first()
#    print jou
    jou.full_name = data[0]
    jou.short_name = data[1]
    jou.address = data[2]
    jou.note = data[3]
    session.add(jou)
    session.commit()

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
#        t = (pub.journal_id, pub.title)
#        print t
    

def getJournalName(session):
    """Pobiera nazwy wydawców"""
    result = []
    for jou in session.query(Journal):
        result.append(jou.full_name)
    return result

def getJournalNameID(session):
    """Pobiera nazwy wydawców wraz z unikatowym numerem ID"""
    result = {}
    for jou in session.query(Journal):
        d = (jou.full_name)
        id = jou.id
        tmp = {d:id}
        result.update(tmp)
    return result

def getJournalData(session, name):
    for jou in session.query(Journal).\
            filter(Journal.full_name == name):
        t = (jou.short_name, jou.address, jou.note)
    return t

def addEmptyString(session):
    jou = Journal('', '', '', '')
    session.add(jou)
    session.commit()
###############################################
## zapytania dla tabeli Publication
###############################################

def getMergePubData(session, id):
    pub = session.query(Publication).filter(Publication.id == id).one()
    result = (pub.id, pub.citation, pub.title, pub.author, pub.year, pub.root, pub.doi, pub.urlcit, pub.urlpub)
    return result

def getPubData(session, id):
    pub = session.query(Publication).filter(Publication.id == id).one()
    jouID = pub.journal_id
    
    if jouID != None:
        jou = session.query(Journal).filter(pub.journal_id == Journal.id).first()
        result = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name, pub.root, pub.urlcit, pub.urlpub)
    else:
        result = (pub.id, pub.citation, pub.title, pub.author, pub.year, '', pub.root, pub.urlcit, pub.urlpub)
    return result

def delPubData(session, id):
    """Usuwa wybrane publikacje z bazy oraz powiazania danej publikacji z autorami
    Wykorzystywane w publikacja.py"""
    pub = session.query(Publication).filter(Publication.id == id).one()
    for pub, perpub in session.query(Publication, PerPub).\
            filter(Publication.id == id).\
            filter(PerPub.pub_id == id):
        session.delete(perpub)

    session.delete(pub)
    session.commit()
    
def addPubData(session, data):
    """Dodaje publikacje do bazy danych wpisana przez uzytkownika"""
    pub = Publication(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[9], data[10], data[11], data[12], data[13], data[14])
    session.add(pub)
    session.commit()
    
    id = data[8]
    for i in range(len(id)):
        tmp = PerPub(int(id[i]), pub.id)
        session.add(tmp)
    
    session.commit()
    


def addPubMultiData(session, data):
    """Dodaje publikacje do bazy danych wpisana przez uzytkownika"""
    
##    pub.title = data[0]
##    pub.author = data[1]
##    pub.citation = data[2]
##    pub.type = data[3]
##    pub.year = data[4]
##    pub.doi = data[5]
##    pub.ident = data[6]
##    pub.journal_id = data[7]
##    self.urlpub = data[8]
##    self.urlcit = data[9]
##    self.root = data[10]
    
    pub = Publication(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13])
    session.add(pub)
    session.commit()

def geteditPubData(session, id):
    """Pobiera dane publikacji o danym ID do pozniejszej edycji"""
    t = []
    print id
    
    pub = session.query(Publication).filter(Publication.id == id).first()
    jouID = pub.journal_id
    
    for pub, per, perpub in session.query(Publication, Person, PerPub).\
            filter(Person.id == PerPub.person_id).\
            filter(Publication.id == PerPub.pub_id).\
            filter(Publication.id == id):
        t.append(per.id)
    print t
    
    if jouID != None:
        jou = session.query(Journal).filter(Journal.id == jouID).first()
        result = (str(pub.id), pub.title, pub.author, pub.citation, pub.type, pub.year, pub.doi, pub.ident, jou.full_name, t, pub.urlpub, pub.urlcit, pub.root, pub.lmcp, pub.jcr, pub.note)
        return result
    else:
        result = (str(pub.id), pub.title, pub.author, pub.citation, pub.type, pub.year, pub.doi, pub.ident, '', t, pub.urlpub, pub.urlcit, pub.root, pub.lmcp, pub.jcr, pub.note)
        return result
    
def editPubData(session, data, id):
    """Edytuje wartości w bazie danych dla danej publikacji"""
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

def getCheckItemAuthor(session, id):
    """Zapytanie zwraca ID użytkowników, którzy sa powiazani z dana publikacja"""
    t = []
    for pub, jou, per, perpub in session.query(Publication, Journal, Person, PerPub).\
            filter(Person.id == PerPub.person_id).\
            filter(Publication.id == PerPub.pub_id).\
            filter(Publication.id == id).group_by(Person.id):
        t.append(per.id)
    return t

def editItemAuthor(session, id):
    """Zapytanie usuwa wszystkich powiazanych autorow z publikacja"""
    t = []
    for pub, per, perpub in session.query(Publication, Person, PerPub).\
            filter(Person.id == PerPub.person_id).\
            filter(Publication.id == PerPub.pub_id).\
            filter(Publication.id == id).group_by(Person.id):
        session.delete(perpub)
    session.commit()

###############################################
## zapytania połaczone widokiem baz.bazView
###############################################

def getLinkPub(session, id):
    link = session.query(Publication).filter(Publication.id == id).one()
    return link.urlpub

def getLinkCit(session, id):
    link = session.query(Publication).filter(Publication.id == id).one()
    return link.urlcit

def getPerPubID(session):
    result = []
    for perpub in session.query(PerPub).group_by(PerPub.pub_id):
        result.append(perpub.pub_id)
    return result

def getCiteID(session):
    result = []
    for cit in session.query(Cite).group_by(Cite.pub_ids):
        t = (cit.pub_ids, cit.allcit)
        result.append(t)
    print result
    return result

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

###################################################
## Polaczone z widokiem sch.view, zapytani głównie dla tabeli Person
###################################################

def addUser(session, data):
    """Dodaje nowego użytkownika do bazy danych. 
    Uzupełnia tabele asocjacyjna pomiedzy użytkownikiem a uczelnia"""
    print data
    user = Person(data['person']['name'],data['person']['surname'], data['person']['filtr'], data['person']['note'])
    session.add(user)
    session.commit()
    tmpPersonID = user.id
    print tmpPersonID
    
#    uni_query = session.query(College).filter(College.name == data['college']['name']).first()
#    if uni_query == None:
    uni = College(data['college']['name'])
    session.add(uni)
    session.commit()
    
#    if uni_query == None:
    tmpCollegeID = uni.id
#    else:
#        tmpCollegeID = uni_query.id
    print tmpCollegeID
    
#    fac_query = session.query(Faculty).filter(Faculty.name == data['faculty']['name']).first()
#    if fac_query == None:
    fac = Faculty(tmpCollegeID,  data['faculty']['name'])
    session.add(fac)
    session.commit()
    
#    if fac_query == None:
    tmpFacultyID = fac.id
#    else:
#        tmpFacultyID = fac_query.id
    print tmpFacultyID
    
    
#    ins_query = session.query(Institute).filter(Institute.name == data['institute']['name']).first()
#    if ins_query == None:
    ins = Institute(tmpFacultyID,  data['institute']['name'])
    session.add(ins)
    session.commit()
    
#    if ins_query == None:
    tmpInsID = ins.id
#    else:
#        tmpInsID = ins_query.id
    print tmpInsID
    
    tmp = ColPer(tmpCollegeID, tmpPersonID)
    session.add(tmp)
    session.commit()
    
def getUserName(session):
    """Pobiera imie i nazwisko z bazy.
    Wykorzystywane do wyswietlania autorów przy wyborze do filtracji danych."""
    result = []
    for per in session.query(Person):
        d = (per.name + ' ' + per.surname)
        result.append(d)
    return result

def getUserNameID(session):
    """Pobiera imie i nazwisko z bazy, w połaczeniu z ID"""
    result = {}
    for per in session.query(Person):
        d = (per.name + ' ' + per.surname)
        id = per.id
        tmp = {d:id}
        result.update(tmp)
#        print tmp
    return result

def getUserFilter(session):
    """Pobieranie wszystkich informacji o autorze.
    Tworzenie słownika na podstawie którego odbywa się filtracja danych dla wybranego użytkownika."""
    result = {}
    for per in session.query(Person):
        a = (per.name + ' ' + per.surname)
        b = per.filtr
        d = {a:b}
        result.update(d)
    return result

###################################################
## zapytania dla tabeli Group
###################################################
    
def addGroup(session,  data, note):
    """Pobiera tworzona grupe, sprawdza czy taka istnieje i robi update uzytkownikow o klucz FK
    Dodaje też dane do tablicy asocjacyjnej pomiędzy Groupa i Autorem"""
#    print data
    tmp = data[0]
#    print tmp
    qGro = session.query(Group).filter(Group.name == tmp[1]).first()
    if qGro == None:
        gro = Group(tmp[1], note)
        session.add(gro)
    if note != '':
        qGro.note = note
    session.commit()
    
    if qGro == None:
        tmpGroID = gro.id
#        print tmpGroID
    else:
        tmpGroID = qGro.id
#        print tmpGroID
    
    
    for i in range(len(data)):
        t = data[i]
        g = GroPer(tmpGroID,  int(t[0]))
        session.add(g)
    
    session.commit()
    
def delGroup(session, data):
    """Usuwa grupy, wraz z powiazanymi autorami"""
    gro = session.query(Group).filter(Group.name == data).one()

    for grup, groper in session.query(Group, GroPer).\
            filter(Group.id == gro.id).\
            filter(GroPer.group_id == gro.id):
        print groper
        session.delete(groper)
    
    session.delete(gro)
    session.commit()

def getGroup(session, data):
    qGro = session.query(Group).filter(Group.name == data).first()
    result = qGro.note
    return result
    
###################################################
## Polaczone z modelem sch.model
###################################################

def sendGroupSurname(session, gname):
    """Zwraca naziwska autorów dla których odbędzie sie wyszkuwanie grupowe."""
    data = getUserInGroup(session, gname)
    return data

###################################################
## Połaczone z autor.py
###################################################

def getUserDialog(session, id):
    """Pobiera z bazy dane na temat wybranego autora"""
    for per, col, fac, ins, colper in session.query(Person, College, Faculty, Institute, ColPer).\
            filter(Person.id == id).\
            filter(ColPer.person_id == Person.id).\
            filter(ColPer.college_id == College.id).\
            filter(College.id == Faculty.college_id).\
            filter(Faculty.id == Institute.faculty_id):
        t = col.name, fac.name, ins.name, per.name, per.surname, per.filtr, per.note
    return t
    
def editUserDialog(session, data, id):
    """Edytuje nowego użytkownika"""
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
    
def delUserDialog(session, id):
    """usuwa wybranego użytkownika i wszystkie powizane z nim tabele"""
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


