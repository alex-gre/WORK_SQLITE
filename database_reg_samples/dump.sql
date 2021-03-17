PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE  `reg` (
	`id` integer PRIMARY KEY AUTOINCREMENT,
	`login` VARCHAR(35),
	`password` VARCHAR(35), 
        `info` TEXT);

INSERT INTO `reg` VALUES(NULL,'loh','111',NULL);
INSERT INTO `reg` VALUES(NULL,'loh2','111','other text');
INSERT INTO `reg` VALUES(NULL,'wew','232dsd','hernija');

COMMIT;
