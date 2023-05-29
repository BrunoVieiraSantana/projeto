from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_file('login.kv')

class LoginApp(MDScreen):
    def build(self):
        pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
     
    def go_home(self):
        self.manager.current = 'home'

    def go_signup(self):
        self.manager.current = 'signup'

