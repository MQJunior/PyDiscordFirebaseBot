# /utils/language_utils.py

from conf.languages import LANGUAGES
import logging

def get_language():
    global current_language
    return LANGUAGES.get(current_language, LANGUAGES[1])  # Padrão para Português se não estiver definido


def get_language_value(p_key:str):
    tmp_return = 'none'
    lang = get_language()
    if p_key in lang:
        tmp_return = p_key
    return lang[tmp_return]
    

def set_language(new_language, language_options=LANGUAGES):
    language = language_options.get(new_language)
    if language:
        global current_language
        current_language = new_language
        tmp_code_language = get_language_value('code') + ' - '+get_language_value('name')
        lang = get_language()
        tmp_msg = get_language_value('language_utils_set_language')
        logging.info(f'{tmp_msg}: {tmp_code_language}')
    else:
        logging.warning('Opção de idioma inválida.')

# set_language(2, LANGUAGES)  
