from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship('Cliente', back_populates='contas')

# Criando o banco de dados
engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)

# Inserindo dados de exemplo
Session = sessionmaker(bind=engine)
session = Session()

cliente1 = Cliente(nome='João')
conta1 = Conta(numero='123', saldo=1000, cliente=cliente1)

session.add(cliente1)
session.commit()

# Executando métodos de recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f'Cliente: {cliente.nome}')
    for conta in cliente.contas:
        print(f'Conta: {conta.numero}, Saldo: {conta.saldo}')


