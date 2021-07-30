import os
import PySimpleGUI as sg
#from logout import janela_de_logout


class Clogui:
    def __init__(self):
        # Layout da janela
        sg.theme('BlueMono')
        layout = [
            [sg.Text('Login', font=12, size=(10, 1)), sg.Input(
                key='login', font=12, size=(20, 1))],
            [sg.Text('Senha', font=12, size=(10, 1)), sg.Input(
                key='senha', password_char=' ', font=12, size=(20, 1))],
            [sg.Button('Novo Usuário', font=12), sg.Button(
                'Fazer Login', font=12), sg.Button('Sair', font=12)]
        ]

    # Declarar Janela
        self.janela = sg.Window('Login de Usuários',
                                layout, font=14)
        self.janela1_ativa = False

    def buscar_usuario(self, login, senha):
        usuarios = []
        try:
            with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
                for linha in arquivo:
                    linha = linha.strip(",")
                    usuarios.append(linha.split())
    #login, senha = fazer_login()
                for usuario in usuarios:
                    nome = usuario[0]
                    password = usuario[1]
                    if login == nome and senha == password:
                        return True
        except FileNotFoundError:
            return False

    # Limpa o Nome do login e a senha digitada na janela

    def limpar(self, login, senha):
        self.janela['login'].update('')
        self.janela['senha'].update('')
        self.janela['login'].SetFocus()
        return

    def Iniciar(self):
        sg.popup_no_titlebar(
            'Bem_Vindos\nProjeto #07 - Sistema de Login.\nPrincipais funcionalidades desse Sistema:\nCadastrar Novos Usuários;\nEfetuar Login de usuário Cadastrado;\nCriar e\ou Atualizar o arquivo de Usuários.', font=12, text_color='blue')
        while True:
            eventos, valores = self.janela.read()
            login = self.janela['login'].get()
            senha = self.janela['senha'].get()
            if eventos == sg.WINDOW_CLOSED:
                break
    # Opção 1
            if eventos == 'Novo Usuário':
                if login == senha:
                    sg.popup_no_titlebar(
                        'Sua senha deve ser diferente do nome do usuário.', font=12, text_color='red')
                    self.limpar(valores['login'], valores['senha'])

                else:
                    user = self.buscar_usuario(login, senha)
                    if user == True:
                        sg.popup_no_titlebar('Usuário já existe!',
                                             font='12', text_color='red')
                        self.limpar(valores['login'], valores['senha'])

                    else:

                        with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                            arquivo.writelines(f' {login} {senha}\n')
                            sg.popup_no_titlebar(
                                'Novo Usuário Aprovado!', font=12, text_color='blue',)

    # Opção 2
            if eventos == 'Fazer Login':
                user = self.buscar_usuario(login, senha)
                if user == True:
                    login = login.capitalize()
                    self.janela.hide()
            # Janela de Boas vindas
#                    sg.popup_no_titlebar(
#                        f'Bem Vindo, {login} seu login foi realizado com sucesso!', font=14, text_color='blue')
                    self.janela1_ativa = True
                    layout1 = [
                        [sg.Text(
                            f'{login}, voce esta logado.')],
                        [sg.Button('Logout')]
                    ]
                    janela1 = sg.Window('Logout', layout1, font="Helvetica 14")
                    eventos1, valores1 = janela1.read()
                    if eventos1 == sg.WINDOW_CLOSED or 'Logout':
                        janela1.close()
                        self.janela.un_hide()
                        self.limpar(valores['login'], valores['senha'])
                else:
                    sg.popup_no_titlebar(
                        f'Você deve ter digitado o nome de usuário e/ou a senha errado.\n Por favor verefique.', font=12, text_color='red')
                    self.limpar(valores['login'], valores['senha'])

    # Opção 3
            if eventos == 'Sair':
                sg.popup_no_titlebar('GoodBay!', font='18', text_color='blue')
                self.janela.close()


usuario = Clogui()
usuario.Iniciar()
