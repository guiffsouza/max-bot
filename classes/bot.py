from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Bot():
    def __init__(self, window):
        self.browser = self.config(window)

    def config(self, window):
        if window:
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            return webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    def acessar_url(self, url):
        self.browser.get(url)

    def url_atual(self):
        return self.browser.current_url

    def input_dados(self, path, dado):
        self.browser.find_element('xpath', path).send_keys(dado)

    def clicar(self, xpath):
        self.browser.find_element('xpath', xpath).click()

    def busca_css(self, css):
        return self.browser.find_element(By.CLASS_NAME, css)

    def busca_xpath(self, id_tag):
        return self.browser.find_element(By.XPATH, id_tag)

    def clica_link(self, id_tag):
        self.browser.find_element(By.ID, id_tag).click()
