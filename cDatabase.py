# -*- coding: utf-8 -*-
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mDatabase import Person, College, Faculty, Institute, Group,  metadata

###################################################
## Polaczone z baza danych
###################################################

def createDatabase():
    metadata.create_all()
    print 'db create'
    
def connectDatabase():
    engine = create_engine("sqlite:///schdatabase.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def addUser(session, data):
    user = Person(data['college']['name'], 'None', data['person']['name'],data['person']['surname'], data['person']['filtr'])
    session.add(user)
    
    fac_query = ins_query = session.query(Faculty.name).filter(Faculty.name == data['faculty']['name']).first()
    if fac_query == None:
        fac = Faculty(data['college']['name'],  data['faculty']['name'])
        session.add(fac)
    
    ins_query = session.query(Institute.name).filter(Institute.name == data['institute']['name']).first()
    if ins_query == None:
        ins = Institute(data['faculty']['name'],  data['institute']['name'])
        session.add(ins)
    
    uni_query = session.query(College.name).filter(College.name == data['college']['name']).first()
    if uni_query == None:
        uni = College(data['college']['name'])
        session.add(uni)
    
    session.commit()
    
def addGroup(session,  data):
    """Pobiera tworzona grupe, sprawdza czy taka istnieje i robi update uzytkownikow o klucz FK"""
#    print data
    for i in range(len(data)):
        tmp = data[i]
        qGro = session.query(Group).filter(Group.name == tmp[1]).first()
        print qGro
        if qGro == None:
            gro = Group(tmp[1])
            session.add(gro)
    
        qPer = session.query(Person).filter(Person.id == tmp[0]).first()
        qPer.group_name = tmp[1]
    
    session.commit()
    
def getUserName(session):
    c = []
    for name, surname in session.query(Person.name, Person.surname):
        d = (name + ' ' + surname)
        c.append(d)
    result = c
    #print result
    return result

def getCollegeName(session):
    c = []
    for name in session.query(College.name).group_by(College.id):
        c.append(name[0])
    result = c
    return result

def getFacultyName(session):
    c = []
    for name in session.query(Faculty.name).group_by(Faculty.id):
        c.append(name[0])
    result = c
    return result

def getInstituteName(session):
    c = []
    for name in session.query(Institute.name).group_by(Institute.id):
        c.append(name[0])
    result = c
    return result

def getAllRecord(session):
    d = []
    for id,  name, surname, filtr in session.query(Person.id,  Person.name, Person.surname, Person.filtr):
        c = (str(id)+ ' ' + name + ' ' + surname)
        d.append(c)
    return d
    
def getGroupName(session):
    result = []
    for name in session.query(Group.name).group_by(Group.id):
        result.append(name[0])
    return result
    

###################################################
## Polaczone z modelem sch.view
###################################################

def getUserFilter(session):
    c = {}
    for name, surname, filtr in session.query(Person.name, Person.surname, Person.filtr):
        a = (name + ' ' + surname)
        b = filtr
        d = {a:b}
        c.update(d)
    result = c
    #print result
    return result
    


#engine = create_engine("sqlite:///schdatabase.db", echo=True)
#Session = sessionmaker(bind=engine)
#session = Session()

#conn = engine.connect()

#leszek = session.query(Person).order_by(Person.id).filter_by(id=2).one()
#print leszek

"""update kolumny dla danej tabeli"""
#u = session.query(Person).order_by(Person.id).filter_by(id=5).one()
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
#for name in session.query(Group.name):
#    print name
#
#for u, a in session.query(College, Person).\
#                        filter(College.name==Person.college_name).\
#                        filter(Person.group_name == 'jakas').group_by(Person.id):
#    print a
