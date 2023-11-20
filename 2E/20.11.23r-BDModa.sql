DROP DATABASE IF EXISTS SalonMody;

CREATE DATABASE SalonMody;

USE SalonMody;
DROP DATABASE IF EXISTS Kreacja;
DROP DATABASE IF EXISTS Material;
DROP DATABASE IF EXISTS Stroj;
CREATE TABLE Stroj (
    idStroj INT PRIMARY KEY AUTO_INCREMENT,
    nazwaStroj VARCHAR(255),
    dataUtworzenia DATE,
    dataWaznosci DATE,
    firma VARCHAR(255),
    wlasciciel VARCHAR(255)
);

CREATE TABLE Material (
    idMaterial INT PRIMARY KEY AUTO_INCREMENT,
    nazwaMaterial VARCHAR(255),
    kategoria VARCHAR(100),
    kolor VARCHAR(100),
    rozmiar VARCHAR(1)
);

CREATE TABLE Kreacja (
    idKreacja INT PRIMARY KEY AUTO_INCREMENT,
    idStroj INT,
    idMaterial INT,
    FOREIGN KEY (idStroj) REFERENCES Stroj(idStroj),
    FOREIGN KEY (idMaterial) REFERENCES Material(idMaterial),
    dataUtworzenia DATE
);

INSERT INTO Stroj VALUES(NULL,"Wieczorowy", "2023-11-20", "2023-12-20", "T19", "Bartosz");
INSERT INTO Stroj VALUES(NULL,"Skatowy", "2023-11-19", "2023-12-24", "Skatepark", "Wojciech");
INSERT INTO Stroj VALUES(NULL,"Casualowy", "2023-11-20", "2024-1-20", "Marks", "Ala");
INSERT INTO Stroj VALUES(NULL,"Biurowy", "2023-11-17", "2023-12-4", "Gohs", "Magda");

INSERT INTO Material VALUES(NULL,"Bluzka", "MSztuczne", "Czerwony", "S");
INSERT INTO Material VALUES(NULL,"Spodnie", "MNaturalne", "Biały", "M");
