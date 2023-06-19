from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

from kivymd.uix.boxlayout import MDBoxLayout
import matplotlib as mpl
from matplotlib import pyplot as plt
from garden_matplotlib import FigureCanvasKivyAgg



from kivy.metrics import dp

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.datatables import MDDataTable


MDApp.get_running_app().KV_FILES.append("dashboard.kv")

mpl.rc('text', color='#ffffff')
mpl.rc('axes', labelcolor='#ffffff')
mpl.rc('xtick', color='#ffffff')
mpl.rc('ytick', color='#ffffff')
#fundo - #455a64
Tipo=None
Pressed=[]
fixos=1
Rvalues=[]
class Dashboard(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Dbtype='Lucro'
        self.Fixo='DESP.'
        self.mesAtual=[1]
    def build(self):
        pass

    def go_login(self, instance, mês):
        global Meses
        if instance in Meses:
            instance.md_bg_color= '#485c64'
            Meses.remove(instance)
            print('True')
            if mês in self.mesAtual:
                self.mesAtual.remove(mês)
                self.mesAtual.append(1)
        else:
            if len(Meses)<2:
                instance.md_bg_color='#221424'
                Meses.append(instance)
                if mês not in self.mesAtual:
                    self.mesAtual.append(mês)
                print('Menor q 2')
            else:
                instance.md_bg_color='#221424'
                for mes in Meses:
                    mes.md_bg_color='#485c64'
                Meses=[instance]
                self.mesAtual.clear()
                self.mesAtual.append(mês)
                print('Maior q 2')
        if len(Meses)==2:
            self.Fixo='FIXO'
        else:
            self.Fixo='DESP.'
        print(self.Fixo,'Self Fixo ------------------------')
        print(self.mesAtual,'AAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    def type(self, instance, tipo):
        global Tipo,Pressed
        instance.md_bg_color='#221424'
        Tipo=tipo
        if instance in Pressed:
            instance.md_bg_color='#121212'
            Pressed.clear()
        elif len(Pressed)==1 and instance not in Pressed:
            Pressed[0].md_bg_color='#121212'
            Pressed.clear()
        Pressed.append(instance)
        self.Dbtype=Tipo
        # print(Pressed,'---------Pressionado-----')

    def teste(self, instance):
        print(instance)
    
    def newValues(self, instance, valores, media=None):
        print(valores,'-------')
        if media==None:
            media=1
        valores=float(valores)/media
        print(valores,'---====----')
        instance.text=f'{valores:.2f} R$'
        print(media)
    def verificação(self, instance):
        pass

class LucroLine(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.value=self.value
        except:
            self.value=[0,0,0,0,0,0,0,0,0,0,0,0]
        self.add_widget(FigureCanvasKivyAgg(self.plot_line()))

    def plot_line(self):
        fig = plt.figure(figsize=(5, 3), dpi=90)
        fig.patch.set_facecolor('#455a64')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#455a64')
        days_of_week= ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul','Ago', 'Set', 'Out', 'Nov', 'Dez']

        
        weekly_expenses = self.value  # Exemplo de valores de gastos
        ax.plot(days_of_week, weekly_expenses, color='#b4abd4', marker='o', linewidth=2)
        ax.set_xlabel('Meses', color='white')
        ax.set_ylabel('Lucro', color='white')
        ax.set_title('Lucro Mensal', color='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(colors='white')

        return fig
    def add(self, mesAtual, valor):
        mesAtual=max(mesAtual)-1
        self.value[mesAtual]=int(valor.text)
        self.clear_widgets()
        self.__init__()

class GastoLine(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.value=self.value
        except:
            self.value=[0,0,0,0,0,0,0,0,0,0,0,0]
        self.add_widget(FigureCanvasKivyAgg(self.plot_line()))

    def plot_line(self):
        fig = plt.figure(figsize=(5, 3), dpi=90)
        fig.patch.set_facecolor('#455a64')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#455a64')
        days_of_week= ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul','Ago', 'Set', 'Out', 'Nov', 'Dez']

        
        weekly_expenses = self.value  # Exemplo de valores de gastos
        ax.plot(days_of_week, weekly_expenses, color='#b4abd4', marker='o', linewidth=2)
        ax.set_xlabel('Meses', color='white')
        ax.set_ylabel('Gastos', color='white')
        ax.set_title('Gastos Mensal', color='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(colors='white')

        return fig
    def add(self, mesAtual, valor):
        mesAtual=max(mesAtual)-1
        self.value[mesAtual]=int(valor.text)
        self.clear_widgets()
        self.__init__()

class GastoMedio(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global Rvalues
        try:
            self.list=self.list
            self.value=self.value
            self.media=self.media
        except:
            self.list=['Aluguel', 'Comida', 'Conforto', 'Compras']
            self.value= [600,300,250,100]
            self.media=1
        self.gastoVal=f'{(sum(self.value)):.2f}'
        self.texto= self.gastoVal+" R$"
        if len(Rvalues)==1:
            Rvalues.append(sum(self.value))
        self.add_widget(FigureCanvasKivyAgg(self.plot_bar()))

    def plot_bar(self):
        colors = ['#b4abd4', '#ec5020','#d82424', '#f04820', '#d84c3c', '#bb5555']
        list_category = self.list
        list_values = self.value
        

        fig = plt.Figure(figsize=(4, 3.45), dpi=60)
        fig.patch.set_facecolor('#455a64')
        ax = fig.add_subplot(111)
        ax.bar(list_category, list_values,  color=colors, width=0.9)

        c = 0

        for i in ax.patches:
            ax.text(i.get_x()-.001, i.get_height()+.5,
                    str("{:,.0f}".format(list_values[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color='#ffffff')

            c += 1

        ax.set_xticklabels(list_category,fontsize=16)
        ax.patch.set_facecolor('#455a64')
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
    def add(self, fixo, valor, nome):
        print("gasto")
        self.list.append(nome.text)
        self.value.append(int(valor.text))
        self.clear_widgets()
        self.__init__()
        if fixo=="FIXO":
            self.media+=1

# mpl.rc('text', color='#ffffff')
# mpl.rc('axes', labelcolor='#ffffff')
# mpl.rc('xtick', color='#ffffff')
# mpl.rc('ytick', color='#ffffff')
#fundo - #455a64
class PieLucro(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.list=self.list
            self.value
            self.media=self.media
        except:
            self.list= ['Renda', 'Despesa', 'Saldo']
            self.value= [1200,750,450]
            self.media=1
        self.add_widget(FigureCanvasKivyAgg(self.plot_pie()))
        
 
    def plot_pie(self):
        colors = ['#b4abd4', '#888fc3','#5679ad', '#ee9944', '#444466', '#bb5555']
        fig = plt.Figure(figsize=(5, 3), dpi=90)
        fig.patch.set_facecolor('#455a64')
        ax = fig.add_subplot(111)
        list_category = self.list
        list_values = self .value

        explode = []
        for i in list_category:
            explode.append(0.05)
        ax.pie(list_values, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
        ax.legend(list_category, labelcolor='#455a64', loc="center left", bbox_to_anchor=(0, 0))

        return fig
    
    def add(self, fixo, valor, text):
        print('Pie ---------------------------')
        print('lucro')
        self.list.append(text.text)
        self.value.append(int(valor.text))
        self.clear_widgets()
        self.__init__()
        if fixo=="FIXO":
            self.media+=1

class PieGasto(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.list=self.list
            self.value
            self.media=self.media
        except:
            self.list= ['Renda', 'Despesa', 'Saldo']
            self.value= [1200,750,450]
            self.media=1
        self.add_widget(FigureCanvasKivyAgg(self.plot_pie()))
        
 
    def plot_pie(self):
        colors = ['#b4abd4', '#888fc3','#5679ad', '#ee9944', '#444466', '#bb5555']
        fig = plt.Figure(figsize=(5, 3), dpi=90)
        fig.patch.set_facecolor('#455a64')
        ax = fig.add_subplot(111)
        list_category = self.list
        list_values = self .value

        explode = []
        for i in list_category:
            explode.append(0.05)
        ax.pie(list_values, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
        ax.legend(list_category, labelcolor='#455a64', loc="center left", bbox_to_anchor=(0, 0))

        return fig
    
    def add(self, fixo, valor, texto):
        print('Pie ---------------------------')
        print('lucro')
        self.list.append(texto.text)
        self.value.append(int(valor.text))
        self.clear_widgets()
        self.__init__()
        if fixo=="FIXO":
            self.media+=1


class LucroMedio(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global Rvalues
        try:
            self.value=self.value
            self.list=self.list
            self.media=self.media
        except:
            self.value= [1600,100,350]
            self.list=['Salario', 'Vendas', 'Corrente']
            self.media=1
        self.medVal=f'{sum(self.value):.2f}'
        self.texto=self.medVal+' R$'
        if Rvalues ==[]:
            Rvalues.append(sum(self.value))
        
        self.add_widget(FigureCanvasKivyAgg(self.plot_bar()))

    def plot_bar(self):
        colors = ['#b4abd4', '#888fc3','#5679ad', '#ee9944', '#444466', '#bb5555']
        list_category = self.list
        list_values = self.value
        

        fig = plt.Figure(figsize=(4, 3.45), dpi=60)
        fig.patch.set_facecolor('#455a64')
        ax = fig.add_subplot(111)
        ax.bar(list_category, list_values,  color=colors, width=0.9)

        c = 0

        for i in ax.patches:
            ax.text(i.get_x()-.001, i.get_height()+.5,
                    str("{:,.0f}".format(list_values[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color='#ffffff')

            c += 1

        ax.set_xticklabels(list_category,fontsize=16)
        ax.patch.set_facecolor('#455a64')
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
        print(list_category,list_values)
        return fig

    def add(self, fixo, valor, nome):
        print('lucro')
        self.list.append(nome.text)
        self.value.append(int(valor.text))
        self.clear_widgets()
        self.__init__()
        if fixo=="FIXO":
            self.media+=1
        
# class PlotWidgetLine(MDBoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.add_widget(FigureCanvasKivyAgg(self.plot_line()))

#     def plot_line(self):
#         fig = plt.figure(figsize=(5, 3), dpi=90)
#         fig.patch.set_facecolor('#455a64')
#         ax = fig.add_subplot(111)
#         ax.set_facecolor('#455a64')
        
#         days_of_week = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
#         weekly_expenses = [50, 30, 40, 20, 55, 10, 15]  # Exemplo de valores de gastos
        
#         ax.plot(days_of_week, weekly_expenses, color='#b4abd4', marker='o', linewidth=2)
#         ax.set_xlabel('Dias da semana', color='white')
#         ax.set_ylabel('Gastos', color='white')
#         ax.set_title('Gasto Mensal', color='white')
#         ax.spines['bottom'].set_color('white')
#         ax.spines['left'].set_color('white')
#         ax.tick_params(colors='white')

#         return fig




# ----------------------------------------------Secundaria -----------------------------------------------

data=["ESPERA", "PAGO"]

Meses=[]
newTabel={}
class Table(MDBoxLayout):
    data_tables = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_()
        try:
            self.media=self.media
        except:
            self.media=1

    def build_(self):
        global data
        #app.theme_cls.primary_dark
        self.status = data
        self.data_tables = MDDataTable(
            # background_color=(0, 1, 0, .3),
            # background_color="white",
            # background_color_cell = "red",
            # background_color_header = "blue",
            # background_color_selected_cell = "green",
            check=True,
            elevation =0,
            size_hint=(1, 1),
            pos_hint={"top": 1,"center_x":0.1},
            use_pagination=False,
            column_data=[
                ("[size=11]NOME[/size]", dp(19)),
                ("[size=11]VAL.[/size]", dp(7)), #sobra 2
                ("[size=11]DATA[/size]", dp(9)),
                ("[size=11]TIPO[/size]", dp(8)),
                ("[size=11]STATUS[/size]", dp(10))


            ],
            row_data=[["[size=11]ALUG.[/size]", "[size=11]350[/size]", "[size=11]04/06[/size]", "[size=11]FIXA[/size]", f"[size=11]{'ESPERA'}[/size]"]],
        )
        self.data_tables.bind(on_check_press=self.update_table)
        self.add_widget(self.data_tables)

    def update_table(self, instance_table, current_row):
        index = self.data_tables.row_data.index(current_row)
        if current_row[4] == f"[size=12]{self.status[1]}[/size]":
            current_row[4] = f"[size=12]{self.status[0]}[/size]"
        else:
            current_row[4] = f"[size=12]{self.status[1]}[/size]"
        self.data_tables.row_data[index] = current_row

    def sort_by_type(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][1][0]
            )
        )

    def sort_by_value(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][2]
            )
        )
    def on_enter(self, instance, local, all=None, Fixo=None):
        global newTabel
        verify=True
        newTabel[local]=instance.text
        for item in all.keys():
            newTabel[item]=all[item].text

        if len(newTabel)==4:
            print(newTabel,'passo1')
            for new in newTabel.values():
                if new=='':
                    verify=False
                    print(newTabel, 'Quebra')
                    break
            if verify:
                self.data_tables.row_data.append([f"[size=11]{newTabel['Nome']}[/size]", f"[size=11]{newTabel['Valor']}[/size]", f"[size=11]{newTabel['Data']}[/size]", f"[size=11]{Fixo}[/size]", f"[size=11]{self.status[0]}[/size]"])
                print(newTabel, 'passo 3')
                print(f'{Fixo}-nnnn--')
                print('Antigo Fixo')
                if Fixo=='FIXO':
                    self.media+=1
                    self.media
                    print('Novo Fixo', 'mmmmm')
    
    def update_row_data(self, instance_button):
        self.data_tables.row_data = [('1','1','1','1')]
        print(self.data_tables.row_data)

    def add_row_data(self, Nome, Valor, Data, Tipo):
        self.data_tables.row_data.append([f"[size=11]{Nome}[/size]", f"[size=11]{Valor}[/size]", f"[size=11]{Data}[/size]", f"[size=11]{Tipo}.[/size]", f"[size=11]Espera[/size]"])
        print(self.data_tables.row_data)
        return self.data_tables.row_data

class Receita(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if len(Rvalues)==2:
            Rvalues.append((Rvalues[0]-Rvalues[1]))
        try:
            self.value=self.value
            self.list=self.list
        except:
            self.value= Rvalues
            self.list=['Renda', 'Despesa','Saldo']
        self.porcent=int((self.value[1]*100)/self.value[0])
        self.ptext=f"{self.porcent}%"
        self.add_widget(FigureCanvasKivyAgg(self.plot_bar()))

    def plot_bar(self):
        colors = ['#b4abd4', '#888fc3','#5679ad', '#ee9944', '#444466', '#bb5555']
        list_category = self.list
        list_values = self.value
        

        fig = plt.Figure(figsize=(4, 3.45), dpi=60)
        fig.patch.set_facecolor('#455a64')
        ax = fig.add_subplot(111)
        ax.bar(list_category, list_values,  color=colors, width=0.9)

        c = 0

        for i in ax.patches:
            ax.text(i.get_x()-.001, i.get_height()+.5,
                    str("{:,.0f}".format(list_values[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color='#ffffff')

            c += 1

        ax.set_xticklabels(list_category,fontsize=16)
        ax.patch.set_facecolor('#455a64')
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
    def add(self, tipo, valor, progressbar, textbar):
        print('lucro')
        if tipo=='Lucro':
            Rvalues[0]+=int(valor.text)
        elif tipo=='Gasto':
            Rvalues[1]+=int(valor.text)
        Rvalues[2]=Rvalues[0]-Rvalues[1]
        print('')
        progressbar.value=int((self.value[1]*100)/self.value[0])
        textbar.text=f'{progressbar.value}%'
        self.clear_widgets()
        self.__init__()


            

class PlotWidgetLine(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.value=self.value
        except:
            self.value=[0,0,0,0]
        self.add_widget(FigureCanvasKivyAgg(self.plot_line()))

    def plot_line(self):
        fig = plt.figure(figsize=(5, 3), dpi=90)
        fig.patch.set_facecolor('#455a64')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#455a64')
        days_of_week= ['1°Sem', '2°Sem', '3°Sem', '4°Sem']

        
        weekly_expenses = self.value  # Exemplo de valores de gastos
        ax.plot(days_of_week, weekly_expenses, color='#b4abd4', marker='o', linewidth=2)
        ax.set_xlabel('Semanas do Mês', color='white')
        ax.set_ylabel('Gastos', color='white')
        ax.set_title('Gastos Semanais', color='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(colors='white')

        return fig
    def add(self):
        self.value
        self.value.append(45)
        self.clear_widgets()
        self.__init__()