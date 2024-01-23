# /conf/logger_config.py
import logging

# Configuração básica do logging
logging.basicConfig(filename='bot.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Se necessário, adicione configurações adicionais
# Exemplo:
# logging.getLogger('discord').setLevel(logging.WARNING)
# logging.getLogger('asyncio').setLevel(logging.WARNING)
