-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 08, 2023 at 08:32 PM
-- Server version: 8.0.35-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.14

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webapp`
--
DROP DATABASE `dusza`;
CREATE DATABASE IF NOT EXISTS `dusza` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `dusza`;

-- --------------------------------------------------------

--
-- Table structure for table `feladat`
--

DROP TABLE IF EXISTS `feladat`;
CREATE TABLE IF NOT EXISTS `feladat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `number` int NOT NULL,
  `upload_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `upload_id` (`upload_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `feladat`
--

INSERT INTO `feladat` (`id`, `data`, `number`, `upload_id`) VALUES
(1, 'egy feladat kell ide', 6, 1),
(2, 'még egy jó lenne', 5, 1),
(3, 'kellene nekem még sok', 7, 1),
(4, 'lorem ipsum dolor sit', 7, 2),
(5, 'amit in caeli con', 5, 3),
(6, 'terra et in convo', 8, 3),
(7, 'alma körte banán mangó', 7, 4),
(8, 'krokodil aligátor gekkó gyík', 7, 4),
(9, 'feladatok kellenek még meke', 7, 5),
(10, 'sfd jlg lksjdf lksd', 7, 5),
(11, 'dfk sdfnjl lkla klsdf', 7, 5),
(12, 'afk sdfmk lsdk kma', 7, 5);

-- --------------------------------------------------------

--
-- Table structure for table `homepage`
--

DROP TABLE IF EXISTS `homepage`;
CREATE TABLE IF NOT EXISTS `homepage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `homepage`
--

INSERT INTO `homepage` (`id`, `data`) VALUES
(1, '<h2>Üdvözöljük a főoldalon!</h2><p>Szép jó napot kívánunk tisztelettel!</p>'),
(2, '<h2>Üdvözöljük a főoldalon!</h2><p>Szép jó napot kívánunk tisztelettel!</p><figure class=\"image\"><img src=\"https://dusza.myferences.hu/upload_image\"></figure>'),
(3, '<h2>Üdvözöljük a főoldalon!</h2><p>Szép jó napot kívánunk tisztelettel!</p><figure class=\"image\"><img style=\"aspect-ratio:1008/504;\" src=\"https://dusza.myferences.hu/static/uploaded_images/potato.jpg\" width=\"1008\" height=\"504\"></figure>'),
(4, '<h2><strong>Üdvözöljük a főoldalon!</strong></h2><p>Szép jó napot kívánunk tisztelettel!</p><figure class=\"image\"><img style=\"aspect-ratio:1008/504;\" src=\"https://dusza.myferences.hu/static/uploaded_images/potato.jpg\" width=\"1008\" height=\"504\"></figure>'),
(5, '<h2><strong>Üdvözöljük a főoldalon!</strong></h2><p>Szép jó napot kívánunk tisztelettel!</p><figure class=\"image\"><img style=\"aspect-ratio:1008/504;\" src=\"https://dusza.myferences.hu/static/uploaded_images/potato.jpg\" width=\"1008\" height=\"504\"></figure>'),
(6, '<figure class=\"image\"><img style=\"aspect-ratio:4624/3468;\" src=\"https://dusza.myferences.hu/static/uploaded_images/20231201_170221.jpg\" width=\"4624\" height=\"3468\"></figure><h2><strong>Üdvözöljük a főoldalon!</strong></h2><p>Szép jó napot kívánunk tisztelettel!</p><figure class=\"image\"><img style=\"aspect-ratio:1008/504;\" src=\"https://dusza.myferences.hu/static/uploaded_images/potato.jpg\" width=\"1008\" height=\"504\"></figure>'),
(7, '<h2>&nbsp;</h2><figure class=\"table\"><table><tbody><tr><td>mili</td><td>gram</td></tr><tr><td>kilo</td><td>gram</td></tr><tr><td>kilo</td><td>norbert</td></tr><tr><td>stu</td><td>rumungro</td></tr></tbody></table></figure><h2><strong>Üdvözöljük a főoldalon!</strong></h2><p>Szép jó napot kívánunk tisztelettel!</p><figure class=\"image\"><img style=\"aspect-ratio:1008/504;\" src=\"https://dusza.myferences.hu/static/uploaded_images/potato.jpg\" width=\"1008\" height=\"504\"></figure>'),
(8, '<h2><strong>Üdvözöljük a főoldalon!</strong></h2><p>Szép jó napot kívánunk!</p>'),
(9, '<h2><strong>Üdvözöljük a főoldalon!</strong></h2><p>Szép jó napot kívánunk!</p><p>&nbsp;</p><p>Gál Tamás xoxo</p><p>&nbsp;</p><figure class=\"image\"><img style=\"aspect-ratio:730/360;\" src=\"https://dusza.myferences.hu/static/uploaded_images/El-Salvador-prez-Nayib-Bukele-warns-US-hes-the-only-one-allowed-to-ruin-his-country-min.jpg\" width=\"730\" height=\"360\"></figure>'),
(10, '<h2><strong>Üdvözöljük a főoldalon!</strong></h2><p>Szép jó napot kívánunk!</p><p>&nbsp;</p><p>Gál Tamás xoxo</p><p>&nbsp;</p><p>&nbsp;</p>'),
(11, '<h2><strong>Üdvözöljük a főoldalon!</strong></h2><p>Szép jó napot kívánunk!</p>');

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
CREATE TABLE IF NOT EXISTS `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `display_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `display_name`) VALUES
(1, 'ADMIN', 'Webmester'),
(2, 'TANAR', 'Tanár'),
(3, 'DIAK', 'Diák'),
(4, 'ZSURI', 'Zsűri');

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
CREATE TABLE IF NOT EXISTS `teams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `team_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `evfolyam` int NOT NULL,
  `osztaly` varchar(1) NOT NULL,
  `verseny_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `team_name` (`team_name`),
  KEY `verseny_id` (`verseny_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `team_name`, `description`, `evfolyam`, `osztaly`, `verseny_id`) VALUES
(1, '7/B csapata', 'A legjobb versenyzők', 7, 'b', 1),
(3, '7/B tartalék', 'A többi versenyző', 7, 'b', 1);

-- --------------------------------------------------------

--
-- Table structure for table `upload`
--

DROP TABLE IF EXISTS `upload`;
CREATE TABLE IF NOT EXISTS `upload` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `upload`
--

INSERT INTO `upload` (`id`, `user_id`) VALUES
(1, 1),
(3, 1),
(2, 2),
(4, 8),
(5, 8);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `digest` varchar(255) NOT NULL,
  `role_id` int NOT NULL,
  `evfolyam` int DEFAULT NULL,
  `osztaly` varchar(1) DEFAULT NULL,
  `team_id` int DEFAULT NULL,
  `progress` int DEFAULT NULL,
  `helyes` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `role_id` (`role_id`),
  KEY `team_id` (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `progress`, `helyes`) VALUES
(1, 'admin', 'scrypt:32768:8:1$cREfsjByVMKJGCjm$0e126590b1637bf7e918fc793c9a11e46a6426b6aa514f9371ad500195fc1a069adec215968be956fa2144fa1c55f97c4ce0a1972be49424eae06e9ed5bc87f2', 1, NULL, NULL, NULL, NULL, NULL),
(2, 'Tóth István', 'scrypt:32768:8:1$aXmu7e2qGkoLnIey$99b0397574f50b114653e2735c9c9cf34961b10d29a714f4300b1a3b638e035833252bcbbf5f5aa16b435c279496a422a3894f47412f7c2df0367dcdcc9c53e0', 3, 7, 'b', 1, 3, 1),
(3, 'Horváth Éva', 'scrypt:32768:8:1$Ua9lGcGN8LdqyaiJ$46e6fca1f1867d6a5739df34161a98070f0fcee3e35136fa9a8efe56da4134506d1561d1bbd9445398e71e1a66178992def9d9dfde85071cd7dc95dfb1a71f41', 3, 7, 'b', 1, 7, 1),
(4, 'Varga Mária', 'scrypt:32768:8:1$IM29LAmEm9fRV0jQ$a5e9f363f6fee7069f3c052bb4b3563c49de16d731859bd7fe7d12002835fd708d7bd1ea8a7fe0528f0e7ff8652ae1520feadb6af121417c384f3b6ce34c8a33', 3, 7, 'b', 1, 2, 0),
(5, 'Molnár Katalin', 'scrypt:32768:8:1$2Z4pxE7pgNe8zQev$90b4afbd7d01410f7d7f261b30cdfecf9642b2c2ceb3d2b8f55c3117f0081b010cbf3cd003d339478f80051df5e083c08a1bce0312e6c7e09c9c818e8abeca16', 3, 7, 'b', 3, 0, 0),
(6, 'Szabó László', 'scrypt:32768:8:1$jzNZw0LRpzREMpAU$e9e83e01c0d8aa91778369448d5e76f7837f9e6af1f15971b0adf9faeb7e0d2a69e02817d775830d4ab969c4d858a1c455814af9f74809edd602d920d207cdbf', 3, 7, 'b', 3, 1, 0),
(7, 'Kovács József', 'scrypt:32768:8:1$BKr879eDTUOCGCTR$61ee3a97060a9c756d79bda4d0889c0cb9e0ed75bc4cbe6b60e765ff5b403a8ff9d3e11f7027551f0a417b34a553a542aa349f0ab22c397560db636584588229', 4, 5, ' ', NULL, 1, 0),
(8, 'Adolf Géza', 'scrypt:32768:8:1$na3TkBkQCKWzaZkh$9d918fd50cf68310eec4144a4b50d11c3a7fdb40009c8a0b246e53e74bcec8dc0c520f0d07324b0ebb2bbe73bf09ae1f0ae13aadaa695c30423a2626ecae75a0', 2, 5, ' ', NULL, 1, 0),
(9, 'Neubrandt Ferenc', 'scrypt:32768:8:1$L78mAY2GJOydjtep$249ba9900a6c948a7b51284f36b22feb32f0d92b39af424d6c2adb02cef802f1c7459fb88f72beb5352494700e218aa39083780b599cb56852c57c7e84edb1c3', 2, 5, ' ', NULL, 1, 0),
(10, 'Nagy Anna', 'scrypt:32768:8:1$PU5kYFGJyXYx0R7j$38bbd675f071fbb28d5b458908c810f7ed1393bbaa2acc03ba052d7471dbbb6f2640338f5605a84e8069bfdcfd1200a168b7bc291287ab2690ecc46bf43027fc', 4, 5, ' ', NULL, 1, 0),
(11, 'Kiss Gábor', 'scrypt:32768:8:1$kSf1kjXw7xt8O8cy$72c7054f9bdb4fe5f847567542c944b50a52026a75b0fb6356f0afc66e45e00ffefe04f14e55e866d19ace8fa21945e9eb37a1351c69f96233627abf260c145c', 3, 7, 'b', 3, 2, 0),
(12, 'diak1', 'scrypt:32768:8:1$0kpP0yosOVhMU7vH$92da37bf3109dd36732c209da002ec3324bbfcfb7b4af584d8f3c4b00986ba488d689791fa6af5aad85aaed1fdac3df98cf23524a985ae4d55935e8b84e31198', 3, 8, 'X', NULL, 1, 0),
(13, 'diak2', 'scrypt:32768:8:1$HKqr1ZSOmjIgS4QK$4e54da4027fa4666b6f72fccfea42561811734bed4e1cdf1d6411ee44f8e367b9d3ffc3ceeb1425390139685801817b6d541af1898465e106e19c375a2b926bd', 3, 8, 'X', NULL, 1, 0),
(14, 'diak3', 'scrypt:32768:8:1$tJmosM3lczH2XrK6$c0bf6a2dfb81737ba5e1604ecc851471e661dd0ece483c7de117491e41abcd5ed408ffb1c23c61fde89800abb74d3aa2b2ea3bdef536869e1308804349b5c330', 3, 8, 'X', NULL, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `verseny`
--

DROP TABLE IF EXISTS `verseny`;
CREATE TABLE IF NOT EXISTS `verseny` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `kezdet` int NOT NULL,
  `veg` int NOT NULL,
  `evfolyam` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `verseny`
--

INSERT INTO `verseny` (`id`, `name`, `description`, `kezdet`, `veg`, `evfolyam`) VALUES
(1, 'Legjobb verseny', 'hetedikeseknek versenyecske', 1699696112, 1731622400, 7);

-- --------------------------------------------------------

--
-- Table structure for table `verseny_feladat`
--

DROP TABLE IF EXISTS `verseny_feladat`;
CREATE TABLE IF NOT EXISTS `verseny_feladat` (
  `verseny_id` int NOT NULL,
  `feladat_id` int NOT NULL,
  KEY `verseny_id` (`verseny_id`),
  KEY `feladat_id` (`feladat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `verseny_feladat`
--

INSERT INTO `verseny_feladat` (`verseny_id`, `feladat_id`) VALUES
(1, 3),
(1, 4),
(1, 7),
(1, 8),
(1, 9),
(1, 10);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `feladat`
--
ALTER TABLE `feladat`
  ADD CONSTRAINT `feladat_ibfk_1` FOREIGN KEY (`upload_id`) REFERENCES `upload` (`id`);

--
-- Constraints for table `teams`
--
ALTER TABLE `teams`
  ADD CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`verseny_id`) REFERENCES `verseny` (`id`);

--
-- Constraints for table `upload`
--
ALTER TABLE `upload`
  ADD CONSTRAINT `upload_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `users_ibfk_2` FOREIGN KEY (`team_id`) REFERENCES `teams` (`id`);

--
-- Constraints for table `verseny_feladat`
--
ALTER TABLE `verseny_feladat`
  ADD CONSTRAINT `verseny_feladat_ibfk_1` FOREIGN KEY (`verseny_id`) REFERENCES `verseny` (`id`),
  ADD CONSTRAINT `verseny_feladat_ibfk_2` FOREIGN KEY (`feladat_id`) REFERENCES `feladat` (`id`);
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
