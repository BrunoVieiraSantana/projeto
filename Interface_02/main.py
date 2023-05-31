from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import StringProperty
from login import LoginApp
from home import HomeApp
from signup import SignupApp

class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginApp(name='login'))
        sm.add_widget(HomeApp(name='home'))
        sm.add_widget(SignupApp(name='signup'))
        self.title='Gestão Financeira'
        self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Teal"
        #self.theme_cls.primary_palette = "Pink"
        #self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = '900'
        return sm


if __name__ == '__main__':
    MainApp().run()