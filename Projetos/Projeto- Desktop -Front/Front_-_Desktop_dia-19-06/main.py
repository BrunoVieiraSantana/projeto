from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.tools.hotreload.app import MDApp


class SM(ScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}


class MainApp(MDApp):
    DEBUG = True
    sm = None
    state = {}

    def build_app(self, first=False):
        self.title='Gestão Financeira'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        if self.sm is None:
            self.state = {'current': 'login',
                          'login': 'data login',
                          'home': 'data home',
                          'signup': 'data signup',
                          'dashboard': 'data dashboard'
                          }
        else:
            self.state = {'current': self.sm.current,
                          'login': self.sm.get_screen('login').ids.data.text,
                          'home': self.sm.get_screen('home').ids.data.text,
                          'signup': self.sm.get_screen('signup').ids.data.text,
                          'dashboard': self.sm.get_screen('dashboard').ids.data.text}

        KV_FILES = []
        self.sm = SM()
        CLASSES = self.sm.get_classes()

        return self.sm

    def apply_state(self, state):
        self.sm.current = state['current']
        self.sm.get_screen('login').ids.data.text = state['login']
        self.sm.get_screen('home').ids.data.text = state['home']
        self.sm.get_screen('signup').ids.data.text = state['signup']
        self.sm.get_screen('dashboard').ids.data.text = state['dashboard']


if __name__ == '__main__':
    app = MainApp()
    app.run()

