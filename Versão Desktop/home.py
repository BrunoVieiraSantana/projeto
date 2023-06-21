from kivymd.uix.screen import MDScreen

from kivymd.app import MDApp

MDApp.get_running_app().KV_FILES.append("home.kv")

class Home(MDScreen):
    def build(self):
        pass

    def go_home(self):
        self.manager.current = 'home'

    def go_login(self):
        self.manager.current = 'login'
        print('Deslogando...')




