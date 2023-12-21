import pymongo

# Conectando ao MongoDB Atlas
client = pymongo.MongoClient()
db = client[]

# Criando uma coleção chamada 'bank' para armazenar documentos de clientes
collection = db[]

# Inserindo documentos de exemplo
cliente_document = {
    'nome': 'João',
    'contas': [
        {'numero': '123', 'saldo': 1000},
        # Adicione mais contas conforme necessário
    ]
}

collection.insert_one(cliente_document)

# Recuperação de informações com base em pares de chave e valor
# Exemplo: Recuperar todas as informações do cliente com nome 'João'
resultado = collection.find_one({'nome': 'João'})
print(resultado)
