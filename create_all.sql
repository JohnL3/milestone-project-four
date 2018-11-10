-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Table `category_table`
-- -----------------------------------------------------
CREATE TABLE `category_table` (
  `cat_id` INT(11) NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`cat_id`),
  UNIQUE INDEX `category_name_UNIQUE` (`category_name` ) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `author_table`
-- -----------------------------------------------------
CREATE TABLE `author_table` (
  `author_id` INT(11) NOT NULL AUTO_INCREMENT,
  `author_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`author_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_table`
-- -----------------------------------------------------
CREATE TABLE `user_table` (
  `user_id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(100) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_name_UNIQUE` (`user_name` ) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipe_table`
-- -----------------------------------------------------
CREATE TABLE `recipe_table` (
  `recipe_id` INT(11) NOT NULL AUTO_INCREMENT,
  `recipe_name` VARCHAR(100) NOT NULL,
  `Nuts` CHAR(1) NOT NULL DEFAULT 'F',
  `Egg` CHAR(1) NOT NULL DEFAULT 'F',
  `Milk` CHAR(1) NOT NULL DEFAULT 'F',
  `Pnuts` CHAR(1) NOT NULL DEFAULT 'F',
  `Celery` CHAR(1) NOT NULL DEFAULT 'F',
  `Mustard` CHAR(1) NOT NULL DEFAULT 'F',
  `SSeeds` CHAR(1) NOT NULL DEFAULT 'F',
  `Fish` CHAR(1) NOT NULL DEFAULT 'F',
  `Moll` CHAR(1) NOT NULL DEFAULT 'F',
  `SBeans` CHAR(1) NOT NULL DEFAULT 'F',
  `Lupin` CHAR(1) NOT NULL DEFAULT 'F',
  `SDioxide` CHAR(1) NOT NULL DEFAULT 'F',
  `Cerals` CHAR(1) NOT NULL DEFAULT 'F',
  `Crust` CHAR(1) NOT NULL DEFAULT 'F',
  `instructions` BLOB NOT NULL,
  `likes` SMALLINT(5) NULL DEFAULT 0,
  `collected` SMALLINT(5) NULL DEFAULT 0,
  `prep` VARCHAR(45) NULL,
  `cook` VARCHAR(45) NULL,
  `serves` SMALLINT(3) NULL,
  `url` VARCHAR(100) NOT NULL,
  `cat_id` INT(11) NOT NULL,
  `author_id` INT(11) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`recipe_id`),
  UNIQUE INDEX `recipe_id_UNIQUE` (`recipe_id` ) ,
  INDEX `cat_ndx` (`cat_id` ) ,
  INDEX `fk_recipe_table_author_table1_idx` (`author_id` ) ,
  INDEX `fk_recipe_table_user_table1_idx` (`user_id` ) ,
  CONSTRAINT `category`
    FOREIGN KEY (`cat_id`)
    REFERENCES `category_table` (`cat_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `author`
    FOREIGN KEY (`author_id`)
    REFERENCES `author_table` (`author_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `user`
    FOREIGN KEY (`user_id`)
    REFERENCES `user_table` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_collects_recipes`
-- -----------------------------------------------------
CREATE TABLE `user_collects_recipes` (
  `user_table_user_id` INT(11) NOT NULL,
  `recipe_table_recipe_id` INT(11) NOT NULL,
  PRIMARY KEY (`user_table_user_id`, `recipe_table_recipe_id`),
  INDEX `fk_user_table_has_recipe_table1_recipe_table1_idx` (`recipe_table_recipe_id` ) ,
  INDEX `fk_user_table_has_recipe_table1_user_table1_idx` (`user_table_user_id` ) ,
  CONSTRAINT `fk_user_table_has_recipe_table1_user_table1`
    FOREIGN KEY (`user_table_user_id`)
    REFERENCES `user_table` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_table_has_recipe_table1_recipe_table1`
    FOREIGN KEY (`recipe_table_recipe_id`)
    REFERENCES `recipe_table` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ingredients_table`
-- -----------------------------------------------------
CREATE TABLE `ingredients_table` (
  `recipe_id` INT(11) NOT NULL,
  `ing_name` VARCHAR(45) NOT NULL,
  `ing_quantity` VARCHAR(45) NULL,
  INDEX `recipe_idx` (`recipe_id` ) ,
  CONSTRAINT `recipe`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipe_table` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE `Likes` (
  `user_name` VARCHAR(100) NOT NULL,
  `recipe_id` INT(11) NOT NULL,
  UNIQUE INDEX `recipe_id_UNIQUE` (`recipe_id`, `user_name`))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
