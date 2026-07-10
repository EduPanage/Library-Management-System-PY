class Emprestimo:

    def __init__ (self,
                  usuario_id,
                  livro_id,
                  data_prevista,
                  data_devolucao,
                  id=None,
                  data_emprestimo=None,
                  status='ATIVO'):
        self.id = id
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        self.data_prevista = data_prevista
        self.data_devolucao = data_devolucao
        self.data_emprestimo = data_emprestimo
        self.status = status
        