DROP TABLE IF EXISTS `verseny_feladat`;
DROP TABLE IF EXISTS `feladat`;
DROP TABLE IF EXISTS `upload`;
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `teams`;
DROP TABLE IF EXISTS `roles`;
DROP TABLE IF EXISTS `verseny`;


CREATE TABLE `verseny` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `kezdet` INT NOT NULL,
    `veg` INT NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `roles` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `display_name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (`name`)
);

CREATE TABLE `teams` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `team_name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `verseny_id` INT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`verseny_id`) REFERENCES `verseny`(`id`),
    UNIQUE (`team_name`)
);

CREATE TABLE `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `digest` VARCHAR(255) NOT NULL,
    `role_id` INT NOT NULL,
    `evfolyam` INT,
    `osztaly` VARCHAR(1),
    `team_id` INT,
    PRIMARY KEY (`id`),
    UNIQUE (`username`),
    FOREIGN KEY (`role_id`) REFERENCES `roles`(`id`),
    FOREIGN KEY (`team_id`) REFERENCES `teams`(`id`)
);

CREATE TABLE `upload` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `feladat` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `data` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `number` INT NOT NULL,
    `upload_id` INT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`upload_id`) REFERENCES `upload`(`id`)
);


CREATE TABLE `verseny_feladat` (
    `verseny_id` INT NOT NULL,
    `feladat_id` INT NOT NULL,
    FOREIGN KEY (`verseny_id`) REFERENCES `verseny`(`id`),
    FOREIGN KEY (`feladat_id`) REFERENCES `feladat`(`id`)
);

INSERT INTO `verseny`(`kezdet`, `veg`)
VALUES (
        1699696112,
        1700000000
       ),(
        1709696112,
        1705000000
       );

INSERT INTO `teams`(`team_name`, `description`, `verseny_id`)
VALUES
    ('Csapat1', 'CS', 1),
    ('Csapat2', 'CS', 2),
    ('Csapat4', 'CS', 1)
;

INSERT INTO `roles`(`name`, `display_name`)
VALUES
    ('ADMIN', 'Webmester'),
    ('TANAR', 'Tanár'),
    ('DIAK', 'Diák'),
    ('ZSURI', 'Zsűri');

INSERT INTO `users`(`username`, `digest`, `role_id`, `team_id`)
VALUES
    (
     -- password: admin
     'admin',
     'scrypt:32768:8:1$cREfsjByVMKJGCjm$0e126590b1637bf7e918fc793c9a11e46a6426b6aa514f9371ad500195fc1a069adec215968be956fa2144fa1c55f97c4ce0a1972be49424eae06e9ed5bc87f2',
     1,
     NULL
    ),
    (
     -- password: user
     'user',
     'scrypt:32768:8:1$dnrbg8IX6U47POC0$ee35dd8aa822783b17c9ef1b18fd887c13495eb3c80ac8da47b770941d1bb289af6eebd131b5c22643539353001cfa04b1037f50a1567dc27525cf18884a8aab',
     3,
     1
    ),
    (
     -- password: user
     'user2',
     'scrypt:32768:8:1$dnrbg8IX6U47POC0$ee35dd8aa822783b17c9ef1b18fd887c13495eb3c80ac8da47b770941d1bb289af6eebd131b5c22643539353001cfa04b1037f50a1567dc27525cf18884a8aab',
     3,
     1
    ),
    (
     -- password: user
     'user3',
     'scrypt:32768:8:1$dnrbg8IX6U47POC0$ee35dd8aa822783b17c9ef1b18fd887c13495eb3c80ac8da47b770941d1bb289af6eebd131b5c22643539353001cfa04b1037f50a1567dc27525cf18884a8aab',
     3,
     1
    )
    ;

INSERT INTO `upload`(`user_id`)
VALUES (1), (2), (1);

INSERT INTO `feladat`(`data`, `number`, `upload_id`)
VALUES ('egy feladat kell ide', 6, 1),
    ('még egy jó lenne', 5, 1),
    ('kellene nekem még sok', 7, 1),
    ('lorem ipsum dolor sit', 7, 2),
    ('amit in caeli con', 5, 3),
    ('terra et in convo', 8, 3);

INSERT INTO `verseny_feladat`(`verseny_id`, `feladat_id`)
VALUES (1, 2),
       (1, 5),
       (1, 3),
       (2, 1),
       (2, 2),
       (2, 5);
