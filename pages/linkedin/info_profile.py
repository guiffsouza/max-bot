from bs4 import BeautifulSoup
import time


class Profile_info():
    def __init__(self, dados, driver):
        self.dados = dados
        self.driver = driver

    def scraping(self, lista_usuario):
        self.navega_profile_info()
        self.imprime_dados(lista_usuario)

    def navega_profile_info(self):
        self.driver.clica_link(self.dados['link_profile_info'])
        time.sleep(2)

    def get_html(self):
        time.sleep(2)
        elemento = self.driver.busca_xpath(self.dados['content_html'])
        html_content = elemento.get_attribute('outerHTML')
        return html_content

    def imprime_dados(self, lista_usuario):
        html_content = self.get_html()
        usuario = self.organiza_dados(html_content, lista_usuario)
        print(usuario)

    def organiza_dados(self, html_content, lista_usuarios):
        bs = BeautifulSoup(html_content, 'html.parser')
        url_atual = self.driver.url_atual()
        for usuario in lista_usuarios:
            url_atual = url_atual.replace("overlay/contact-info/", "")
            if usuario['url'] == url_atual:
                try:
                    telefone = bs.findAll(
                        'span', {'class': 't-14 t-black t-normal'})[0]
                    email = bs.findAll(
                        'a', {'class': 'pv-contact-info__contact-link link-without-visited-state t-14'})[2]
                    usuario['telefone'] = telefone.text.strip()
                    usuario['email'] = email.text.strip()
                except:
                    usuario['telefone'] = None
                    usuario['email'] = None
        return lista_usuarios