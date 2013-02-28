#from distutils.core import setup
#import py2exe

#setup(
#  windows=[{"script" : "frames.py"}],
#  options={"py2exe" : {
#    "includes": ["sip", "PyQt4.QtSql"],
#    "packages": ["sqlalchemy.databases.sqlite"]
#}})

from frames import MainFrame

import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.make_reference()

world = MainFrame()
#bob = Turtle(world)

lumpy.object_diagram()
lumpy.class_diagram()
