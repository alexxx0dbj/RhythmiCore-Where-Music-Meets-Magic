-- Generated by Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   at:        2023-12-16 21:56:19 EET
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE album (
    id_album NUMBER(3) NOT NULL,
    nume     VARCHAR2(30) NOT NULL
);

ALTER TABLE album
    ADD CONSTRAINT album_nume_ck CHECK ( REGEXP_LIKE ( nume,
                                                       '[a-zA-Z0-9.!?$&%-]{1,}' ) );

ALTER TABLE album ADD CONSTRAINT album_pk PRIMARY KEY ( id_album );

CREATE TABLE artist (
    id_artist NUMBER(3) NOT NULL,
    nume      VARCHAR2(30) NOT NULL
);

ALTER TABLE artist
    ADD CONSTRAINT artist_nume_ck CHECK ( REGEXP_LIKE ( nume,
                                                        '[a-zA-Z0-9.!?$&%-]{1,}' ) );

ALTER TABLE artist ADD CONSTRAINT artist_pk PRIMARY KEY ( id_artist );

ALTER TABLE artist ADD CONSTRAINT artist_nume_artist_uk UNIQUE ( nume );

CREATE TABLE bilbiotecautilizator (
    id_biblioteca_utilizator NUMBER(3) NOT NULL,
    id_utilizator            NUMBER(3) NOT NULL,
    id_melodie               NUMBER(3) NOT NULL,
    nota                     NUMBER(3, 2) NOT NULL
);

ALTER TABLE bilbiotecautilizator
    ADD CONSTRAINT nota CHECK ( nota BETWEEN 0 AND 5 );

ALTER TABLE bilbiotecautilizator ADD CONSTRAINT biblioteca_utilizator_pk PRIMARY KEY ( id_biblioteca_utilizator );

CREATE TABLE detaliigenuri (
    genmuzical_id_gen_muzical NUMBER(3) NOT NULL,
    melodie_id_melodie        NUMBER(3) NOT NULL,
    descriere                 VARCHAR2(30)
);

ALTER TABLE detaliigenuri ADD CONSTRAINT detaliigenuri_pk PRIMARY KEY ( genmuzical_id_gen_muzical,
                                                                        melodie_id_melodie );

CREATE TABLE detaliimelodie (
    id_artist  NUMBER(3) NOT NULL,
    id_album   NUMBER(3) NOT NULL,
    id_melodie NUMBER(3) NOT NULL,
    detalii    VARCHAR2(50)
);

CREATE TABLE genmuzical (
    id_gen_muzical NUMBER(3) NOT NULL,
    nume           VARCHAR2(30) NOT NULL,
    detalii        VARCHAR2(60)
);

ALTER TABLE genmuzical
    ADD CONSTRAINT genmuzical_nume_ck CHECK ( REGEXP_LIKE ( nume,
                                                            '[a-zA-Z0-9.-]{1,}' ) );

ALTER TABLE genmuzical ADD CONSTRAINT gen_muzical_pk PRIMARY KEY ( id_gen_muzical );

ALTER TABLE genmuzical ADD CONSTRAINT gen_muzical_nume_gen_uk UNIQUE ( nume );

CREATE TABLE melodie (
    id_melodie NUMBER(3) NOT NULL,
    nume       VARCHAR2(30) NOT NULL
);

ALTER TABLE melodie
    ADD CONSTRAINT melodie_nume_ck CHECK ( REGEXP_LIKE ( nume,
                                                         '[a-zA-Z0-9.!?$&%-]{1,}' ) );

ALTER TABLE melodie ADD CONSTRAINT melodie_pk PRIMARY KEY ( id_melodie );

CREATE TABLE ratingmelodie (
    rating       NUMBER(3, 2) NOT NULL,
    numar_voturi NUMBER(3),
    id_melodie   NUMBER(3) NOT NULL
);

ALTER TABLE ratingmelodie
    ADD CONSTRAINT ratingmelodie_rating_ck CHECK ( rating BETWEEN 0 AND 5 );

ALTER TABLE ratingmelodie ADD CONSTRAINT ratingmelodie_numar_voturi_ck CHECK ( numar_voturi >= 0 );

CREATE UNIQUE INDEX ratingmelodie__idx ON
    ratingmelodie (
        id_melodie
    ASC );

CREATE TABLE utilizator (
    id_utilizator NUMBER(3) NOT NULL,
    nume          VARCHAR2(30) NOT NULL,
    parola        VARCHAR2(30) NOT NULL,
    email         VARCHAR2(30) NOT NULL
);

ALTER TABLE utilizator
    ADD CONSTRAINT utilizator_nume_ck CHECK ( REGEXP_LIKE ( nume,
                                                            '^[a-zA-Z.-]' ) );

ALTER TABLE utilizator
    ADD CONSTRAINT utilizator_parola_ck CHECK ( length(parola) > 8 );

ALTER TABLE utilizator
    ADD CONSTRAINT utilizator_email_ck CHECK ( REGEXP_LIKE ( email,
                                                             '[a-z0-9._%-]+@[a-z0-9._%-]+\.[a-z]{2,4}' ) );

ALTER TABLE utilizator ADD CONSTRAINT utilizator_pk PRIMARY KEY ( id_utilizator );

ALTER TABLE utilizator ADD CONSTRAINT utilizator_nume_utilizator_uk UNIQUE ( nume );

ALTER TABLE utilizator ADD CONSTRAINT utilizator_adresa_email_uk UNIQUE ( email );

ALTER TABLE detaliimelodie
    ADD CONSTRAINT album_detaliimelodie_fk FOREIGN KEY ( id_album )
        REFERENCES album ( id_album );

ALTER TABLE detaliimelodie
    ADD CONSTRAINT artist_detaliimelodie_fk FOREIGN KEY ( id_artist )
        REFERENCES artist ( id_artist );

ALTER TABLE detaliigenuri
    ADD CONSTRAINT detaliigenuri_genmuzical_fk FOREIGN KEY ( genmuzical_id_gen_muzical )
        REFERENCES genmuzical ( id_gen_muzical );

ALTER TABLE detaliigenuri
    ADD CONSTRAINT detaliigenuri_melodie_fk FOREIGN KEY ( melodie_id_melodie )
        REFERENCES melodie ( id_melodie );

ALTER TABLE bilbiotecautilizator
    ADD CONSTRAINT melodie_bu_fk FOREIGN KEY ( id_melodie )
        REFERENCES melodie ( id_melodie );

ALTER TABLE detaliimelodie
    ADD CONSTRAINT melodie_detaliimelodie_fk FOREIGN KEY ( id_melodie )
        REFERENCES melodie ( id_melodie );

ALTER TABLE ratingmelodie
    ADD CONSTRAINT melodie_ratingmelodie_fk FOREIGN KEY ( id_melodie )
        REFERENCES melodie ( id_melodie );

ALTER TABLE bilbiotecautilizator
    ADD CONSTRAINT utilizator_bu_fk FOREIGN KEY ( id_utilizator )
        REFERENCES utilizator ( id_utilizator );

CREATE SEQUENCE album_id_album_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER album_id_album_trg BEFORE
    INSERT ON album
    FOR EACH ROW
    WHEN ( new.id_album IS NULL )
BEGIN
    :new.id_album := album_id_album_seq.nextval;
END;
/

CREATE SEQUENCE artist_id_artist_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER artist_id_artist_trg BEFORE
    INSERT ON artist
    FOR EACH ROW
    WHEN ( new.id_artist IS NULL )
BEGIN
    :new.id_artist := artist_id_artist_seq.nextval;
END;
/

CREATE SEQUENCE bilbiotecautilizator_id_biblio START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER bilbiotecautilizator_id_biblio BEFORE
    INSERT ON bilbiotecautilizator
    FOR EACH ROW
    WHEN ( new.id_biblioteca_utilizator IS NULL )
BEGIN
    :new.id_biblioteca_utilizator := bilbiotecautilizator_id_biblio.nextval;
END;
/

CREATE SEQUENCE genmuzical_id_gen_muzical_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER genmuzical_id_gen_muzical_trg BEFORE
    INSERT ON genmuzical
    FOR EACH ROW
    WHEN ( new.id_gen_muzical IS NULL )
BEGIN
    :new.id_gen_muzical := genmuzical_id_gen_muzical_seq.nextval;
END;
/

CREATE SEQUENCE melodie_id_melodie_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER melodie_id_melodie_trg BEFORE
    INSERT ON melodie
    FOR EACH ROW
    WHEN ( new.id_melodie IS NULL )
BEGIN
    :new.id_melodie := melodie_id_melodie_seq.nextval;
END;
/

CREATE SEQUENCE utilizator_id_utilizator_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER utilizator_id_utilizator_trg BEFORE
    INSERT ON utilizator
    FOR EACH ROW
    WHEN ( new.id_utilizator IS NULL )
BEGIN
    :new.id_utilizator := utilizator_id_utilizator_seq.nextval;
END;
/



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             9
-- CREATE INDEX                             1
-- ALTER TABLE                             29
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           6
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          6
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
