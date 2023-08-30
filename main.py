import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import sys
import pathlib
import os

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
        text: root.findfile()
        text_size: self.width, None
'''

class NewBox(BoxLayout):
    def meipasstest(*args):
        if hasattr(sys, "_MEIPASS"):
            return "sys._MEIPASS: " + str(sys._MEIPASS)
        else:
            return "no _MEIPASS found"
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
        return str(solution)


# Defining a class
class MyFirstKivyApp(App):
      
    # Function that returns 
    # the root widget
    def build(self):
          
        # Label with text Hello World is 
        # returned as root widget
        return Builder.load_string(kvstring)
  
  
# Here our class is initialized
# and its run() method is called. 
# This initializes and starts 
# our Kivy application.
MyFirstKivyApp().run()
MyFirstKivyApp().on_request_close()