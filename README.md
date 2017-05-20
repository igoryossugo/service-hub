# Service hub

## Instalação (linux/mac os)
O projeto roda em python 2.7, Django.
Para configuração do projeto, é necessário a instalação no [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) e [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

Fazer download do repositório e criar ambiente virutual.
```
$ git clone git@github.com:igoryossugo/servicehub.git
$ mkvirtualenv servicehub
```

Após isso, instalar as dependências e bibliotecas do projeto
```
$ pip install -r requirements/requirements.txt
```

Criar tabelas do banco
```
$ make migrate
```

Para rodar o projeto
```
$ make runserver
```

Dúvidas sobre a implementação e ultilização do framework django:
https://www.djangoproject.com/