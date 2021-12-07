DROP TABLE IF EXISTS Donators;
DROP TABLE IF EXISTS Applicants;

CREATE TABLE IF NOT EXISTS `Donators` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `Amount`	numeric NOT NULL,
  `Name`	TEXT NOT NULL,
  `Card` numeric NOT NULL,
  `Expiry` numeric NOT NULL,
  `Security` numeric NOT NULL
);

 --INSERT INTO 'Donators'('Amount', 'Name', 'Card', 'Expiry', 'Security' ) VALUES


-- CREATE TABLE IF NOT EXISTS `Applicants` (
--   `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--   `firstName`	TEXT NOT NULL,
--   `surName`	TEXT NOT NULL,
--   `Amount` numeriC NOT NULL ,
--   `Email ` TEXT NOT NULL,
--   `Reason` TEXT NOT NULL
-- );
--
-- INSERT INTO 'Applicants'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Fei','Liu',5000, 'LiuF29@cardiff.ac.uk', 'bla bla bla');
-- INSERT INTO 'Applicants'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Gianfranco','Cicciomessere',2000, 'cicciomessereg@cardiff.ac.uk', 'bla bla bla');
-- INSERT INTO 'Applicants'('firstName','surName', 'Amount', 'Email', 'Reason' ) VALUES ('Stevens','Matthew',1000, 'stevensm7@cardiff.ac.uk', 'bla bla bla');
