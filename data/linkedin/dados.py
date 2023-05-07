from dotenv import dotenv_values
import os

diretorio_html = f'{os.getcwd()}/relatorio/linkedin/html/index.html'
diretorio_txt = f'{os.getcwd()}/relatorio/linkedin/txt/leads-linkedin.txt'

dados_usuario = dotenv_values(".env")

dados_login = {
    "url_login_page": "https://www.linkedin.com/home",

    "usuario": dados_usuario['USUARIO'],
    "input_usuario": '//*[@id="session_key"]',

    "senha":  dados_usuario['PASSWORD'],
    "input_senha": '//*[@id="session_password"]',

    "botao": '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button',
}

dados_home = {

    "url_follow_page": "https://www.linkedin.com/mynetwork/network-manager/people-follow/followers/",

}

dados_seguidores = {
    "css_box_dados": 'scaffold-finite-scroll__content',

    "diretorio_html": diretorio_html,

    "diretorio_txt": diretorio_txt
}

dados_profile = {
    'diretorio_txt': diretorio_txt,
    'css': 'ph5'
}

dados_profile_info = {
    'link_profile_info': 'top-card-text-details-contact-info',
    'content_html': '/html/body'
}
