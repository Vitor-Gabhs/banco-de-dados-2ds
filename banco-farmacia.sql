CREATE TABLE FARMACIA (
    id_farmacia     INTEGER PRIMARY KEY,           -- auto-increment automático
    nome_farmacia   VARCHAR(100) NOT NULL,
    cnpj_farmacia   VARCHAR(14)  NOT NULL UNIQUE,
    tel_farmacia    VARCHAR(20),
    end_farmacia    VARCHAR(200)
);

CREATE TABLE Produto (
    cod_produto     INTEGER PRIMARY KEY,           -- auto-increment
    valor_produto   DECIMAL(10,2) NOT NULL,
    qtd_produto     INTEGER NOT NULL DEFAULT 0,
    id_farmacia     INTEGER NOT NULL,

    FOREIGN KEY (id_farmacia) REFERENCES FARMACIA(id_farmacia)
);

CREATE TABLE Farmaceutico (
    rg_farmaceutico    VARCHAR(20) PRIMARY KEY,
    nome_farmaceutico  VARCHAR(100) NOT NULL,
    id_farmacia        INTEGER NOT NULL,

    FOREIGN KEY (id_farmacia) REFERENCES FARMACIA(id_farmacia)
);
