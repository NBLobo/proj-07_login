from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
import stdiomask
from time import sleep
init(autoreset=True)

# Criar o Menu de Opções


def exibir_menu():
    print(Fore.GREEN + '''       Bem-Vindos ao Projeto
          Sistema de Login        
Escolha uma Opção:
[1] Cadastrar novo usuário
[2] Fazer login
[3] Sair ou digite Enter    
''')
    try:
        opcao = int(input('Digite sua opção: '))
        return(opcao)
    except ValueError:
        print()

# Fazer login com nome e senha do usuário


def fazer_login():
    login = input('Nome: ')
    senha = stdiomask.getpass(prompt='Senha: ', mask='')
    return(login, senha)
#    senha = stdiomask.getpass(prompt='Senha: ', mask='*')

# Pesquisar no arquivo usuarios.txt


def buscar_usuario(login, senha):
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


while True:
    system('cls')
    opcao = exibir_menu()

    if opcao == 1:
        # Cadastrar novo usuário
        login, senha = fazer_login()
        if login == senha:
            print('Sua senha deve ser diferente do login.')
            senha = getpass('Senha: ')
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.RED+'Usuário já existe!')
            sleep(2)
            # exit()
        else:
            with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.writelines(f'{login} {senha}\n')
            print(Fore.CYAN + 'Cadastro aprovado!')
            exit()

    elif opcao == 2:
        # Fazer o Login do usuário
        login, senha = fazer_login()
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.CYAN + 'Login realizado com sucesso!')
            sleep(1)
            exit()
        else:
            print(
                Fore.RED+'Você deve ter digitado seu nome de usuário ou a senha errado.\n Por favor verefique.')
            sleep(2)
    else:
        system('cls')
        print(Fore.LIGHTMAGENTA_EX+'GoodBay!')
        break
