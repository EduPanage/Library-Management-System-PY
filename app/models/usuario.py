class Usuario:
    
    def __init__(self, 
                 nome, 
                 email, 
                 senha_hash, 
                 perfil, 
                 ativo=True, 
                 id=None ,
                 criado_em=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.perfil = perfil
        self.ativo = ativo
        self.criado_em = criado_em
        