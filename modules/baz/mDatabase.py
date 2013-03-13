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

from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, Unicode, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relation, relationship

#połaczenie z baza danych
engine = create_engine("sqlite:///schdatabase.db", echo=True) 
#deklaracja mapowania
DeclarativeBase = declarative_base(engine) 
#polaczenie klas z opisem tabel wraz z fizyczna tabela w bazie danych
metadata = DeclarativeBase.metadata 

## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli Person
class Person(DeclarativeBase):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    filtr = Column(String)
    note = Column(String)
    
    ## Konstruktor
    def __init__(self, name, surname, filtr, note):
        self.name = name
        self.surname = surname
        self.filtr = filtr
        self.note = note
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s','%s','%s','%s')" % (self.name, 
            self.surname, self.filtr, self.note)

## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli College
class College(DeclarativeBase):
    __tablename__ = 'college'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    ## Konstruktor
    def __init__(self, name):
        self.name = name
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s')" % (self.name)
    
## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli Faculty
class Faculty(DeclarativeBase):
    __tablename__ = 'faculty'
    
    id = Column(Integer, primary_key=True)
    college_id = Column(Integer, ForeignKey('college.id'))
    name = Column(String)
    college = relation("College",  backref='faculty')
    
    ## Konstruktor
    def __init__(self, college_id,  name):
        self.college_id = college_id
        self.name = name
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s','%s')" % (self.college_id,  self.name)
    
## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli Institute
class Institute(DeclarativeBase):
    __tablename__ = 'institute'
    
    id = Column(Integer, primary_key=True)
    faculty_id = Column(String, ForeignKey('faculty.id'))
    name = Column(String)
    faculty = relation('Faculty',  backref='institute')
    
    ## Konstruktor
    def __init__(self, faculty_id,  name):
        self.faculty_id = faculty_id
        self.name = name
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s','%s')" % (self.faculty_id,  self.name)

## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli Group
class Group(DeclarativeBase):
    __tablename__ = 'group'
    
    id = Column(Integer, primary_key=True)
    name = Column(String,  unique=True)
    note = Column(String)
    
    ## Konstruktor
    def __init__(self, name, note):
        self.name = name
        self.note = note
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s','%s')" % (self.name, self.note)
    
## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli ColPer
class ColPer(DeclarativeBase):
    """Tabela asocjacyjna tabel Person oraz College"""
    __tablename__ = 'colper'
    
    college_id = Column(Integer, ForeignKey('college.id'),  primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'),  primary_key=True)
    college = relation("College",  backref='colper')
    person = relation("Person",  backref='colper')
    
    ## Konstruktor
    def __init__(self, college_id,  person_id):
        self.college_id = college_id
        self.person_id = person_id
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __rerp__(self):
        return "('%s','%s')" % (self.college_id,  self.person_id)

## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli GroPer
class GroPer(DeclarativeBase):
    """Tabela asocjacyjna tabel Person oraz Group"""
    __tablename__ = 'groper'
    
    group_id = Column(Integer, ForeignKey('group.id'),  primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'),  primary_key=True)
    group = relation("Group",  backref='groper')
    person = relation("Person",  backref='groper')
    
    ## Konstruktor
    def __init__(self, group_id,  person_id):
        self.group_id = group_id
        self.person_id = person_id
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __rerp__(self):
        return "('%i','%i')" % (self.group_id,  self.person_id)
    
## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli Publication
class Publication(DeclarativeBase):
    __tablename__ = 'publication'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    citation = Column(Integer)
    type = Column(String)
    year = Column(Integer)
    doi = Column(String)
    ident = Column(String)
    journal_id = Column(Integer, ForeignKey('journal.id'))
    urlpub = Column(String)
    urlcit = Column(String)
    root = Column(String)
    lmcp = Column(String)
    jcr = Column(String)
    note = Column(String)
    journal = relation('Journal',  backref='publication')
    
    ## Konstruktor
    def __init__(self, title, author, citation, type, year, doi, ident, journal_id, urlpub, urlcit, root, lmcp, jcr, note):
        self.title = title
        self.author = author
        self.citation = citation
        self.type = type
        self.year = year
        self.doi = doi
        self.ident = ident
        self.journal_id = journal_id
        self.urlpub = urlpub
        self.urlcit = urlcit
        self.root = root
        self.lmcp = lmcp
        self.jcr = jcr
        self.note = note
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s','%s','%i','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.title, self.author, self.citation, self.type, self.year, self.doi, self.ident, self.journal_id, self.urlpub, self.urlcit, self.root, self.lmcp, self.jcr, self.note)
    
## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli Journal
class Journal(DeclarativeBase):
    __tablename__ = 'journal'
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    short_name = Column(String)
    address = Column(String)
    note = Column(String)
    
    ## Konstruktor
    def __init__(self, full_name, short_name, address, note):
        self.full_name = full_name
        self.short_name = short_name
        self.address = address
        self.note = note
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s','%s','%s','%s')" % (self.full_name,  self.short_name,  self.address, self.note)

## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli Cite
class Cite(DeclarativeBase):
    __tablename__ = 'cite'
    
    id = Column(Integer, primary_key=True)
    urlcit = Column(String)
    allcit = Column(String)
    id_pub_m = Column(Integer)
    pub_ids = Column(Integer, ForeignKey('publication.id'))
    public = relation("Publication",  backref='cite')
    
    ## Konstruktor
    def __init__(self, urlcit, allcit, id_pub_m, pub_ids):
        self.urlcit = urlcit
        self.allcit = allcit
        self.id_pub_m = id_pub_m
        self.pub_ids =pub_ids
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s','%s','%s','%s')" % (self.urlcit, self.allcit, self.id_pub_m, self.pub_ids)

## Dokumentacja dla klasy
#
# Klasa zawiera obiekty z tabeli PerPub
class PerPub(DeclarativeBase):
    __tablename__ = 'perpub'
    
    person_id = Column(Integer, ForeignKey('person.id'),  primary_key=True)
    pub_id = Column(Integer, ForeignKey('publication.id'),  primary_key=True)
    person = relation("Person",  backref='perpub')
    pub = relation("Publication",  backref='perpub')
    
    ## Konstruktor
    def __init__(self, person_id, pub_id):
        self.person_id = person_id
        self.pub_id = pub_id
    
    ##Dokumentacja __repr__
    # @param self Wskaźnik obiektu
    def __repr__(self):
        return "('%s','%s')" % (self.person_id, self.pub_id)

