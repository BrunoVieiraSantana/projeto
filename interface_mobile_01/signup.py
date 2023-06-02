from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_file('signup.kv')

class SignupApp(MDScreen):
    def build(self):
        pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
  
        
    def go_login(self):
        self.manager.current = 'login'



