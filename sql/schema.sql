CREATE TABLE IF NOT EXISTS usuarios (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	senha_hash TEXT NOT NULL,
	perfil VARCHAR(20) NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(email),
	
	CONSTRAINT chk_perfil
	CHECK (
	perfil IN ('ADMIN', 'FUNCIONARIO', 'CLIENTE')
	)
);

CREATE TABLE IF NOT EXISTS autores (
	id serial PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	UNIQUE (nome)
);

CREATE TABLE IF NOT EXISTS categorias (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS livros (
	id SERIAL PRIMARY KEY,
	titulo VARCHAR(200) NOT NULL,
	autor_id INTEGER NOT NULL,
	categoria_id INTEGER NOT NULL,
	ano_publicacao INTEGER NOT NULL,
	quantidade_total INTEGER NOT NULL,
	valor_aluguel NUMERIC (10, 2) NOT NULL,
	criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

	CONSTRAINT fk_livros_autor
	FOREIGN KEY (autor_id) REFERENCES autores(id),

	CONSTRAINT fk_livros_categoria
	FOREIGN KEY (categoria_id) REFERENCES categorias(id),
	
	CONSTRAINT chk_quant_livro
	CHECK (quantidade_total >= 0),
	
	CONSTRAINT chk_ano_publicacao
	CHECK (ano_publicacao <= EXTRACT(YEAR FROM CURRENT_DATE)),
	
	CONSTRAINT chk_valor_aluguel
	CHECK (valor_aluguel >= 0)
);

CREATE TABLE IF NOT EXISTS emprestimos (
	id SERIAL PRIMARY KEY,
	usuario_id INTEGER NOT NULL,
	livro_id INTEGER NOT NULL,
	data_emprestimo DATE NOT NULL DEFAULT CURRENT_DATE,
	data_prevista DATE NOT NULL ,
	data_devolucao DATE,
	status VARCHAR(20) NOT NULL DEFAULT 'ATIVO',

	CONSTRAINT fk_emprestimos_usuario
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id),

	CONSTRAINT fk_emprestimos_livro
	FOREIGN KEY (livro_id) REFERENCES livros(id),
	
	CONSTRAINT chk_status_emprestimo
	CHECK (
	status IN ('ATIVO', 'DEVOLVIDO')
	)
);

CREATE TABLE IF NOT EXISTS logs (
	id SERIAL PRIMARY KEY,
	usuario_id INTEGER NOT NULL,
	acao TEXT NOT NULL,
	data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

	CONSTRAINT fk_logs_usuario
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- INDEX TABLE autores

CREATE INDEX IF NOT EXISTS idx_autores_nome
	ON autores(nome);

-- INDEX TABLE categorias

CREATE INDEX IF NOT EXISTS idx_categorias_nome
	ON categorias(nome);

-- INDEX TABLE livros

CREATE INDEX IF NOT EXISTS idx_livros_titulo
	ON livros(titulo);
CREATE INDEX IF NOT EXISTS idx_livros_autor
	ON livros(autor_id);
CREATE INDEX IF NOT EXISTS idx_livros_categoria
	ON livros(categoria_id);

-- INDEX TABLE emprestimos

CREATE INDEX IF NOT EXISTS idx_emprestimos_usuario
	ON emprestimos(usuario_id);
CREATE INDEX IF NOT EXISTS idx_emprestimos_livro
	ON emprestimos(livro_id);

-- INDEX TABLE logs

CREATE INDEX IF NOT EXISTS idx_logs_usuario
	ON logs(usuario_id);
CREATE INDEX IF NOT EXISTS idx_logs_data_hora
	ON logs(data_hora);





