from distutils.core import setup
import py2exe

setup(
  windows=[{"script" : "frames.py"}],
  options={"py2exe" : {
    "includes": ["sip", "PyQt4.QtSql"],
    "packages": ["sqlalchemy.databases.sqlite"]
}})
