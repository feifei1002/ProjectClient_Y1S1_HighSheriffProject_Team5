DROP TABLE IF EXISTS Donators;
DROP TABLE IF EXISTS Applicants;

CREATE TABLE IF NOT EXISTS `Donators` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `firstName`	TEXT NOT NULL,
  `surName`	TEXT NOT NULL,
  `Amount`  numeric
);

-- Look at the quotes They are different on each line.  See https://sqlite.org/lang_keywords.html
INSERT INTO 'Donators'('firstName','surName', 'Amount' ) VALUES ('Fei','Liu',5000);
INSERT INTO 'Donators'('firstName','surName', 'Amount' ) VALUES ('Fei','Liu',1000);

CREATE TABLE IF NOT EXISTS `Applicants` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `firstName`	TEXT NOT NULL,
  `surName`	TEXT NOT NULL,
  `Amount`  numeric
);

-- Look at the quotes They are different on each line.  See https://sqlite.org/lang_keywords.html
INSERT INTO 'Applicants'('firstName','surName', 'Amount' ) VALUES ('Fei','Liu',5000);
INSERT INTO 'Applicants'('firstName','surName', 'Amount' ) VALUES ('Fei','Liu',1000);
