DROP TABLE IF EXISTS Donators;
DROP TABLE IF EXISTS Applicants;

CREATE TABLE IF NOT EXISTS `Donators` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `firstName`	TEXT NOT NULL,
  `surName`	TEXT NOT NULL,
  `Amount`  numeric
);

INSERT INTO 'Donators'('firstName','surName', 'Amount' ) VALUES ('Fei','Liu',5000);
INSERT INTO 'Donators'('firstName','surName', 'Amount' ) VALUES ('Peter','Hayward',4000);
INSERT INTO 'Donators'('firstName','surName', 'Amount' ) VALUES ('Jashan','Vigneswaran',3000);


CREATE TABLE IF NOT EXISTS `Applicants` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `firstName`	TEXT NOT NULL,
  `surName`	TEXT NOT NULL,
  `Amount`  numeric
);

INSERT INTO 'Applicants'('firstName','surName', 'Amount' ) VALUES ('Fei','Liu',5000);
INSERT INTO 'Applicants'('firstName','surName', 'Amount' ) VALUES ('Gianfranco','Cicciomessere',2000);
INSERT INTO 'Applicants'('firstName','surName', 'Amount' ) VALUES ('Stevens','Matthew',2000);
