# Fake Pinterest

Este é um projeto que fiz acompanhando um mini curso da Hashtag Treinamentos.

O objetivo do curso era criar uma "cópia" do Pinterest utilizando Python com o framework Flask.

O meu objetivo era entender melhor como funcionava o desenvolvimento Full Stack em Python e ter uma ideia
de como funcionam frameworks full stack como Django(Python) e o Laravel(PHP).

Utilizei o Python 3.11.3, Flask e SQLite nesse projeto.

## Guia para rodar o projeto localmente.

Presumo que você já tem pelo menos o Python 3.11 instalado, o ideal é que esteja usando o
Python 3.11.3.

### Após clonar o repósitorio, abra o terminal na pasta dele e crie um ambiente virtual com:
```
python -m venv venv
```
### Ative o ambiente virtual:
```
venv/Scripts/activate
```

### Instale as dependências do projeto com:
```
pip install -r requirements.txt
```
### Cria o banco de dados com:
```
python criar_banco.py
```

### Agora é só ser feliz com:
```
python main.py
```

Não deixei o banco de dados criado por conta do SQLAlchemy estar estourando um erro de
integridade da chave estrangeira quando o projeto é clonado.
Mas deixei um arquivo com as fotos usadas na criação do projeto para você não ter que ficar caçando
foto para testar.

E se der der algum erro, boa sorte kkkk

## Futuro

Talvez um dia eu retorne nesse projeto para brincar um pouco e adicionar mais algumas features como:
- Barra de pesquisa
- Redefinir senha
- Sistema de verificação de e-mail
- Sistema de Likes
- Sistema de Comentários
- Sistema de Favoritos
- Compartilhar Post
- Ao clickar no post dar foco a ele como um pop-up centralizado na página
- Sistema de seguir perfil
- Refazer esse front end que tá meio torto(Talvez eu faça isso quando for praticar Tailwind) kkkk
- Adicionar responsividade e acesibilidade ao front end.
