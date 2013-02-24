# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, Unicode, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relation, relationship

engine = create_engine("sqlite:///schdatabase.db", echo=True) #połaczenie z baza danych
DeclarativeBase = declarative_base(engine) #deklaracja mapowania
metadata = DeclarativeBase.metadata #polaczenie klas z opisem tabel wraz z fizyczna tabela w bazie danych

###########################################
## Documentation for a class.
#   
#   More details.
class Person(DeclarativeBase):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    filtr = Column(String)
    
    ## The constructor.
    #  @param self name.
    #  @param self surname.
    #  @param self filtr.
    def __init__(self, name, surname, filtr):
        self.name = name
        self.surname = surname
        self.filtr = filtr
    
    ## Documentation for a method.
    #   @param self The object pointer.
    def __repr__(self):
        return "('%s','%s','%s')" % (self.name, self.surname, self.filtr)

###########################################
class College(DeclarativeBase):
    __tablename__ = 'college'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "('%s')" % (self.name)
    
###########################################
class Faculty(DeclarativeBase):
    __tablename__ = 'faculty'
    
    id = Column(Integer, primary_key=True)
    college_id = Column(Integer, ForeignKey('college.id'))
    name = Column(String)
    college = relation("College",  backref='faculty')
    
    def __init__(self, college_id,  name):
        self.college_id = college_id
        self.name = name
        
    def __repr__(self):
        return "('%s','%s')" % (self.college_id,  self.name)
    
###########################################
class Institute(DeclarativeBase):
    __tablename__ = 'institute'
    
    id = Column(Integer, primary_key=True)
    faculty_id = Column(String, ForeignKey('faculty.id'))
    name = Column(String)
    faculty = relation('Faculty',  backref='institute')
    
    def __init__(self, faculty_id,  name):
        self.faculty_id = faculty_id
        self.name = name
        
    def __repr__(self):
        return "('%s','%s')" % (self.faculty_id,  self.name)

###########################################
class Group(DeclarativeBase):
    __tablename__ = 'group'
    
    id = Column(Integer, primary_key=True)
    name = Column(String,  unique=True)
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return "('%s')" % (self.name)
    
###########################################
class ColPer(DeclarativeBase):
    """Tabela asocjacyjna tabel Person oraz College"""
    __tablename__ = 'colper'
    
    college_id = Column(Integer, ForeignKey('college.id'),  primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'),  primary_key=True)
    college = relation("College",  backref='colper')
    person = relation("Person",  backref='colper')
    
    def __init__(self, college_id,  person_id):
        self.college_id = college_id
        self.person_id = person_id
        
    def __rerp__(self):
        return "('%s','%s')" % (self.college_id,  self.person_id)
        
###########################################
class GroPer(DeclarativeBase):
    """Tabela asocjacyjna tabel Person oraz Group"""
    __tablename__ = 'groper'
    
    group_id = Column(Integer, ForeignKey('group.id'),  primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'),  primary_key=True)
    group = relation("Group",  backref='groper')
    person = relation("Person",  backref='groper')
    
    def __init__(self, group_id,  person_id):
        self.group_id = group_id
        self.person_id = person_id
        
    def __rerp__(self):
        return "('%i','%i')" % (self.group_id,  self.person_id)
    
###########################################
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
    journal = relation('Journal',  backref='publication')
    
    def __init__(self, title, author, citation, type, year, doi, ident, journal_id, urlpub, urlcit, root):
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
        
    def __repr__(self):
        return "('%s','%s','%i','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.title, self.author, self.citation, self.type, self.year, self.doi, self.ident, self.journal_id, self.urlpub, self.urlcit, self.root)
    
###########################################
class Journal(DeclarativeBase):
    __tablename__ = 'journal'
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    short_name = Column(String)
    address = Column(String)
    
    def __init__(self, full_name,  short_name,  address):
        self.full_name = full_name
        self.short_name = short_name
        self.address = address
        
    def __repr__(self):
        return "('%s','%s','%s')" % (self.full_name,  self.short_name,  self.address)

############################################
class Cite(DeclarativeBase):
    __tablename__ = 'cite'
    
    id = Column(Integer, primary_key=True)
    urlcit = Column(String)
    id_pub_m = Column(Integer)
    pub_ids = Column(Integer, ForeignKey('publication.id'))
    public = relation("Publication",  backref='cite')
    
    def __init__(self, urlcit, id_pub_m, pub_ids):
        self.urlcit = urlcit
        self.id_pub_m = id_pub_m
        self.pub_ids =pub_ids
        
    def __repr__(self):
        return "('%s','%s','%s')" % (self.urlcit,  self.id_pub_m, self.pub_ids)

###########################################
class PerPub(DeclarativeBase):
    __tablename__ = 'perpub'
    
    person_id = Column(Integer, ForeignKey('person.id'),  primary_key=True)
    pub_id = Column(Integer, ForeignKey('publication.id'),  primary_key=True)
    person = relation("Person",  backref='perpub')
    pub = relation("Publication",  backref='perpub')
    
    def __init__(self, person_id, pub_id):
        self.person_id = person_id
        self.pub_id = pub_id
    
    def __repr__(self):
        return "('%s','%s')" % (self.person_id, self.pub_id)

