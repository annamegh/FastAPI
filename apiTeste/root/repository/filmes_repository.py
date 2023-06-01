#interação de sql com o banco

from root.configs.connection import DBConnectionHandler
from root.entities.filmes import Filmes

class FilmesRepository:
    def select(self):
        with DBConnectionHandler() as db: #faz uma instancia da classe e permite acesso aos elementos dela
            data = db.session.query(Filmes).all()
            return data
        
    def insert(self, titulo, genero, ano): #insere um novo filme no banco
        with DBConnectionHandler() as db:
            data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_insert)
            db.session.commit()
        
    def delet(self, titulo): #busca pelo titulo e deleta
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano): #busca o filme com o titulo e faz o update do ano
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({ "ano": ano})
            db.session.commit()