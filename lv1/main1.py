import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import sys



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
'''

class NewBox(BoxLayout):
    def meipasstest(*args):
        if hasattr(sys, "_MEIPASS"):
            return "sys._MEIPASS: " + str(sys._MEIPASS)
        else:
            return "no _MEIPASS found"

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