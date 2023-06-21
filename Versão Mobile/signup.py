import re
import sqlite3
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_file('signup.kv')

class Signup(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
  
    def go_login(self):
        self.manager.current = 'login'
        
    def register_user(self):
        name = self.ids.name_text_field.text
        email = self.ids.email_text_field.text
        password = self.ids.password_text_field.text
        confirm_password = self.ids.confirm_password_text_field.text
        
        if not name or not email or not password or not confirm_password:
            self.ids.mensagem_login.text = "[color=#FFFFFF]Todos os campos são obrigatórios[/color]"
            return
        
        if password != confirm_password:
            self.ids.mensagem_login.text = "[color=#FFFFFF]As senhas não coincidem[/color]"
            return
        
        if not validaçãoEmail(email):
            self.ids.mensagem_login.text = "[color=#FFFFFF]Email inválido[/color]"
            return
        
        if not validaçãoSenha(password):
            self.ids.mensagem_login.text = "[color=#FFFFFF]Senha inválida.\nA senha deve conter pelo menos uma letra maiúscula,\numa letra minúscula,\num número\ne um dos seguintes caracteres especiais: @$!%*#?&.\nAlém disso, a senha deve ter no mínimo 6 caracteres.[/color]"
            return
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM usuarios WHERE email=?", (email,))
        if cursor.fetchone() is not None:
            self.ids.mensagem_login.text = "[color=#FFFFFF]O e-mail já está em uso[/color]"
            # conn.close()
            return
        
        cursor.execute("INSERT INTO usuarios (nome, senha, email, status) VALUES (?, ?, ?, ?)",
                       (name, password, email, "active"))
        conn.commit()
        # conn.close()
        
        self.ids.mensagem_login.text = "[color=#00FF00]Conta criada com sucesso[/color]"
        self.ids.name_text_field.text = ""
        self.ids.email_text_field.text = ""
        self.ids.password_text_field.text = ""
        self.ids.confirm_password_text_field.text = ""

    def build(self):
        pass

def validaçãoEmail(email):
    validarEmail = email
    r = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if r.match(validarEmail):
        return validarEmail
    else:
        return False

def validaçãoSenha(senha):
    r2 = re.compile(r'(?=.*[A-Z])')
    r3 = re.compile(r'(?=.*[a-z])')
    r4 = re.compile(r'(?=.*[0-9])')
    r5 = re.compile(r'(?=.*[@$!%*#?&])')
    r6 = re.compile(r'[A-Za-z\d@$!%*#?&]{6,255}$')
    validarSenha = senha
    if r2.match(validarSenha):
        r2Check = True
    else:
        r2Check = False
    if r3.match(validarSenha):
        r3Check = True
    else:
        r3Check = False
    if r4.match(validarSenha):
        r4Check = True
    else:
        r4Check = False
    if r5.match(validarSenha):
        r5Check = True
    else:
        r5Check = False
    if r6.match(validarSenha):
        r6Check = True
    else:
        r6Check = False
    if r2Check == True and r3Check == True and r4Check == True and r5Check == True and r6Check == True:
        return validarSenha
    else:
        return False
