--------------------------------VIZUALIAZRE--------------------------------

--afisare artisti
SELECT * FROM artist;

-- afisare melodii in functie de un gen muzical specific (exemplu: 'POP')
SELECT m.nume, g.nume AS gen_muzical
FROM melodie m
JOIN detaliigenuri d ON m.id_melodie = d.melodie_id_melodie
JOIN genmuzical g ON d.genmuzical_id_gen_muzical = g.id_gen_muzical
WHERE g.nume = 'POP';

--afisare pentru toti artistii, albumele si melodiile corespunzatoare albumelelor
SELECT ar.nume AS nume_artist, a.nume AS nume_album, m.nume AS nume_melodie
FROM artist ar
JOIN detaliimelodie da ON ar.id_artist = da.id_artist
JOIN album a ON da.id_album = a.id_album
JOIN melodie m ON da.id_melodie = m.id_melodie;

--afisare melodii in care canta doi artisti si melodia propriu-zisa
SELECT DISTINCT a1.nume AS artist1, a2.nume AS artist2, m.nume AS melodie
FROM artist a1
JOIN detaliimelodie da1 ON a1.id_artist = da1.id_artist
JOIN melodie m ON da1.id_melodie = m.id_melodie
JOIN detaliimelodie da2 ON m.id_melodie = da2.id_melodie
JOIN artist a2 ON da2.id_artist = a2.id_artist
WHERE a1.id_artist < a2.id_artist;

--------------------------------UPDATE-------------------------------------

--update un email la un utlizator in functie de numele utilizatorului
UPDATE utilizator
SET email = 'minu_Geo@yahoo.com'
WHERE nume = 'George Minu';
SELECT * FROM utilizator;


/*PUS IN SCRIPT DE INSERARE 
--update pentru rating pe baza notelor utilizatorilor 
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
*/

--afisare nume melodie si rating
SELECT 
    m.nume AS melodie,
    rm.rating
FROM ratingmelodie rm
JOIN melodie m ON rm.id_melodie = m.id_melodie;


/*
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
*/

-------------------ADAUGARE--------------------------------

--adaugare coloane pentru sex in utilizator 
ALTER TABLE utilizator
ADD sex VARCHAR2(10);
UPDATE utilizator
SET sex = CASE WHEN id_utilizator = 1 THEN 'F' ELSE 'Nespecificat' END
WHERE id_utilizator = 1;

SELECT * FROM utilizator;


----------------STERGERE------------------------------

--stergere coloane pentru sex in utilizator 
ALTER TABLE utilizator
DROP COLUMN sex;

SELECT * FROM utilizator;

--stergere utilizatori care nu au inregistrari in biblioteca utilizatori
SELECT * FROM utilizator;

DELETE FROM utilizator u
WHERE NOT EXISTS (
    SELECT 1
    FROM bilbiotecautilizator bu
    WHERE bu.id_utilizator = u.id_utilizator
);

SELECT * FROM utilizator;

--stergere utilizator care are inregistrari in biblioteca utilizator
DELETE FROM bilbiotecautilizator
WHERE id_utilizator = 1;

DELETE FROM utilizator
WHERE id_utilizator = 1;

-------------VERIFICARE CONSTRANGERI-----------------

--pt utilizator
INSERT INTO utilizator VALUES (null, '2Mihai Gica', 'misu1G22@', 'maryMary78@yahoo.com');-- pt nume  
INSERT INTO utilizator VALUES (null, 'Mihai Gica', 'mi@', 'maryMary78@yahoo.com');-- pt parola
INSERT INTO utilizator VALUES (null, 'Mihai Gica', 'misu1G2222@', 'maryMary78yahoo.com');-- pt nume  

--pt biblioteca utilizator
INSERT INTO bilbiotecautilizator (id_biblioteca_utilizator, id_utilizator, id_melodie, nota)
SELECT null, u.id_utilizator, m.id_melodie, 9
FROM utilizator u
CROSS JOIN melodie m
WHERE u.nume = 'Ana-Maria Popa' AND m.nume = 'Dont Let the Sun Go Down on Me';

--pt gen muzica
INSERT INTO genmuzical VALUES (null, '@',null);

--pt melodie
INSERT INTO album VALUES (null, '****');

--pt artist
INSERT INTO artist VALUES (null,'#####');

--pt album
INSERT INTO album VALUES (null, '###'); 
