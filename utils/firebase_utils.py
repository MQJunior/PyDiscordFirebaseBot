import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa o Firebase
try:
    cred = credentials.Certificate("conf/credentials.json")
    firebase_admin.initialize_app(cred)
    print("Firebase inicializado com sucesso.")
except Exception as e:
    raise RuntimeError(f"Erro ao inicializar o Firebase: {e}")

# Função para verificar se o canal de logs está definido no Firebase
def is_channel_log_defined():
    try:
        # Verifica se o documento 'logs' existe na coleção 'config'
        channel_log_ref = firestore.client().collection('channels').document('log')
        return channel_log_ref.get().exists
    except Exception as e:
        print(f"Erro ao verificar o canal de logs: {e}")
        return False

# Função para verificar se a coleção 'setup' existe
def check_setup_collection():
    try:
        # Tenta acessar a coleção 'setup'
        firestore.client().collection('channels').get()
        if not firestore.client().collection('channels').get():
            return False
        else:
            return True
    except Exception as e:
        print(f"Erro ao verificar a coleção 'setup': {e}")
        return False

# Função para setar o id do canal de logs
def set_channel_log_id(channel_id):
    try:
        # Referência para o documento 'logs' na coleção 'config'
        channel_log_ref = firestore.client().collection('channels').document('log')

        # Atualiza o ID do canal
        channel_log_ref.set({'channel_id': channel_id}, merge=True)
        print(f"ID do canal de logs atualizado para {channel_id} no Firebase.")
    except Exception as e:
        print(f"Erro ao definir o ID do canal de logs: {e}")

# ...
def get_channel_log_id():
    try:
        # Referência para o documento 'setup' na coleção 'channels'
        setup_ref = firestore.client().collection('channels').document('log')

        # Obtém os dados do documento
        setup_data = setup_ref.get().to_dict()
        
        print(setup_data)

        # Retorna o ID do canal de log se existir, ou None se não existir
        return setup_data.get('channel_id')
    except Exception as e:
        # logging.error(f"Erro ao obter o ID do canal de logs: {e}")
        return None