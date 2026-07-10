class Log:
    
    def __init__ (self, usuario_id, acao, data_hora=None, id=None):
        
        self.id = id
        self.usuario_id = usuario_id
        self.acao = acao
        self.data_hora = data_hora