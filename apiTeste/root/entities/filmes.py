from root.configs.base import Base
from sqlalchemy import Column, String, Integer 

class Filmes(Base): # implementação
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True) # declara chave primária, não nulo
    genero = Column(String, nullable=False) # não pode ser nulo
    ano = Column(Integer, nullable=False)

    def __repr__(self): # toString
        return f"Filme (titulo={self.titulo}, ano={self.ano})"
