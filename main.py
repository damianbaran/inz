import wx
from src.modules.controler import Controler


class Main:
    def __init__(self, app): 
        self.controler = Controler() 

if __name__ == "__main__":
    app = wx.App(False)
    controller = Main(app)
    app.MainLoop()
