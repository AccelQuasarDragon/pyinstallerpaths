from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import sys
import pathlib
import os

# https://kivy.org/doc/stable/guide/lang.html#special-syntax
kvstring = '''
#:import os os
#:import sys sys
NewBox:
    orientation: 'vertical'
    Label:
        text: "os.getcwd(): " + str(os.getcwd())
    Label:
        text: "sys.executable: " + str(sys.executable)
    Label:
        text: "sys.path: " + str(sys.path)
        text_size: self.width, None
    Label:
        text: root.meipasstest()
    Label:
        # text: root.findfile()
        # text_size: self.width, None
'''

class NewBox(BoxLayout):
    def meipasstest(*args):
        if hasattr(sys, "_MEIPASS"):
            return "sys._MEIPASS: " + str(sys._MEIPASS)
        else:
            return "no _MEIPASS found, you are running from ide"
    def findfile(*args):
        solution = []
        if hasattr(sys, "_MEIPASS"):
            possiblepaths = sys.path+[os.getcwd(), sys._MEIPASS]
        else:
            possiblepaths = sys.path+[os.getcwd()]
        for pathstr in possiblepaths:
            tempsol = list(pathlib.Path(pathstr).rglob(os.path.join("findthis.py")))
            solution += tempsol
            if len(tempsol) > 0:
                print("found ", solution, "in ", pathstr)
                #reminder that os.getcwd is in path on windows
        return str(solution)

class BasicApp(App):
    def build(self):
        if hasattr(sys, "_MEIPASS"):
            self.title = "RUNNING FROM PYINSTALLER"
        else:
            self.title = "RUNNING FROM TERMINAL"
        return Builder.load_string(kvstring)
    def on_request_close(self):
        pass
  
BasicApp().run()
BasicApp().on_request_close()