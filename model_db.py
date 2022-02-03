from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///vagas.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Vagas(Base):
    __tablename__ = 'vagas'
    vaga_id = Column(Integer, primary_key=True)
    titulo = Column(String(50), index=True)
    descricao = Column(String(1000))
    salario = Column(Float)
    empresa = Column(String(50))
    contratacao = Column(String(10))
    modalidade = Column(String(20), index=True)

    def __repr__(self):
        return '<Vaga: {}>'.format(self.titulo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


# função que vai criar o DB
def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
