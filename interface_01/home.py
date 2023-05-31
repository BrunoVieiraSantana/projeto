from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


Builder.load_file('home.kv')

class HomeApp(MDScreen):
    def build(self):
        pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
     
    def go_home(self):
        self.manager.current = 'home'

    def go_login(self):
        self.manager.current = 'login'
        print('Deslogando...')

