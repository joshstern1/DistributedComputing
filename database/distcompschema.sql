-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

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
  `userID` INT(11) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `credits` INT(11) NOT NULL DEFAULT 0,
  `hardwareRating` INT(11) NULL DEFAULT NULL,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) INVISIBLE,
  UNIQUE INDEX `userID_UNIQUE` (`userID` ASC) VISIBLE,
  PRIMARY KEY (`userID`))
ENGINE = InnoDB
AUTO_INCREMENT = 52
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `distcompschema`.`executables`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `distcompschema`.`executables` (
  `executableID` INT(11) NOT NULL,
  `userID` INT(11) NOT NULL,
  `executableName` VARCHAR(45) NOT NULL,
  `executable` MEDIUMBLOB NOT NULL,
  `result` MEDIUMBLOB NULL DEFAULT NULL,
  PRIMARY KEY (`executableID`),
  UNIQUE INDEX `executableID_UNIQUE` (`executableID` ASC) VISIBLE,
  CONSTRAINT `userID_key`
    FOREIGN KEY (`userID`)
    REFERENCES `distcompschema`.`user` (`userID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
