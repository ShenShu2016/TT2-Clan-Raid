CREATE TABLE `Clan` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`PlayerCode` varchar(10) NOT NULL,
	`CSV_ID` INT NOT NULL,
	`Clan_Code` varchar(10),
	`Issuer` varchar(50),
	PRIMARY KEY (`id`)
);

CREATE TABLE `PlayerName` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`PlayerCode` varchar(10) NOT NULL,
	`PlayerName` varchar(50) NOT NULL,
	`CSV_ID` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `AttackDetail` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`PlayerCode` varchar(10) NOT NULL,
	`CSV_ID` INT NOT NULL,
	`TitanNumber` INT NOT NULL,
	`TitanName` varchar(20) NOT NULL,
	`TitanDamage` INT NOT NULL,
	`ArmorHead` INT NOT NULL,
	`ArmorTorso` INT NOT NULL,
	`ArmorLeftArm` INT NOT NULL,
	`ArmorRightArm` INT NOT NULL,
	`ArmorLeftHand` INT NOT NULL,
	`ArmorRightHand` INT NOT NULL,
	`ArmorLeftLeg` INT NOT NULL,
	`ArmorRightLeg` INT NOT NULL,
	`BodyHead` INT NOT NULL,
	`BodyTorso` INT NOT NULL,
	`BodyLeftArm` INT NOT NULL,
	`BodyRightArm` INT NOT NULL,
	`BodyLeftHand` INT NOT NULL,
	`BodyRightHand` INT NOT NULL,
	`BodyLeftLeg` INT NOT NULL,
	`BodyRightLeg` INT NOT NULL,
	`SkeletonHead` INT NOT NULL,
	`SkeletonTorso` INT NOT NULL,
	`SkeletonLeftArm` INT NOT NULL,
	`SkeletonRightArm` INT NOT NULL,
	`SkeletonLeftHand` INT NOT NULL,
	`SkeletonRightHand` INT NOT NULL,
	`SkeletonLeftLeg` INT NOT NULL,
	`SkeletonRightLeg` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `CSV` (
	`CSV_ID` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`Upload_TimeStamp` TIMESTAMP(6) NOT NULL UNIQUE,
	`Data` TEXT NOT NULL,
	`Issuer` varchar(50),
	`Raid_Finished_Date` TIMESTAMP,
	PRIMARY KEY (`CSV_ID`)
);

CREATE TABLE `PersonalDetailPerCSV` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`PlayerCode` varchar(10) NOT NULL,
	`CSV_ID` INT NOT NULL,
	`TotalRaidAttacks` INT NOT NULL,
	`TotalTitanNumber` INT NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Clan` ADD CONSTRAINT `Clan_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);

ALTER TABLE `PlayerName` ADD CONSTRAINT `PlayerName_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);

ALTER TABLE `AttackDetail` ADD CONSTRAINT `AttackDetail_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);

ALTER TABLE `PersonalDetailPerCSV` ADD CONSTRAINT `PersonalDetailPerCSV_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);
