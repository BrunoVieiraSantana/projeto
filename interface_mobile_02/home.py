from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
import matplotlib as mpl
from matplotlib import pyplot as plt
from garden_matplotlib import FigureCanvasKivyAgg

mpl.rc('text', color='#ffffff')
mpl.rc('axes', labelcolor='#ffffff')
mpl.rc('xtick', color='#ffffff')
mpl.rc('ytick', color='#ffffff')


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


class PlotWidgetPie(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(self.plot_pie()))
 
    def plot_pie(self):
        colors = ['#b4abd4', '#888fc3','#5679ad', '#ee9944', '#444466', '#bb5555']
        fig = plt.Figure(figsize=(5, 3), dpi=90)
        fig.patch.set_facecolor('#263238')
        ax = fig.add_subplot(111)
        list_category = ['Renda', 'Despesa', 'Saldo']
        list_values = [1200,750,450]

        explode = []
        for i in list_category:
            explode.append(0.05)
        ax.pie(list_values, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
        ax.legend(list_category, labelcolor='#263238', loc="center left", bbox_to_anchor=(0, 0))

        return fig
    

class PlotWidgetBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(self.plot_bar()))

    def plot_bar(self):
        colors = ['#b4abd4', '#888fc3','#5679ad', '#ee9944', '#444466', '#bb5555']
        list_category = ['Renda', 'Despesa', 'Saldo']
        list_values = [1200,750,450]
        

        fig = plt.Figure(figsize=(4, 3.45), dpi=60)
        fig.patch.set_facecolor('#263238')
        ax = fig.add_subplot(111)
        ax.bar(list_category, list_values,  color=colors, width=0.9)

        c = 0

        for i in ax.patches:
            ax.text(i.get_x()-.001, i.get_height()+.5,
                    str("{:,.0f}".format(list_values[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color='#ffffff')

            c += 1

        ax.set_xticklabels(list_category,fontsize=16)
        ax.patch.set_facecolor('#263238')
        ax.spines['bottom'].set_color('#ffffff')
        ax.spines['bottom'].set_linewidth(1)
        ax.spines['right'].set_linewidth(0)
        ax.spines['top'].set_linewidth(0)
        ax.spines['left'].set_color('#ffffff')
        ax.spines['left'].set_linewidth(1)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(False, color='#ffffff')
        ax.xaxis.grid(False)


        return fig
  
