# -*- coding: utf-8 -*-
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#### wyjatki
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm.interfaces
import sqlalchemy.exc
import sqlalchemy.orm.exc

from modules.sch.schModel import sModel


from mDatabase import Person, College, Faculty, Institute, Group, ColPer, GroPer, Publication, Journal, PerPub, metadata

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
    for name in session.query(College.name).group_by(College.id):
        c.append(name[0])
    result = c
    return result

def getFacultyName(session):
    """Pobiera wszystkie nazwy wydziałów.
    Wykorzystywane przy dodawaniu użytkownika."""
    c = []
    for name in session.query(Faculty.name).group_by(Faculty.id):
        c.append(name[0])
    result = c
    return result

def getInstituteName(session):
    """Pobiera wszystkie nazwy Instytutów.
    Wykorzystywane przy dodawaniu użytkownika."""
    c = []
    for name in session.query(Institute.name).group_by(Institute.id):
        c.append(name[0])
    result = c
    return result

def getAllRecord(session):
    """Pobiera z bazy ID, Imie, Nazwisko autorów.
    Zapytanie używane przy dodawaniu autorów do grupy"""
    d = []
    for id,  name, surname, filtr in session.query(Person.id,  Person.name, Person.surname, Person.filtr):
        c = (str(id)+ ' ' + name + ' ' + surname)
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
    for g, p, l in session.query(Group, Person.surname, GroPer).\
                filter(GroPer.person_id == Person.id).\
                filter(GroPer.group_id == Group.id).\
                filter(Group.name == gname).group_by(Person.id):
        result.append(p)
#    print result
    return result
    
def getCheckedUser(session, gname):
    result = []
    for g, p, pg in session.query(Group, Person.id, GroPer).\
                filter(Group.id == GroPer.group_id).\
                filter(Person.id == GroPer.person_id).\
                filter(Group.name == gname).group_by(Person.id):
        result.append(p)
    return result
    
###############################################
## metody polaczone z widokiem baz.bazView
###############################################
    
def addPubData(session,  data):

    jouid = data[6].split(' ')
    jouid = jouid[0]

    pub = Publication(data[0], data[1], data[2], data[3], data[4], data[5],  jouid)
    session.add(pub)
    session.commit()
    
    id = data[7]
    for i in range(len(id)):
        print id[i]
        tmp = PerPub(int(id[i]), pub.id)
        session.add(tmp)
    
    session.commit()
    
def setJournalData(session,  data):
    print data
    jou = Journal(data[0], data[1], data[2])
    session.add(jou)
    session.commit()
    
def getJournalName(session):
    result = []
    for id, name in session.query(Journal.id, Journal.full_name).group_by(Journal.id):
        print id
        t = name
        result.append(str(id) + ' ' +  t)
    return result
    
def getRecords(session, key, search):
    if key == 'Autor':
        print 'tak autor'
#        for per, pub, jou in session.query(Person.name, Person.surname, Publication.title, Journal.full_name, PerPub):
    elif key == 'Tytuł':
        print 'tak tytul'
    elif key == 'Rok':
        t =  []
        print 'tak rok'
        for pub_tit, pub_y, jou in session.query(Publication.title, Publication.year, Journal.full_name).\
                        filter(Journal.id == Publication.journal_id).\
                        filter(Publication.year == search).group_by(Publication.id):
            print pub_tit, pub_y, jou
            c = ('','1', pub_tit, 'autor', pub_y, jou)
            t.append(c)
        return t
    elif key == 'Wydawca':
        print 'tak wydawca'
    
    

###################################################
## Polaczone z widokiem sch.view
###################################################

def addUser(session, data):
    """Dodaje nowego użytkownika do bazy danych. 
    Uzupełnia tabele asocjacyjna pomiedzy użytkownikiem a uczelnia"""
    user = Person(data['person']['name'],data['person']['surname'], data['person']['filtr'])
    session.add(user)
    session.commit()
    tmpPersonID = user.id
    
    uni_query = session.query(College).filter(College.name == data['college']['name']).first()
    if uni_query == None:
        uni = College(data['college']['name'])
        session.add(uni)
    session.commit()
    
    if uni_query == None:
        tmpCollegeID = uni.id
    else:
        tmpCollegeID = uni_query.id
    
    
    fac_query = session.query(Faculty).filter(Faculty.name == data['faculty']['name']).first()
    if fac_query == None:
        fac = Faculty(tmpCollegeID,  data['faculty']['name'])
        session.add(fac)
    session.commit()
    
    if fac_query == None:
        tmpFacultyID = fac.id
    else:
        tmpFacultyID = fac_query.id
    
    
    ins_query = session.query(Institute).filter(Institute.name == data['institute']['name']).first()
    if ins_query == None:
        ins = Institute(tmpFacultyID,  data['institute']['name'])
        session.add(ins)
    session.commit()
    
    tmp = ColPer(tmpCollegeID, tmpPersonID)
    session.add(tmp)
    session.commit()
    
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
        print tmpGroID
    else:
        tmpGroID = qGro.id
        print tmpGroID
    
    
    for i in range(len(data)):
        t = data[i]
        g = GroPer(tmpGroID,  int(t[0]))
        try:
            session.add(g)
            session.flush()
        except sqlalchemy.exc.IntegrityError, exc:
            reason = exc.message
            if reason.endswith('is not unique'):
                print "%s already exists" % exc.params[0]
                session.rollback()
    
    session.commit()
    
def getUserName(session):
    """Pobiera imie i nazwisko z bazy.
    Wykorzystywane do wyswietlania autorów przy wyborze do filtracji danych."""
    c = []
    for name, surname in session.query(Person.name, Person.surname):
        d = (name + ' ' + surname)
        c.append(d)
    result = c
    #print result
    return result

def getUserFilter(session):
    """Pobieranie wszystkich informacji o autorze.
    Tworzenie słownika na podstawie którego odbywa się filtracja danych dla wybranego użytkownika."""
    c = {}
    for name, surname, filtr in session.query(Person.name, Person.surname, Person.filtr):
        a = (name + ' ' + surname)
        b = filtr
        d = {a:b}
        c.update(d)
    result = c
    #print result
    return result
    
###################################################
## Polaczone z modelem sch.model
###################################################

def sendGroupSurname(session, gname):
    """Zwraca naziwska autorów dla których odbędzie sie wyszkuwanie grupowe."""
    data = getUserInGroup(session, gname)
    return data

#engine = create_engine("sqlite:///schdatabase.db", echo=True)
#Session = sessionmaker(bind=engine)
#session = Session()

#sendGroupSurname()

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
