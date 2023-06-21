from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

MDApp.get_running_app().KV_FILES.append("signup.kv")

class Signup(MDScreen):
    def build(self):
        pass

    def go_login(self):
        self.manager.current = 'login'
    
    def do_register(self, ):
        print('Registro')
        self.manager.current = 'login'

  
        




