# MaxBot

![Avatar Max](https://media.discordapp.net/attachments/1097950471307669615/1100827652450943036/1f9d1d01-e02f-4fc3-8c18-e88b14cd7b5f.jpg?width=900&height=600)

> Status: Desenvolvimento

O MaxBot é um bot desenvolvido em Python3 que tem como objetivo coletar dados _publicos_ de redes sociais como Linkedin, Intagram e Facebook. Os dados coletados podem ser utilizados para estudos de marketing, contato com os usuarios, entre outros.

### Arquitetura

A arquitetura escolhida para desenvolver o projeto foi a Page Objects, onde consiste em criar um objeto por página.

### Como Utilizar

Um arquivo `.env` contendo os dados de login deve ser criado.

```
USUARIO="login de usuario"
PASSWORD="senha do usuario"
```

Chamando o metodo `get_followers()` conseguimos realizar a busca da `URL` pelos seguidores no linkedin.

```
from classes.linkedin import Linkedin
bot_max = Linkedin(dados_linkedin)
bot_max.get_followers()
```

Chamando o metodo `get_dados_followers()` conseguimos realizar a busca pelos dados publicos dos seguidores do usuarios.

```
from classes.linkedin import Linkedin
bot_max = Linkedin(dados_linkedin)
bot_max.get_dados_followers()
```
