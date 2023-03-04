from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen




class WindowManager(ScreenManager):
    pass

class Main_Screen(Screen):
    pass


kv=Builder.load_file("beeptest.kv")

class BeeptestApp(App):
        
    def build(self):
        return kv

if __name__=='__main__':
    BeeptestApp().run()



sth = ("""Carousel:
        loop: True
        canvas.before:
            Color:
                rgba: (218/264, 223/264, 225/264, 0)
            Rectangle:
                pos: self.pos
                size: self.size

        FloatLayout:
            id: middle
            Label:
                id: Timecounter
                pos_hint: {"center_x":0.5,"center_y":0.2}
                size_hint: (0.2,0.3)
                text: "Hello World"
            Label:
                id: Levelcounter
                pos_hint: {"center_x":0.5,"center_y":0.4}
                size_hint: (0.2,0.3)
            
            Button:
                text: "Start"
                size_hint: (0.4,0.2)
                pos_hint: {"center_x":0.5,"center_y":0.7}
                on_press: root.on_press()
        FloatLayout:
            id: right
            Label:
                text: "Your best result"
        FloatLayout:
            id : left
            Label:
                text: "Last results"   """)
