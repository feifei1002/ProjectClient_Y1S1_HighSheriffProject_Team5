DROP TABLE IF EXISTS Donators;
DROP TABLE IF EXISTS Applicants;
DROP TABLE IF EXISTS Tests;
DROP TABLE IF EXISTS reworkingApplicants;

CREATE TABLE IF NOT EXISTS `Donators` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `Amount`	TEXT NOT NULL,
  `Name`	TEXT NOT NULL,
  `Cardnumber`  TEXT NOT NULL,
  `Expirydate` TEXT NOT NULL,
  `security` TEXT NOT NULL
);


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

CREATE TABLE IF NOT EXISTS `Tests` (
  `ID`   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `Test` TEXT NOT NULL,
  `Answer` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `reworkingApplicants` (
  `ID`   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `firstName` TEXT NOT NULL,
  `surName` TEXT NOT NULL,
  `Email` TEXT NOT NULL,
  `Score` numeric
);
