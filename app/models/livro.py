class Livro:
    
    def __init__ (self,
                  titulo,
                  autor_id,
                  categoria_id,
                  ano_publicacao,
                  quantidade_total,
                  valor_aluguel,
                  id=None,
                  criado_em=None):
        self.id = id
        self.titulo = titulo
        self.autor_id = autor_id
        self.categoria_id = categoria_id
        self.ano_publicacao = ano_publicacao
        self.quantidade_total = quantidade_total
        self.valor_aluguel = valor_aluguel
        self.criado_em = criado_em