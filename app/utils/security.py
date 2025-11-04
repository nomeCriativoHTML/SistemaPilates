import hashlib
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "sua_chave_secreta_aqui"  # mudar para uma variável de ambiente
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # duração do token JWT

# -------------------------------
# Funções de hash de senha
# -------------------------------
def hash_senha(senha: str) -> str:
    """Criptografa a senha usando SHA-256."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()

def verify_senha(senha: str, senha_hash: str) -> bool:
    """Verifica se a senha fornecida corresponde ao hash armazenado."""
    return hash_senha(senha) == senha_hash

# -------------------------------
# Função para criar JWT
# -------------------------------
def create_access_token(data: dict) -> str:
    """Gera um token JWT com payload."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token
