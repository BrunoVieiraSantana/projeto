from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import FakeRectangularElevationBehavior 
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from garden_matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib import pyplot as plt




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

class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class PlotWidgetPie(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(self.plot_pie()))
 
    def plot_pie(self):
        colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']
        fig = plt.Figure(figsize=(5, 3), dpi=90)
        ax = fig.add_subplot(111)
        list_values = [1200,750,450]
        list_category = ['Renda', 'Despesa', 'Saldo']

        explode = []
        for i in list_category:
            explode.append(0.05)
        ax.pie(list_values, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
        ax.legend(list_category, loc="center right", bbox_to_anchor=(1.55, 0.50))

        return fig
