CREATE DATABASE hindu_db;
USE hindu_db;


CREATE TABLE IF NOT EXISTS `hindu` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` TEXT NOT NULL,
    `link` TEXT NOT NULL,
    `date` DATE NOT NULL,
    PRIMARY KEY (`id`),
    FULLTEXT (`title`),
    FULLTEXT (`link`)
    )ENGINE=InnoDB;
