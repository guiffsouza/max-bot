import time
import os


class Login():
    def __init__(self, dados, driver):
        self.dados = dados
        self.driver = driver

    def login(self):
        self.abrir_linkedin()
        self.realiza_login()

    def abrir_linkedin(self):
        self.driver.acessar_url(self.dados["url_login_page"])
        print("O Linkedin foi acessado com sucesso.")
        self.criar_diretorios('./relatorio/linkedin/html')
        self.criar_diretorios('./relatorio/linkedin/txt')
        time.sleep(2)

    def criar_diretorios(self, diretorio):
        if not os.path.isdir(diretorio):
            os.makedirs(diretorio)
            print(f'Criando diretorio {diretorio}')
        else:
            return print(f'O diretorio {diretorio} já existe.')

    def realiza_login(self):
        self.driver.input_dados(
            self.dados["input_usuario"], self.dados["usuario"])
        self.driver.input_dados(self.dados["input_senha"], self.dados["senha"])
        self.driver.clicar(self.dados["botao"])
        print("Login realizado com sucesso!")
        time.sleep(2)
