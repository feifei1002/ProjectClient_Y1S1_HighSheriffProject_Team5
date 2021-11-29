DROP TABLE IF EXISTS Donators;
DROP TABLE IF EXISTS Applicants;
DROP TABLE IF EXISTS Questions;

CREATE TABLE IF NOT EXISTS `Donators` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `firstName`	TEXT NOT NULL,
  `surName`	TEXT NOT NULL,
  `Amount`  numeric,
  `Email` TEXT NOT NULL,
  `Reason` TEXT NOT NULL
);

INSERT INTO 'Donators'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Fei','Liu',5000, 'LiuF29@cardiff.ac.uk', 'bla bla bla');
INSERT INTO 'Donators'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Peter','Hayward',4000, 'haywardpj@cardiff.ac.uk', 'bla bla bla');
INSERT INTO 'Donators'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Jashan','Vigneswaran',3000, 'vigneswaranj@cardiff.ac.uk', 'bla bla bla');


CREATE TABLE IF NOT EXISTS `Applicants` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `firstName`	TEXT NOT NULL,
  `surName`	TEXT NOT NULL,
  `Amount`  numeric,
  `Email` TEXT NOT NULL,
  `Reason` TEXT NOT NULL
);

INSERT INTO 'Applicants'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Fei','Liu',5000, 'LiuF29@cardiff.ac.uk', 'bla bla bla');
INSERT INTO 'Applicants'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Gianfranco','Cicciomessere',2000, 'cicciomessereg@cardiff.ac.uk', 'bla bla bla');
INSERT INTO 'Applicants'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Stevens','Matthew',1000, 'stevensm7@cardiff.ac.uk', 'bla bla bla');

CREATE TABLE IF NOT EXISTS `Questions` (
  `ID`   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `Question` TEXT NOT NULL
);

INSERT INTO 'Questions' ('Question') VALUES ('What is your favourite animal?');
INSERT INTO 'Questions' ('Question') VALUES ('What is your favourite colour?')
