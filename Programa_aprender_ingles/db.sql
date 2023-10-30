CREATE TABLE palabras(id Serial, palabra text, traduccion text);

INSERT INTO palabras(palabra, traduccion) VALUES ('Run', 'Correr');

INSERT INTO palabras(palabra, traduccion) VALUES ('Jump', 'Saltar');

select * from palabras;