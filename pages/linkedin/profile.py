from pages.linkedin.info_profile import Profile_info
from data.linkedin.dados import dados_profile_info
from bs4 import BeautifulSoup
import time


class Profile():
    def __init__(self, dados, driver):
        self.dados = dados
        self.driver = driver
        self.profile_info_page = Profile_info(dados_profile_info, self.driver)

    def scraping(self):
        self.lista_todos_profiles()

    def navega_page_profile(self, url):
        self.driver.acessar_url(url)
        print("Profile acessado com sucesso.")
        time.sleep(2)

    def lista_todos_profiles(self):
        lista_usuarios = []
        for item in self.profile_txt():
            url = item.split()[0]
            self.navega_page_profile(url)
            usuario = self.usuario()
            lista_usuarios.append(usuario)
            self.profile_info_page.scraping(lista_usuarios)

    def profile_txt(self):
        diretorio = self.dados['diretorio_txt']
        txt_profile = open(diretorio, 'r')
        return txt_profile.readlines()

    def get_html(self):
        time.sleep(2)
        elemento = self.driver.busca_css(self.dados['css'])
        html_content = elemento.get_attribute('outerHTML')
        return html_content
    

    def organizar_dados(self, html_content):
        bs = BeautifulSoup(html_content, 'html.parser')
        url = self.driver.url_atual()
        model = {'nome': None, 'estado': None, 'url': url}
        try:
            nome = bs.findAll(
                'h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'})[0].text
            estado = bs.findAll(
                'span', {'class': 'text-body-small inline t-black--light break-words'})[0].text.strip()
            model['nome'] = nome
            model['estado'] = estado
        except:
            pass
        return model

    def usuario(self):
        html_content = self.get_html()
        lista_usuario = self.organizar_dados(html_content)
        # salvar no banco de dados
        return lista_usuario
