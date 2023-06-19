from kivymd.uix.screen import MDScreen

from kivymd.app import MDApp

MDApp.get_running_app().KV_FILES.append("login.kv")

class Login(MDScreen):
    def build(self):
        pass

    def go_home(self):
        self.manager.current = 'home'

    def go_signup(self):
        self.manager.current = 'signup'



