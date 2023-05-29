from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder


Builder.load_file('dashboard.kv')
class DashboardApp(MDBoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

