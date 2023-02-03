TRUNCATE TABLE SONGS;

ALTER SEQUENCE songs_id_seq RESTART WITH 1;

INSERT INTO songs(title, artist, key, tempo) 
VALUES('Crazy In Love', 'Beyoncé', 'D-', 100);
INSERT INTO songs(title, artist, key, tempo) 
VALUES('How Deep Is Your Love', 'Bee Gees', 'Eb', 105);
INSERT INTO songs(title, artist, key, tempo) 
VALUES('Watermelon Sugar', 'Harry Style', 'C', 95);