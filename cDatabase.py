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

from modules.sch.schModel import sModel
from modules.men.menModel import mModel


from mDatabase import Person, College, Faculty, Institute, Group, ColPer, GroPer, Publication, Journal, PerPub, metadata

###################################################
## Polaczone z modelami
###################################################

mmodel = mModel()

def getChoiceRecord(session, data):
    tmp = []
    for i in range(len(data)):
        print data[i]
        for p, j in session.query(Publication, Journal).\
                filter(Publication.id == data[i]).\
                filter(Publication.journal_id == Journal.id):
            t = ('', p.citation, p.title, p.author, p.year, j.full_name)
            tmp.append(t)
#    return tmp
    
    mmodel.getBaseData(tmp)
#    return t
    


###################################################
## Polaczone z baza danych
###################################################

schmodel = sModel()

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
        e = unichr(380)
        t = p.surname.encode('utf-8')
        result.append(t)
    return result
    
def getCheckedUser(session, gname):
    result = []
    for g, p, pg in session.query(Group, Person, GroPer).\
                filter(Group.id == GroPer.group_id).\
                filter(Person.id == GroPer.person_id).\
                filter(Group.name == gname).group_by(Person.id):
        result.append(p.id)
    return result
    
###############################################
## zapytania dla tabeli Journal
###############################################

def addJournalData(session, data):
    """Dodawanie nowego wydawcy"""
    tmp =[]
    for t in session.query(Journal).filter(Journal.full_name == data[0]).group_by(Journal.id):
        tmp.append(t)
    print tmp
    if tmp == []:
        jou = Journal(data[0], data[1], data[2])
        session.add(jou)
        session.commit()
    else:
        wx.MessageBox(u'Nazwa wydawcy jest unikatowa.\n Nie można dodać drugiego takiego wydawcy.', u'Wydawca istnieje!', wx.OK | wx.ICON_INFORMATION)

def editJournalData(session, data):
    """Edytuje wybranego wydawcę"""
    jou = session.query(Journal).filter(Journal.full_name == data[0]).group_by(Journal.id).first()
    print jou
    if jou != None:
        jou.full_name = data[0]
        jou.short_name = data[1]
        jou.issn = data[2]
        session.add(jou)
        session.commit()
    else:
        raise RuntimeError, wx.MessageBox(u'Brak takiego wydawcy.\n Rekord nie istnieje w bazie.', u'Wydawca nie istnieje!', wx.OK | wx.ICON_INFORMATION)

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
        t = (jou.short_name, jou.issn)
    return t
    
###############################################
## zapytania dla tabeli Publication
###############################################

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
    pub = Publication(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], '', '')
    session.add(pub)
    session.commit()
    
    id = data[8]
    for i in range(len(id)):
        tmp = PerPub(int(id[i]), pub.id)
        session.add(tmp)
    
    session.commit()
    
#def addPubSearchData(session, data):
    

def geteditPubData(session, id):
    """Pobiera dane publikacji o danym ID do pozniejszej edycji"""
    t = []
    for pub, jou, per, perpub in session.query(Publication, Journal, Person, PerPub).\
            filter(Journal.id == Publication.journal_id).\
            filter(Person.id == PerPub.person_id).\
            filter(Publication.id == PerPub.pub_id).\
            filter(Publication.id == id).group_by(Person.id):
        t.append(per.id)
    result = (str(pub.id), pub.title, pub.author, pub.citation, pub.type, pub.year, pub.doi, pub.ident, jou.full_name, t)
    return result
    
def editPubData(session, data, id):
    """Edytuje wartości w bazie danych dla danej publikacji"""
    print data, id
    for pub, jou, per, perpub in session.query(Publication, Journal, Person, PerPub).\
            filter(Journal.id == Publication.journal_id).\
            filter(Person.id == PerPub.person_id).\
            filter(Publication.id == PerPub.pub_id).\
            filter(Publication.id == id).group_by(Person.id):
        print pub.id

    pub.title = data[0]
    pub.author = data[1]
    pub.citation = data[2]
    pub.type = data[3]
    pub.year = data[4]
    pub.doi = data[5]
    pub.ident = data[6]
    pub.journal_id = data[7]
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
    

###############################################
## zapytania połaczone widokiem baz.bazView
###############################################



def getRecords(session, key, search):
    if search == '*' and key != '':
        tmp = []
        for pub, jou, per, perpub in session.query(Publication, Journal, Person, PerPub).\
                        filter(Journal.id == Publication.journal_id).\
                        group_by(Publication.id):
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    elif key == 'AutorID':
        tmp = []
        for per, pub, jou, perpub in session.query(Person, Publication, Journal, PerPub).\
                        filter(PerPub.person_id == Person.id).\
                        filter(PerPub.pub_id == Publication.id).\
                        filter(or_(Person.name.like('%' + search + '%'), Person.surname.like('%' + search + '%'))).\
                        filter(Journal.id == Publication.journal_id).group_by(Publication.id):
            print per.name, per.surname, pub.title, jou.full_name
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    elif key == 'Autor':
        tmp =[]
        print search
        for pub, jou in session.query(Publication, Journal).\
                        filter(Publication.author.like('%' + search + '%')).\
                        filter(Journal.id == Publication.journal_id).group_by(Publication.id):
#            print pub.title, jou.full_name
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    elif key == 'Tytul':
        tmp =[]
        for pub, jou in session.query(Publication, Journal).\
                        filter(Publication.title.like('%' + search + '%')).\
                        filter(Journal.id == Publication.journal_id).group_by(Publication.id):
            print pub.title, jou.full_name
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    elif key == 'Rok':
        tmp =  []
        for pub, jou in session.query(Publication, Journal).\
                        filter(Journal.id == Publication.journal_id).\
                        filter(Publication.year == search).group_by(Publication.id):
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    elif key == 'Wydawca':
        tmp =[]
        for pub, jou in session.query(Publication, Journal).\
                        filter(Journal.id == Publication.journal_id).\
                        filter(Journal.full_name.like('%' + search + '%')).group_by(Publication.id):
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    elif key == 'DOI':
        tmp =[]
        for pub, jou in session.query(Publication, Journal).\
                        filter(Journal.id == Publication.journal_id).\
                        filter(Publication.doi == search).group_by(Publication.id):
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    elif key == 'Grupa':
        tmp = []
        for pub, jou, gro, groper, per, perpub in session.query(Publication, Journal, Group, GroPer, Person, PerPub).\
                        filter(Journal.id == Publication.journal_id).\
                        filter(GroPer.group_id == Group.id).\
                        filter(GroPer.person_id == Person.id).\
                        filter(PerPub.person_id == Person.id).\
                        filter(PerPub.pub_id == Publication.id).\
                        filter(Group.name == search).group_by(Publication.id):
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    elif key == 'ISSN':
        tmp = []
        for pub, jou, per, perpub in session.query(Publication, Journal, Person, PerPub).\
                        filter(Journal.id == Publication.journal_id).\
                        filter(Journal.issn == search).group_by(Publication.id):
            c = (pub.id, pub.citation, pub.title, pub.author, pub.year, jou.full_name)
            tmp.append(c)
        return tmp
    else:
        print 'tak'
    

###################################################
## Polaczone z widokiem sch.view, zapytani głównie dla tabeli Person
###################################################

def addUser(session, data):
    """Dodaje nowego użytkownika do bazy danych. 
    Uzupełnia tabele asocjacyjna pomiedzy użytkownikiem a uczelnia"""
    user = Person(data['person']['name'],data['person']['surname'], data['person']['filtr'])
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
    
def addGroup(session,  data):
    """Pobiera tworzona grupe, sprawdza czy taka istnieje i robi update uzytkownikow o klucz FK
    Dodaje też dane do tablicy asocjacyjnej pomiędzy Groupa i Autorem"""
    tmp = data[0]
    qGro = session.query(Group).filter(Group.name == tmp[1]).first()
    if qGro == None:
        gro = Group(tmp[1])
        session.add(gro)
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
        t = col.name, fac.name, ins.name, per.name, per.surname, per.filtr
    return t
    
def editUserDialog(session, data, id):
    """Edytuje nowego użytkownika"""
    for per, col, fac, ins, colper in session.query(Person, College, Faculty, Institute, ColPer).\
            filter(Person.id == id).\
            filter(ColPer.person_id == Person.id).\
            filter(ColPer.college_id == College.id).\
            filter(College.id == Faculty.college_id).\
            filter(Faculty.id == Institute.faculty_id):
        t = col.name, fac.name, ins.name, per.name, per.surname, per.filtr
    
    col.name = data[0]
    fac.name = data[1]
    ins.name = data[2]
    per.name = data[3]
    per.surname = data[4]
    per.filtr = data[5]
    session.add(col)
    session.add(fac)
    session.add(ins)
    session.add(per)
    session.commit()
    
def delUserDialog(session, id):
    """usuwa wybranego użytkownika i wszystkie powizane z nim tabele"""
    for perpub in session.query(PerPub).\
            filter(PerPub.person_id == id):
        print perpub
        session.delete(perpub)
    
    for groper in session.query(GroPer).\
            filter(GroPer.person_id == id):
        print groper
        session.delete(groper)
    
    for per, col, fac, ins, colper in session.query(Person, College, Faculty, Institute, ColPer).\
            filter(Person.id == id).\
            filter(ColPer.person_id == Person.id).\
            filter(ColPer.college_id == College.id).\
            filter(College.id == Faculty.college_id).\
            filter(Faculty.id == Institute.faculty_id):
        t =  col.name, fac.name, ins.name, per.name, per.surname, per.filtr
        print t
        session.delete(colper)
        session.delete(col)
        session.delete(fac)
        session.delete(ins)
        session.delete(per)
    
    session.commit()

#engine = create_engine("sqlite:///schdatabase.db", echo=True)
#Session = sessionmaker(bind=engine)
#session = Session()
#getJournalName(session)

#getUserNameID(session)
#for per, col, fac, ins, colper in session.query(Person, College, Faculty, Institute, ColPer).\
#            filter(Person.id == 3).\
#            filter(ColPer.person_id == Person.id).\
#            filter(ColPer.college_id == College.id).\
#            filter(College.id == Faculty.college_id).\
#            filter(Faculty.id == Institute.faculty_id).group_by(Person.id):
#    print col.name, fac.name, ins.name, per.name, per.surname, per.filtr

#for per, col, cp in session.query(Person, College, ColPer).\
#        filter(Person.id == 1).\
#        filter(ColPer.person_id == Person.id).\
#        filter(ColPer.college_id == College.id):
#    print col.id, col.name, per.name, per.surname, per.filtr
#colid = col.id
#
#for col, fac in session.query(College, Faculty).\
#        filter(College.id == colid).\
#        filter(Faculty.college_id == colid):
#    print col.name, fac.name
    

#t = session.query.join(College.faculty)
#print t

#t = session.query(Person).get(1)
#print t 
    #print col.name, fac.name, ins.name, per.name, per.surname, per.filtr

#getCheckItemAuthor(session, 1)

#editPubData(session, 1)
#for pub, jou, per, perpub in session.query(Publication, Journal, Person, PerPub).\
#                        filter(Journal.id == Publication.journal_id).\
#                        filter(Person.id == PerPub.person_id).\
#                        filter(Publication.id == PerPub.pub_id).\
#                        filter(Publication.id == 1).group_by(Publication.id):
#    print pub.title, pub.author, pub.citation, pub.type, pub.year, pub.doi, pub.ident, jou.full_name
#    
#for per, pub, perpub in session.query(Person, Publication, PerPub).\
#                        filter(Person.id == PerPub.person_id).\
#                        filter(Publication.id == PerPub.pub_id).\
#                        filter(Publication.id == 1).group_by(Person.id):
#        print per.id
##
#for pub in session.query(Publication):
#    print pub.title, pub.author, pub.year, pub.journal_id, pub.doi

#for jou in session.query(Journal):
#    print jou
#    

#for per_name, per_surname, pub_title, jou_name, perpub in session.query(Person.name, Person.surname, Publication.title, Journal.full_name, PerPub).\
#                        filter(PerPub.person_id == Person.id).\
#                        filter(PerPub.pub_id == Publication.id).\
#                        filter(or_(Person.name.like('%' + search + '%'), Person.surname.like('%' + search + '%'))).group_by(Publication.id):
#    print per_name, per_surname, pub_title, jou_name

#for p in session.query(Publication):
#    print p
#
#for pub_tit, pub_y, jou in session.query(Publication.title, Publication.year, Journal.full_name).\
#                        group_by(Publication.id):
#    print pub_tit, pub_y, jou

#sendGroupSurname()
#
#for g, p, l in session.query(Group, Person.filtr, GroPer).\
#                filter(GroPer.person_id == Person.id).\
#                filter(GroPer.group_id == Group.id).\
#                filter(Group.name == 'm72').group_by(Person.id):
#    print p
#    
#
#t = session.query(ColPer.college_id,  ColPer.person_id).all()
#print t

#t = session.query(Person).get(3)
#print t.id
#
#uni_query = session.query(College).filter(College.name == 'Politechnika').first()
#print uni_query.id

#uni = College('agh')
#session.add(uni)
#session.commit()
#print uni.id

#conn = engine.connect()

#leszek = session.query(Person).order_by(Person.id).filter_by(id=2).one()
#print leszek

"""update kolumny dla danej tabeli"""
#u = session.query(Person).filter(Person.id == 1).update({"filtr":'W Czyzycki, W Czyżycki'}, synchronize_session=False)
#session.commit()


#print u[0]
#u[0] = 'W Czyżycki, W Czyzycki, W CZYZYCKI, W CZYŻYCKI'
#session.add(u[0])
#session.commit()
#u.group_id = 'zmieniona nazwa'
#session.commit()
"""dodawanie nowych obiektow z relacja pomiedzy bazami"""
#d = College('Politechnika Krakowska')
#d.person = [Person('ktos', 'ktos', 'ktos'), Person('ktos', 'ktos', 'ktos')]
#session.add(d)
#session.commit()

#x = Group('m72')
#session.add(x)
#session.commit()

#c = session.query(College).filter_by(id=4).one()
#print c
#
#print c.person

#x = session.query(Person).filter_by()
#########################################
#for instance in session.query(Person).all(): 
#    print 't'
#
#for id,  name, surname, filtr,  person_college_name in session.query(Person.id,  Person.name, Person.surname, Person.filtr,  Person.college_name):
#    print id, name, surname, filtr,  person_college_name
#cd = Person()
#ed = Group()
#ed.person_id = 1
#ed.name = 'm72'
#session.add(ed)

#for id, person_id, name in session.query(Group.id,  Group.person_id,  Group.name):
#    print id,  person_id,  name

#t = session.query(College).all()
#print t
#t = session.query(Group).all()
#print t
#x = session.query(GroPer).all()
#print x
#for name in session.query(Group.name):
#    print name

#for u, p,  c in session.query(College, Person,  ColPer).\
#                        filter(Person.id == ColPer.person_id).\
#                        filter(College.id == ColPer.college_id).group_by(Person.id):
#    print p,  u,  c.college_id,  c.person_id
##('asd','asd','asd') ('Uczelnia') 1 1
##('qwe','qwe','qwe') ('Uczelnia') 1 2
##('asd','as','asd') ('Politechnika') 2 3
