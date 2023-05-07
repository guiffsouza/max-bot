from bs4 import BeautifulSoup
import time


class Seguidores():
    def __init__(self, dados, driver):
        self.dados = dados
        self.driver = driver

    def get_dados(self):
        self.scroll_final_page()
        self.salva_dados()

    def scroll_final_page(self):
        print('Realizando scroll da pagina.')
        SCROLL_PAUSE_TEMPO = 1.5
        ultima_altura_pagina = self.driver.browser.execute_script(
            "return document.body.scrollHeight")

        while True:
            self.driver.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TEMPO)
            nova_altura_pagina = self.driver.browser.execute_script(
                "return document.body.scrollHeight")
            if nova_altura_pagina == ultima_altura_pagina:
                break
            ultima_altura_pagina = nova_altura_pagina

    def get_html(self):
        print("Gerando HTML")
        time.sleep(2)
        element = self.driver.busca_css(self.dados["css_box_dados"])
        html_content = element.get_attribute('outerHTML')
        diretorio = self.dados["diretorio_html"]
        arquivo_html = open(diretorio, "w")
        arquivo_html.write(html_content)
        print('Pagina HTML salva com sucesso.')
        return html_content

    def salva_dados(self):
        html_content = self.get_html()
        bs = BeautifulSoup(html_content, 'html.parser')
        linhas = bs.findAll(
            'span', {'class': 'entity-result__title-text t-16'})

        lista = []
        diretorio = self.dados["diretorio_txt"]
        arquito_txt = open(diretorio, "w")

        for item in linhas:
            link = item.findChildren("a")
            url = link[0]['href']
            lista.append(url)
            arquito_txt.write(f'{url}\n')
        print('Dados salvos com sucesso.')
