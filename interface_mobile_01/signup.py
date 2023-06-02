from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button.button import MDFillRoundFlatButton



class SignupApp(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = MDScreen()

        self.label = MDLabel(
            text='Cadastro de Novo Usuário',
            pos_hint={"center_x": .88, "center_y": .8})

        self.nome = MDTextField(
            hint_text="Nome Completo",
            halign="center",
            size_hint = (0.50, .3),
            pos_hint = {"center_x": 0.5, "center_y":0.67},
            font_size = 10)
        
        self.email = MDTextField(
            hint_text="E-mail",
            halign="center",
            size_hint = (0.50, .3),
            pos_hint = {"center_x": 0.5, "center_y":0.57},
            font_size = 10)

        self.senha = MDTextField(
            hint_text = "Senha",
            halign="center",
            size_hint = (0.50, .3),
            pos_hint = {"center_x": 0.5, "center_y":0.47},
            font_size = 10,
            password= True)

        self.senhaRepetir = MDTextField(
            hint_text = "Repita a Senha",
            halign="center",
            size_hint = (0.50, .3),
            pos_hint = {"center_x": 0.5, "center_y":0.37},
            font_size = 10,
            password= True)

        self.button_01 = MDFillRoundFlatButton(
            text='    Salvar    ',
            pos_hint={"center_x": .5, "center_y": .3},
            on_press=self.save)
        
        self.button_02 = MDTextButton(
            text='Voltar para Tela de Login',
            pos_hint={"center_x": .5, "center_y": .06})
        self.button_02.bind(on_press=self.go_login)

        self.layout.add_widget(self.nome)
        self.layout.add_widget(self.email)
        self.layout.add_widget(self.senha)
        self.layout.add_widget(self.senhaRepetir)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button_01)
        self.layout.add_widget(self.button_02)


        self.add_widget(self.layout)
        

    def save(self, instance):
        nome = self.nome.text
        email = self.email.text
        senha = self.senha.text
        novo = {"nome": nome, "e-mail": email, "senha": senha}
        self.label.text = ("Cadastro realizado com sucesso")

    def go_login(self, instance):
        self.manager.current = 'login'



