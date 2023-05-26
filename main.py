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
        #self.theme_cls.primary_palette = "Pink"
        sm.add_widget(LoginApp(name='login'))
        sm.add_widget(HomeApp(name='home'))
        sm.add_widget(SignupApp(name='signup'))
        return sm
    
class NavTab(ToggleButtonBehavior, MDBoxLayout):
    text = StringProperty("")
    icon = StringProperty("")
    icon_active = StringProperty("")
    def __init__(self, **kw):
        super().__init__(**kw)

if __name__ == '__main__':
    MainApp().run()