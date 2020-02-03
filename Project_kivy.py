from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.button import Button
from functools import partial

class FirstKivy(App):
    def build(self):
        return Label(text ="                  [b][color=DC143C]Hello There\n\n[color=9370DB] Welcome to Benevolent Eye!", font_size='25', markup = True)
FirstKivy().run()

class KivyButton(App):
    def disable(self,instance,*args):
        instance.disabled=True
    def update(self,instance,*args):
        instance.text="Analyzing"
                
    def build(self):
         def on_press(self):
           self.source= KivyButton().run()
         button1(text="Click Here to get started!",pos=(300,350),size_hint=(.25,.18))
         button1.bind(on_press=partial(self.disable,button1))
         button1.bind(on_press=partial(self.update,button1))
         self.game = PivotGame()
         Clock.schedule_interval(self.game.update,1.0/30.0)
         Clock.schedule_interval(self.game.update_opponent,5.0)
         self._keyboard= Window.request_keyboard(self._keyboard_closed, self)
         self._keyboard.bind(on_key_down = self._on_keyboard_down)
         self._keyboard.bind(on_key_up = self._on_keyboard_up)

KivyButton().run()         
