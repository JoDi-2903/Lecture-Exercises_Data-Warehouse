/* 
 * DHBW Stuttgart | Data Warehouse | Semester 5
 * ********************************************
 * Autor:            Jonathan Diebel
 * Erstelldatum:     04.11.2022
 */
 
INSERT INTO staging.kunde (kunde_id, vorname, nachname, anrede, geschlecht, geburtsdatum, wohnort, quelle)
VALUES (493744, 'Bernhard', 'Leis', 'Herr', 'männlich', to_date('27.09.1951', 'DD.MM.YYYY'), 3, 'CRM');

INSERT INTO staging.fahrzeug (fin, kunde_id, baujahr, modell, quelle)
VALUES ('WPOSJYDU7SDO692GB', 493744, 2021, '911 Carrera 4', 'Fahrzeug DB');

INSERT INTO staging.kfzzuordnung (fin, kfz_kennzeichen, quelle)
VALUES ('WPOSJYDU7SDO692GB', 'HN-BL 1951', 'Fahrzeug DB');