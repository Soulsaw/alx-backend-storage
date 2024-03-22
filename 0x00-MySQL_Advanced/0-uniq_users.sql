-- This script create a users table with a requirements
CREATE TABLE IF NOT EXISTS `users`
(
	`id` int NOT NULL AUTO_INCREMENT,
	`email` varchar(256) NOT NULL,
	`name` varchar(256),
	PRIMARY KEY(`id`),
	UNIQUE(`email`)
);
