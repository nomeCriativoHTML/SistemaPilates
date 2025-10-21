import hashlib

def hash_senha(senha: str) -> str:
    """Criptografa a senha usando SHA-256."""
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def verificar_senha(senha: str, senha_hash: str) -> bool:
    """Verifica se a senha fornecida corresponde ao hash armazenado."""
    return hash_senha(senha) == senha_hash
