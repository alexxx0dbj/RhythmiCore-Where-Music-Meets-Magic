-- INSERT-URI IN TABELE 

--delete tabele si resetare autoincrement
DELETE FROM bilbiotecautilizator;
EXEC reset_sequence('bilbiotecautilizator_id_biblio');

DELETE FROM utilizator;
EXEC reset_sequence('utilizator_id_utilizator_seq');

DELETE FROM  detaliimelodie;

DELETE FROM detaliigenuri;

DELETE FROM  album;
EXEC reset_sequence('album_id_album_seq');

DELETE FROM artist;
EXEC reset_sequence('artist_id_artist_seq');

DELETE FROM  ratingmelodie;

DELETE FROM  melodie;
EXEC reset_sequence('melodie_id_melodie_seq');

DELETE FROM genmuzical;
EXEC reset_sequence(' genmuzical_id_gen_muzical_seq');



-- ARTIST 
INSERT INTO artist VALUES (null,'Michael Jackson');
INSERT INTO artist VALUES (null,'George Michael');
INSERT INTO artist VALUES (null,'Elton John');
INSERT INTO artist VALUES (null,'Paul McCartney');
INSERT INTO artist VALUES (null,'Stevie Wonder');




-- ALBUM
INSERT INTO album VALUES (null, 'Thriller'); --Michael Jackson
INSERT INTO album VALUES (null, 'Duets');  --Elton John
INSERT INTO album VALUES (null, 'Tug of War'); --Paul McCartney
INSERT INTO album VALUES (null, 'Faith'); --George Michael
INSERT INTO album VALUES (null, 'Songs in the Key of Life'); -- Stevie Wonder




--MELODII
--colaborari melodii

-- 1) album Duets Elton John colab cu George Michael
INSERT INTO melodie VALUES ( null, 'Dont Let the Sun Go Down on Me');

--2) album Tug of War Paul McCartney cu Stevie Wonder
INSERT INTO melodie VALUES (null, 'Ebony and Ivory');

--3) album Thriller Michael Jackson cu Paul McCartney
INSERT INTO melodie VALUES ( null, 'The Girl Is Mine');

--melodii un singur interpret
--4) Thriller Michael Jackson
INSERT INTO melodie VALUES (null, 'Beat It');

--5) Thriller Michael Jackson
INSERT INTO melodie VALUES ( null, 'Billie Jean');

--6) Duets Elton John
INSERT INTO melodie VALUES ( null, 'Dont Go Breaking My Heart');

--7) Songs in the Key of Life Stevie Wonder
INSERT INTO melodie VALUES (null, 'Sir Duke');

--8) Tug of War Paul McCartney
INSERT INTO melodie VALUES ( null, 'Take It Away');

--9) Faith George Michael
INSERT INTO melodie VALUES ( null, 'One More Try');

--10) Faith George Michael
INSERT INTO melodie VALUES (null, 'Faith');



--RATING

-- Exemplu de inser?ie în ratingmelodie cu id_melodie din melodie egal cu id_melodie din ratingmelodie
INSERT INTO ratingmelodie (rating, numar_voturi, id_melodie)
SELECT 0.00, null, m.id_melodie
FROM melodie m;



--DETALII MELODIE
--melodie The Girl Is Mine
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Melodie compusa in anul 1982 '
FROM artist a, album al, melodie m
WHERE a.nume = 'Michael Jackson' AND m.nume = 'The Girl Is Mine' AND al.nume = 'Thriller';


INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Melodie despre competitia pentru aceeasi femeie'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Paul McCartney' AND m.nume = 'The Girl Is Mine' AND al.nume = 'Thriller';

--melodie Dont Let the Sun Go Down on Me
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Melodie despre nevoia de ajutor in momente grele'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Elton John' AND m.nume = 'Dont Let the Sun Go Down on Me' AND al.nume = 'Duets';

INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Reinterpretare in anul 1991'
FROM artist a, album al, melodie m  
WHERE a.nume = 'George Michael' AND m.nume = 'Dont Let the Sun Go Down on Me' AND al.nume = 'Duets';

--melodie Ebony and Ivory
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'An debut melodie 1982'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Paul McCartney' AND m.nume = 'Ebony and Ivory' AND al.nume = 'Tug of War';

INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Melodia promoveaza unitatea si egalitatea rasiala'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Stevie Wonder' AND m.nume = 'Ebony and Ivory' AND al.nume = 'Tug of War';

--melodie Beat It
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Hit international cu numeroase premii'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Michael Jackson' AND m.nume = 'Beat It' AND al.nume = 'Thriller';


--melodie Billie Jean
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Cunoscuta pentru linia de bas distincta'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Michael Jackson' AND m.nume = 'Billie Jean' AND al.nume = 'Thriller';

--melodie Dont Go Breaking My Heart
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Colaborare cu Kiki Dee'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Elton John' AND m.nume = 'Dont Go Breaking My Heart' AND al.nume = 'Duets';

--melodia Sir Duke
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Melodia aduce un omagiu lui Duke Ellington'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Stevie Wonder' AND m.nume = 'Sir Duke' AND al.nume = 'Songs in the Key of Life';

--melodie Take It Away
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Colaborarea cu bateristul Ringo Star'
FROM artist a, album al, melodie m  
WHERE a.nume = 'Paul McCartney' AND m.nume = 'Take It Away' AND al.nume = 'Tug of War';

--melodie One More Try
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Abordarea temei de iubire si regret'
FROM artist a, album al, melodie m  
WHERE a.nume = 'George Michael' AND m.nume = 'One More Try' AND al.nume = 'Faith';

--melodie Faith
INSERT INTO detaliimelodie (id_artist, id_album, id_melodie, detalii)
SELECT a.id_artist, al.id_album, m.id_melodie, 'Imens succes comercial'
FROM artist a, album al, melodie m  
WHERE a.nume = 'George Michael' AND m.nume = 'Faith' AND al.nume = 'Faith';



--UTILIZATOR
INSERT INTO utilizator VALUES (null, 'Ana-Maria Popa', 'MyP@ssw0rd@', 'ana-popa1989@gmail.com'); --1
INSERT INTO utilizator VALUES (null, 'George Minu', 'Minutzu%1969', 'george_minutzu69@yahoo.com'); --2
INSERT INTO utilizator VALUES (null, 'Mihai Constantin', 'Mihaita!Con22', 'mihai.const2000@outlook.com'); --3
INSERT INTO utilizator VALUES (null, 'Andreea Ionescu', 'Andre$Ionescu123', 'ady_andreea_ionescu@yahoo.com'); --4
INSERT INTO utilizator VALUES (null, 'Gica Petrica', 'gicaGica#000', 'gica_petri@gmail.com'); --5
INSERT INTO utilizator VALUES (null, 'Mihaela Poraicu', 'miHaP##123', 'mihaaa_poraicu@gmail.com'); --6
INSERT INTO utilizator VALUES (null, 'Maria Bonaparte', 'Maryyyyy123@', 'maryMary78@yahoo.com'); --7

--BIBLIOTECA UTILIZATORI
--pt melodia Dont Let the Sun Go Down on Me ---X3
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 1.10
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Ana-Maria Popa' AND m.nume = 'Dont Let the Sun Go Down on Me';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.00
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'George Minu' AND m.nume = 'Dont Let the Sun Go Down on Me';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 0.20
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Gica Petrica' AND m.nume = 'Dont Let the Sun Go Down on Me';

--pt melodia Ebony and Ivory ---X4
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 0.20
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Gica Petrica' AND m.nume = 'Ebony and Ivory';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 3.20
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'George Minu' AND m.nume = 'Ebony and Ivory';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 0.40
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Mihai Constantin' AND m.nume = 'Ebony and Ivory';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 5.00
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Andreea Ionescu' AND m.nume = 'Ebony and Ivory';



--pt melodia The Girl Is Mine X2
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 0.20
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Ana-Maria Popa' AND m.nume = 'The Girl Is Mine';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 0.40
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Mihai Constantin' AND m.nume = 'The Girl Is Mine';

--pt melodia Beat It ---X5
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 3.90
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Ana-Maria Popa' AND m.nume = 'Beat It';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.80
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'George Minu' AND m.nume = 'Beat It';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 5.00
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Mihai Constantin' AND m.nume = 'Beat It';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 0.65
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Andreea Ionescu' AND m.nume = 'Beat It';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 1.25
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Gica Petrica' AND m.nume = 'Beat It';

--pt melodia Billie Jean ---X3
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.35
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Gica Petrica' AND m.nume = 'Billie Jean';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.05
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'George Minu' AND m.nume = 'Billie Jean';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 2.25
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Andreea Ionescu' AND m.nume = 'Billie Jean';

--pt melodia Dont Go Breaking My Heart --X3
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.70
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Ana-Maria Popa' AND m.nume = 'Dont Go Breaking My Heart';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.00
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Mihai Constantin' AND m.nume = 'Dont Go Breaking My Heart';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 3.95
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Gica Petrica' AND m.nume = 'Dont Go Breaking My Heart';

--pt melodia Sir Duke --X4
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 0.95
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Gica Petrica' AND m.nume = 'Sir Duke';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 5.00
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'George Minu' AND m.nume = 'Sir Duke';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 1.35
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Ana-Maria Popa' AND m.nume = 'Sir Duke';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 3.00
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Andreea Ionescu' AND m.nume = 'Sir Duke';

--pt melodia Take It Away --X2
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.00
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Andreea Ionescu' AND m.nume = 'Take It Away';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.60
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Mihai Constantin' AND m.nume = 'Take It Away';

--pt melodia One More Try ---X2
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.65
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Mihai Constantin' AND m.nume = 'One More Try';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.25
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Ana-Maria Popa' AND m.nume = 'One More Try';

--pt melodia Faith ---X3
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 3.90
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'George Minu' AND m.nume = 'Faith';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 4.90
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Andreea Ionescu' AND m.nume = 'Faith';

INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 5.00
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Gica Petrica' AND m.nume = 'Faith';



--GEN MUZICAL
INSERT INTO genmuzical VALUES (null, 'POP','Cel mai ascultat gen muzical de tineri'); --POP
INSERT INTO genmuzical VALUES (null, 'Soft Rock','Un rock mai linistit ar spune unii');--Soft Rock
INSERT INTO genmuzical VALUES (null, 'R and B','Plin de suflet, emotiv si ritmic'); --R&B
INSERT INTO genmuzical VALUES (null, 'Soul','Expresiv, pasional si inradacinat in emotie'); --Soul
INSERT INTO genmuzical VALUES (null, 'Rock','Acest gen muzical te va baga in priza'); --Rock
INSERT INTO genmuzical VALUES (null, 'Hard Rock',null); --Hard Rock
INSERT INTO genmuzical VALUES (null, 'Funk','Groovy si numai bun de dans'); --Funk
INSERT INTO genmuzical VALUES (null, 'Disco',null); --Disco
INSERT INTO genmuzical VALUES (null, 'Adult Contemporary','Pentru cei cu suflet matur'); --Adult Contemporary




--DETALII GENURI

--Dont Let the Sun Go Down on Me
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Dont Let the Sun Go Down on Me'), 9, 'Ritmat');

INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Dont Let the Sun Go Down on Me'), 2,'O auditie minunata');

--Ebony and Ivory
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Ebony and Ivory'), 1,null);

--The Girl Is Mine
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'The Girl Is Mine'), 3,null);

INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'The Girl Is Mine'), 4,null);

--Beat It
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Beat It'),5 ,null);

INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Beat It'), 6,'Electrizant');

--Billie Jean
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Billie Jean'), 7,'Dansant');

--Dont Go Breaking My Heart 
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Dont Go Breaking My Heart'), 8,null);

INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Dont Go Breaking My Heart'), 2,null);

--Sir Duke
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Sir Duke'), 7,null);

--Take It Away
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'Take It Away'), 5,'Te readuce la viata');

--One More Try
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'One More Try'),9,'Un stil lin si polisat');

--Faith 
INSERT INTO detaliigenuri (genmuzical_id_gen_muzical, melodie_id_melodie, descriere)
VALUES ((SELECT id_melodie FROM melodie WHERE nume = 'One More Try'), 3,'Un stil captivant');


--calculare unui rating mediu auziliar pentru fiecare melodie pe baza notelor date de utilizatori 
SELECT 
    bu.id_melodie,
    m.nume AS melodie,
    AVG(bu.nota) AS nota_medie
FROM bilbiotecautilizator bu
JOIN melodie m ON bu.id_melodie = m.id_melodie
GROUP BY bu.id_melodie, m.nume;

--actualizarea rating din tablea rating pentru fiecare melodie
UPDATE ratingmelodie
SET rating = (
    SELECT COALESCE(AVG(bu.nota), 0)
    FROM bilbiotecautilizator bu
    WHERE bu.id_melodie = ratingmelodie.id_melodie
);


--determinare numar voturi pentru fiecare melodie pe baza inregistrarilor in biblioteca utilizator
SELECT
    m.id_melodie,
    m.nume AS melodie,
    COUNT(bu.id_biblioteca_utilizator) AS numar_voturi
FROM
    melodie m
LEFT JOIN
    bilbiotecautilizator bu ON m.id_melodie = bu.id_melodie
GROUP BY
    m.id_melodie, m.nume
ORDER BY
    m.id_melodie;


//SELECT * FROM artist;
//SELECT * FROM album;
//SELECT * FROM melodie;
//SELECT * FROM ratingmelodie;
//SELECT * FROM utilizator;
//SELECT * FROM bilbiotecautilizator;
//SELECT * FROM genmuzical;
//SELECT * FROM detaliigenuri;
//SELECT * FROM detaliimelodie;