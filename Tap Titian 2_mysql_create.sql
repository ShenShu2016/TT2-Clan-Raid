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
	`MaxRaidAttacks` INT NOT NULL,
	`NumberParticipants` INT NOT NULL,
	`TotalTitanNumber` INT NOT NULL,
	PRIMARY KEY (`CSV_ID`)
);

CREATE TABLE `PersonalDetailPerCSV` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`PlayerCode` varchar(10) NOT NULL,
	`CSV_ID` INT NOT NULL,
	`RaidAttacks` INT NOT NULL,
	`EffectiveDMG` INT NOT NULL,
	`WrongDMG` INT NOT NULL,
	`EffectivePercentage` FLOAT NOT NULL,
	`AverageDMG` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `CSVRules` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`TitanNumber` INT NOT NULL,
	`TitanName` varchar(20) NOT NULL,
	`CSV_ID` INT NOT NULL,
	`ArmorHead` BOOLEAN NOT NULL,
	`ArmorTorso` BOOLEAN NOT NULL,
	`ArmorLeftArm` BOOLEAN NOT NULL,
	`ArmorRightArm` BOOLEAN NOT NULL,
	`ArmorLeftHand` BOOLEAN NOT NULL,
	`ArmorRightHand` BOOLEAN NOT NULL,
	`ArmorLeftLeg` BOOLEAN NOT NULL,
	`ArmorRightLeg` BOOLEAN NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `PersonalRankPerCSV` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`PlayerCode` varchar(10) NOT NULL,
	`CSV_ID` INT NOT NULL,
	`EffectiveDMG_Rank` INT NOT NULL,
	`EffectiveDMG_RankFromLast` INT NOT NULL,
	`RaidAttacks_RankFromLast` INT NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Clan` ADD CONSTRAINT `Clan_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);

ALTER TABLE `PlayerName` ADD CONSTRAINT `PlayerName_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);

ALTER TABLE `AttackDetail` ADD CONSTRAINT `AttackDetail_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);

ALTER TABLE `PersonalDetailPerCSV` ADD CONSTRAINT `PersonalDetailPerCSV_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);

ALTER TABLE `CSVRules` ADD CONSTRAINT `CSVRules_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);

ALTER TABLE `PersonalRankPerCSV` ADD CONSTRAINT `PersonalRankPerCSV_fk0` FOREIGN KEY (`CSV_ID`) REFERENCES `CSV`(`CSV_ID`);
