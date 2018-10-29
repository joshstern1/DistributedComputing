-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema distcompschema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema distcompschema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `distcompschema` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `distcompschema` ;

-- -----------------------------------------------------
-- Table `distcompschema`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `distcompschema`.`user` (
  `userID` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `credits` INT(11) NOT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 51
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `distcompschema`.`lessoruser`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `distcompschema`.`lessoruser` (
  `userID` INT(11) NOT NULL,
  `numExecutables` INT(11) NOT NULL,
  PRIMARY KEY (`userID`),
  CONSTRAINT `userID`
    FOREIGN KEY (`userID`)
    REFERENCES `distcompschema`.`user` (`userID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `distcompschema`.`executables`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `distcompschema`.`executables` (
  `userID` INT(11) NOT NULL,
  `executableID` INT(11) NOT NULL,
  `executableName` VARCHAR(45) NOT NULL,
  `numThreads` INT(11) NOT NULL,
  `executable` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`userID`, `executableID`),
  CONSTRAINT `userID2`
    FOREIGN KEY (`userID`)
    REFERENCES `distcompschema`.`lessoruser` (`userID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `distcompschema`.`lesseeuser`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `distcompschema`.`lesseeuser` (
  `userID` INT(11) NOT NULL,
  `hardwareRating` INT(11) NOT NULL,
  PRIMARY KEY (`userID`),
  CONSTRAINT `userID4`
    FOREIGN KEY (`userID`)
    REFERENCES `distcompschema`.`user` (`userID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `distcompschema`.`threads`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `distcompschema`.`threads` (
  `userID` INT(11) NOT NULL,
  `executableID` INT(11) NOT NULL,
  `threadID` INT(11) NOT NULL,
  `threadName` VARCHAR(45) NOT NULL,
  `thread` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`userID`, `executableID`, `threadID`),
  CONSTRAINT `userID3`
    FOREIGN KEY (`userID` , `executableID`)
    REFERENCES `distcompschema`.`executables` (`userID` , `executableID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
