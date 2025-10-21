from passlib.context import CryptContext

# Configuração do CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
    """Gera o hash da senha com truncamento para 72 bytes"""
    senha_truncada = senha[:72]  # Trunca a senha se for maior que 72 caracteres
    return pwd_context.hash(senha_truncada)

def verificar_senha(senha: str, hash: str) -> bool:
    """Verifica se a senha corresponde ao hash"""
    senha_truncada = senha[:72]  # Trunca a senha também na verificação
    return pwd_context.verify(senha_truncada, hash)
