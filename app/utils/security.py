from passlib.context import CryptContext

# Configuração do CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
    """Gera o hash da senha"""
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str) -> bool:
    """Verifica se a senha corresponde ao hash"""
    return pwd_context.verify(senha, hash)
