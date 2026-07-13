from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from app.utils.password import hash_password, verify_password

class AuthService:

    def __init__(self, db):
        self.usuario_repository = UsuarioRepository(db)

    def register(self,
                 nome,
                 email,
                 password,
                 perfil
    ):
        usuario_existente = self.usuario_repository.search_by_email(email)

        if usuario_existente:
            raise ValueError("Email already registered!")
        
        password_hash = hash_password(password)

        usuario = Usuario(
            nome = nome,
            email = email,
            senha_hash = password_hash,
            perfil = perfil
        )

        self.usuario_repository.save(usuario) 