import uuid
from datetime import datetime

def gerar_id():
    """Gera um ID único usando UUID4"""
    return str(uuid.uuid4())

def ano_atual():
    """Retorna o ano atual"""
    return datetime.now().year
