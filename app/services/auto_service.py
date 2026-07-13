from repositories.usuario_repository import UsuarioRepository
from utils.password import create_hash, verify_password

class AuthService:

    def __init__(self):
        self.usuario_repository = UsuarioRepository()