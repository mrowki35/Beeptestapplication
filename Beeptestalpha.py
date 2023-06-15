import kivy
from kivy.app import App
from kivy.lang import Builder
from pathlib import Path

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

from kivy.uix.label import Label
from kivy.clock import Clock
import time 

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.togglebutton import ToggleButton




class CustomWidget(ToggleButton):
    def __init__(self, **kwargs):
        super(CustomWidget, self).__init__(**kwargs)
        self.current_state = 'START'
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.4}
        self.size_hint = (0.5, 0.25)
        self.update_button_state()
        self.font_size = 24 
        self.bold = True  
        self.italic = True
        #self.color = (0,0,160,1)

    def update_button_state(self):
        self.text = self.current_state
        if self.current_state == 'START':
            self.background_color = (0, 1, 0, 0.5)  # Zielony kolor tła
            self.on_release = self.stop_button_function
        else:
            self.background_color = (1, 0, 0, 0.5)  # Czerwony kolor tła
            self.on_release = self.start_button_function

    def on_state(self, widget, value):
        if value == 'down':
            self.current_state = 'STOP'
        else:
            self.current_state = 'START'
        self.update_button_state()

    def stop_button_function(self):
        # Funkcja do wykonania po kliknięciu przycisku w stanie 'Stop'
        self.parent.stop()
        

    def start_button_function(self):
        # Funkcja do wykonania po kliknięciu przycisku w stanie Start
        self.parent.start()



class WindowManager(ScreenManager):
  pass

class FirstWindow(Screen):
  def __init__(self, **kwargs):
    super(FirstWindow, self).__init__(**kwargs)
    self.count = 0  # zmienna licznikowa
    self.level_count=1
    self.change=1 #to make the correct stage count
    self.custom_widget = CustomWidget()
    self.add_widget(self.custom_widget)

  def run_level(self,running_level ,next_level_func, countdown, iteration_time):
    timer = float(self.ids.timer_label.text)
    if timer <= 0:
      Clock.unschedule(running_level)
      self.count += 1
      if self.count < countdown:
        self.ids.stage_counting_label.text = str(countdown - self.count)
        self.ids.timer_label.text = str(iteration_time)
        Clock.schedule_interval(running_level, 0.01)
      else:
        if next_level_func==self.finished:
          return
        else:
          self.level_count += 1
          self.ids.level_counting_label.text = str(self.level_count)
          self.count = 0
          Clock.schedule_once(next_level_func, 0.01)

    else:
      self.ids.timer_label.text = "{:.2f}".format(timer - 0.01)
      
    
  def firstlevel(self, dt):
    self.run_level(self.firstlevel,self.secondlevel, 7, 9)
    
  def secondlevel(self, dt):
    self.run_level(self.secondlevel,self.thirdlevel, 8+self.change, 8)
    
  def thirdlevel(self, dt):
    self.run_level(self.thirdlevel,self.fourthlevel, 8+self.change, 7.58)

  def fourthlevel(self, dt):
    self.run_level(self.fourthlevel,self.fifthlevel, 9+self.change, 7.2)

  def fifthlevel(self, dt):
    self.run_level(self.fifthlevel,self.sixthlevel, 9+self.change, 6.86)

  def sixthlevel(self, dt):
    self.run_level(self.sixthlevel,self.seventhlevel, 10+self.change, 6.55)

  def seventhlevel(self, dt):
    self.run_level(self.seventhlevel,self.eighthlevel, 10+self.change, 6.26)
    
  def eighthlevel(self, dt):
    self.run_level(self.eighthlevel,self.ninthlevel, 11+self.change, 6)

  def ninthlevel(self, dt):
    self.run_level(self.ninthlevel,self.tenthlevel, 11+self.change, 5.76)

  def tenthlevel(self, dt):
    self.run_level(self.tenthlevel,self.eleventhlevel, 11+self.change, 5.54)

  def eleventhlevel(self, dt):
    self.run_level(self.eleventhlevel,self.twelfthlevel, 12+self.change, 5.33)

  def twelfthlevel(self, dt):
    self.run_level(self.twelfthlevel,self.thirteenthlevel, 12+self.change, 5.14)

  def thirteenthlevel(self, dt):
    self.run_level(self.thirteenthlevel,self.fourthteenthlevel, 13+self.change, 4.97)

  def fourthteenthlevel(self, dt):
    self.run_level(self.fourthteenthlevel,self.fifteenthlevel, 13+self.change, 4.8)

  def fifteenthlevel(self, dt):
    self.run_level(self.fifteenthlevel,self.sixteenthlevel, 13+self.change, 4.65)

  def sixteenthlevel(self, dt):
    self.run_level(self.sixteenthlevel,self.seventeenthlevel, 14+self.change, 4.5)

  def seventeenthlevel(self, dt):
    self.run_level(self.seventeenthlevel,self.eighteenthlevel, 14+self.change, 4.36)

  def eighteenthlevel(self, dt):
    self.run_level(self.eighteenthlevel,self.nineteenthlevel, 15+self.change, 4.24)

  def nineteenthlevel(self, dt):
    self.run_level(self.nineteenthlevel,self.twentiethlevel, 15+self.change, 4.11)

  def twentiethlevel(self, dt):
    self.run_level(self.twentiethlevel,self.twentyfirstlevel, 16+self.change, 4)

  def twentyfirstlevel(self, dt):
    self.run_level(self.twentyfirstlevel,self.finished, 16+self.change, 3.89)
  def finished(self):
    return


  def start(self):
    if self.level_count==1:
      Clock.schedule_interval(self.firstlevel,0.01)
    elif self.level_count==2:
      Clock.schedule_interval(self.secondlevel,0.01)
    elif self.level_count==3:
      Clock.schedule_interval(self.thirdlevel,0.01)
    elif self.level_count==4:
      Clock.schedule_interval(self.fourthlevel,0.01)
    elif self.level_count==5:
      Clock.schedule_interval(self.fifthlevel,0.01)
    elif self.level_count==6:
      Clock.schedule_interval(self.sixthlevel,0.01)
    elif self.level_count==7:
      Clock.schedule_interval(self.seventhlevel,0.01)
    elif self.level_count==8:
      Clock.schedule_interval(self.eighthlevel,0.01)
    elif self.level_count==9:
      Clock.schedule_interval(self.ninthlevel,0.01)
    elif self.level_count==10:
      Clock.schedule_interval(self.tenthlevel,0.01)
    elif self.level_count==11:
      Clock.schedule_interval(self.eleventhlevel,0.01)
    elif self.level_count==12:
      Clock.schedule_interval(self.twelfthlevel,0.01)
    elif self.level_count==13:
      Clock.schedule_interval(self.thirteenthlevel,0.01)
    elif self.level_count==14:
      Clock.schedule_interval(self.fourthteenthlevel,0.01)
    elif self.level_count==15:
      Clock.schedule_interval(self.fifteenthlevel,0.01)
    elif self.level_count==16:
      Clock.schedule_interval(self.sixteenthlevel,0.01)
    elif self.level_count==17:
      Clock.schedule_interval(self.seventeenthlevel,0.01)
    elif self.level_count==18:
      Clock.schedule_interval(self.eighteenthlevel,0.01)
    elif self.level_count==19:
      Clock.schedule_interval(self.nineteenthlevel,0.01)
    elif self.level_count==20:
      Clock.schedule_interval(self.twentiethlevel,0.01)
    elif self.level_count==21:
      Clock.schedule_interval(self.twentyfirstlevel,0.01)

  def stop(self):
    if self.level_count==1:
      Clock.unschedule(self.firstlevel)
    elif self.level_count==2:
      Clock.unschedule(self.secondlevel)
    elif self.level_count==3:
      Clock.unschedule(self.thirdlevel)
    elif self.level_count==4:
      Clock.unschedule(self.fourthlevel)
    elif self.level_count==5:
      Clock.unschedule(self.fifthlevel)
    elif self.level_count==6:
      Clock.unschedule(self.sixthlevel)
    elif self.level_count==7:
      Clock.unschedule(self.seventhlevel)
    elif self.level_count==8:
      Clock.unschedule(self.eighthlevel)
    elif self.level_count==9:
      Clock.unschedule(self.ninthlevel)
    elif self.level_count==10:
      Clock.unschedule(self.tenthlevel)
    elif self.level_count==11:
      Clock.unschedule(self.eleventhlevel)
    elif self.level_count==12:
      Clock.unschedule(self.twelfthlevel)
    elif self.level_count==13:
      Clock.unschedule(self.thirteenthlevel)
    elif self.level_count==14:
      Clock.unschedule(self.fourthteenthlevel)
    elif self.level_count==15:
      Clock.unschedule(self.fifteenthlevel)
    elif self.level_count==16:
      Clock.unschedule(self.sixteenthlevel)
    elif self.level_count==17:
      Clock.unschedule(self.seventeenthlevel)
    elif self.level_count==18:
      Clock.unschedule(self.eighteenthlevel)
    elif self.level_count==19:
      Clock.unschedule(self.nineteenthlevel)
    elif self.level_count==20:
      Clock.unschedule(self.twentiethlevel)
    elif self.level_count==21:
      Clock.unschedule(self.twentyfirstlevel)

#class SecondWindow(Screen):
 # def __init__(self, **kwargs):
  #  super(SecondWindow, self).__init__(**kwargs)



kv = Builder.load_file('Beeptestalpha.kv')

class BeeptestalphaApp(App):
    def build(self):
      return kv

if __name__=='__main__':
     BeeptestalphaApp().run()
