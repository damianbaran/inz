# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, Unicode, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relation, relationship

engine = create_engine("sqlite:///schdatabase.db", echo=True) #połaczenie z baza danych
DeclarativeBase = declarative_base(engine) #deklaracja mapowania
metadata = DeclarativeBase.metadata #polaczenie klas z opisem tabel wraz z fizyczna tabela w bazie danych

###########################################
class Person(DeclarativeBase):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    college_name = Column(String, ForeignKey('college.name'))
    group_name = Column(String, ForeignKey('group.name'))
    name = Column(String)
    surname = Column(String)
    filtr = Column(String)
    college = relation("College",  backref='person')
    group = relation("Group",  backref='person')
    
    def __init__(self, college_name, group_name, name, surname, filtr):
        self.college_name = college_name
        self.group_name = group_name
        self.name = name
        self.surname = surname
        self.filtr = filtr

    def __repr__(self):
        return "Person('%s','%s','%s','%s','%s')" % (self.college_name,  self.group_name,  self.name, self.surname, self.filtr)

###########################################
class College(DeclarativeBase):
    __tablename__ = 'college'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "College('%s')" % (self.name)
    
###########################################
class Faculty(DeclarativeBase):
    __tablename__ = 'faculty'
    
    id = Column(Integer, primary_key=True)
    college_name = Column(String, ForeignKey('college.name'))
    name = Column(String)
    college = relation("College",  backref='faculty')
    
    def __init__(self, college_name,  name):
        self.college_name = college_name
        self.name = name
        
    def __repr__(self):
        return "Faculty('%s','%s')" % (self.college_name,  self.name)
    
###########################################
class Institute(DeclarativeBase):
    __tablename__ = 'institute'
    
    id = Column(Integer, primary_key=True)
    faculty_name = Column(String, ForeignKey('faculty.name'))
    name = Column(String)
    faculty = relation('Faculty',  backref='institute')
    
    def __init__(self, faculty_name,  name):
        self.faculty_name = faculty_name
        self.name = name
        
    def __repr__(self):
        return "Institue('%s','%s')" % (self.faculty_name,  self.name)

###########################################
class Group(DeclarativeBase):
    __tablename__ = 'group'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return "Group('%s')" % (self.name)
    
