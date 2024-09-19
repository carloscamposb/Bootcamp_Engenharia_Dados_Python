-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`d_departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`d_departamento` (
  `idDepartamento` INT NULL,
  `d_departamento_nome` VARCHAR(45) NOT NULL,
  `d_departamento_campus` VARCHAR(45) NOT NULL,
  `d_departamento_andar` VARCHAR(45) NOT NULL,
  `d_departamento_area_de_estudo` VARCHAR(45) NOT NULL,
  `d_cargo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDepartamento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`d_disciplina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`d_disciplina` (
  `dd_idDisciplina` INT NOT NULL,
  `d_disciplina_tipo` VARCHAR(45) NOT NULL,
  `d_pré_requisito` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`dd_idDisciplina`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`d_Curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`d_Curso` (
  `d_idCurso` INT NOT NULL,
  `d_curso_nome` VARCHAR(45) NOT NULL,
  `d_curso_salario` VARCHAR(45) NULL,
  PRIMARY KEY (`d_idCurso`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`d_Datas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`d_Datas` (
  `d_idDatas` INT NOT NULL,
  `d_datas_inicio_aulas` DATETIME NOT NULL,
  `d_datas_final_aulas` DATETIME NOT NULL,
  `d_datas_dias_aulas` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`d_idDatas`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`f_Professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`f_Professor` (
  `sk_Professor` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `f_professor_data_nasc` DATE NOT NULL,
  `f_professor_sexo` CHAR(2) NOT NULL,
  `f_professor_cpf` VARCHAR(11) NOT NULL,
  `d_disciplina_dd_idDisciplina` INT NOT NULL,
  `d_departamento_idDepartamento` INT NOT NULL,
  `d_Curso_d_idCurso` INT NOT NULL,
  `d_Datas_d_idDatas` INT NOT NULL,
  PRIMARY KEY (`sk_Professor`),
  INDEX `fk_f_Professor_d_disciplina_idx` (`d_disciplina_dd_idDisciplina` ASC) VISIBLE,
  INDEX `fk_f_Professor_d_departamento1_idx` (`d_departamento_idDepartamento` ASC) VISIBLE,
  INDEX `fk_f_Professor_d_Curso1_idx` (`d_Curso_d_idCurso` ASC) VISIBLE,
  UNIQUE INDEX `cpf_UNIQUE` (`f_professor_cpf` ASC) VISIBLE,
  INDEX `fk_f_Professor_d_Datas1_idx` (`d_Datas_d_idDatas` ASC) VISIBLE,
  CONSTRAINT `fk_f_Professor_d_disciplina`
    FOREIGN KEY (`d_disciplina_dd_idDisciplina`)
    REFERENCES `mydb`.`d_disciplina` (`dd_idDisciplina`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_f_Professor_d_departamento1`
    FOREIGN KEY (`d_departamento_idDepartamento`)
    REFERENCES `mydb`.`d_departamento` (`idDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_f_Professor_d_Curso1`
    FOREIGN KEY (`d_Curso_d_idCurso`)
    REFERENCES `mydb`.`d_Curso` (`d_idCurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_f_Professor_d_Datas1`
    FOREIGN KEY (`d_Datas_d_idDatas`)
    REFERENCES `mydb`.`d_Datas` (`d_idDatas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
