CREATE TABLE IF NOT EXISTS `Userinformation` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `MSISDN/Number` FLOAT DEFAULT NULL,
    `sessions frequency` INT DEFAULT NULL,
    `Dur. (ms)` FLOAT DEFAULT NULL,
    `Total DL (Bytes)` FLOAT DEFAULT NULL,
    `Total UL (Bytes)` FLOAT DEFAULT NULL,
    `Avg RTT DL (ms)` FLOAT DEFAULT NULL,
    `Avg RTT UL (ms)` FLOAT DEFAULT NULL,
    `Handset Type` TEXT DEFAULT NULL,
    `Avg Bearer TP DL (kbps)` FLOAT DEFAULT NULL,
    `Avg Bearer TP UL (kbps)` FLOAT DEFAULT NULL,
    `Social Media Total (Bytes)` FLOAT DEFAULT NULL,
    `Google Total (Bytes)` FLOAT DEFAULT NULL,
    `Email Total (Bytes)` FLOAT DEFAULT NULL,
    `Youtube Total (Bytes)` FLOAT DEFAULT NULL,
    `Netflix Total (Bytes)` FLOAT DEFAULT NULL,
    `Gaming Total (Bytes)` FLOAT DEFAULT NULL,
    `Other Total (Bytes)` FLOAT DEFAULT NULL,
    `Engagement scores` FLOAT DEFAULT NULL,
    `Experience scores` FLOAT DEFAULT NULL,
    `Satisfaction scores` FLOAT DEFAULT NULL,
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
