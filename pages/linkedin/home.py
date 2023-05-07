import time


class Home():
    def __init__(self, dados, driver):
        self.dados = dados
        self.driver = driver

    def navega_seguidores(self):
        self.acessar_seguidores()

    def acessar_seguidores(self):
        self.driver.acessar_url(self.dados["url_follow_page"])
        print("Acessando pagina dos seguidores.")
        time.sleep(5)
