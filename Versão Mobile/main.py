from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from login import Login
from home import Home
from signup import Signup



class Main(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name='login'))
        sm.add_widget(Home(name='home'))
        sm.add_widget(Signup(name='signup', id='signuppage'))
        self.title='Gestão Financeira'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = '900'
        return sm

if __name__ == '__main__':
    Main().run()