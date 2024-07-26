-- Pesssoa -1- -n-> Contato
DROP DATABASE IF EXISTS Contato;

CREATE TABLE Contato;
USE Contato;

CREATE TABLE Pesssoa(
    id_pessoa INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(75) NOT NULL,
    nascimento DATE NULL

    CONSTRAINT `pk_pessoa` PRIMARY KEY (id_pessoa)
);

INSERT INTO Pesssoa (id_pessoa, nome, nascimento)
VALUES
    (1, "Lucas", "1990-02-01"),
    (2, "Nelson", "2004-12-10"),
    (3, "Victor", "2004-12-06")
