from pages.linkedin.login import Login
from pages.linkedin.home import Home
from pages.linkedin.seguidores import Seguidores
from pages.linkedin.profile import Profile
from data.linkedin.dados import dados_login, dados_home, dados_seguidores, dados_profile
from classes.bot import Bot


class Linkedin():

    def __init__(self, window):
        self.driver = Bot(window)
        self.login_page = Login(dados_login, self.driver)
        self.home_page = Home(dados_home, self.driver)
        self.seguidores_page = Seguidores(dados_seguidores, self.driver)
        self.profile_page = Profile(
            dados_profile, self.driver)

    def get_followers(self):
        self.login_page.login()
        self.home_page.navega_seguidores()
        self.seguidores_page.get_dados()

    def get_dados_followers(self):
        self.login_page.login()
        self.profile_page.scraping()

    def listar_usuarios(self):
        self.profile_page.lista_todos_profiles()

    def scraping(self):
        self.get_followers()
        self.get_dados_followers()