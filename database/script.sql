PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE USUARIOS (
            id_user INTEGER NOT NULL,
            nome TEXT NOT NULL,
            numero TEXT NOT NULL,
            foto IMAGE NOT NULL,
            estagio INTEGER NOT NULL,
            PRIMARY KEY (id_user)
        );
COMMIT;