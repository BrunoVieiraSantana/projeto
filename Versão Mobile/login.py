import sqlite3
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('login.kv')

class Login(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conn = sqlite3.connect('database.db')  
        self.cursor = self.conn.cursor()

    def go_home(self):
        self.manager.current = 'home'

    def go_signup(self):
        self.manager.current = 'signup'

    def login(self):
        username = self.ids.data.text
        password = self.ids.log_password_text_field.text

        self.cursor.execute("SELECT * FROM usuarios WHERE nome=? AND senha=?", (username, password))
        user = self.cursor.fetchone()

        if user:
            self.go_home()
        else:
            print("Credenciais inválidas")

    def on_leave(self):
        pass
        # self.conn.close()  

class LoginApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    LoginApp().run()
