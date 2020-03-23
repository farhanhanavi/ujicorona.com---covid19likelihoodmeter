/*
Navicat MySQL Data Transfer

Source Server         : Localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : prognosis

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2020-03-23 10:48:00
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `responses`
-- ----------------------------
DROP TABLE IF EXISTS `responses`;
CREATE TABLE `responses` (
  `id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of responses
-- ----------------------------
INSERT INTO `responses` VALUES ('1', '3', '2020-03-22 18:56:22', null);
INSERT INTO `responses` VALUES ('1', '4', '2020-03-22 18:56:22', null);

-- ----------------------------
-- Table structure for `symptoms`
-- ----------------------------
DROP TABLE IF EXISTS `symptoms`;
CREATE TABLE `symptoms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `question` varchar(255) NOT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of symptoms
-- ----------------------------
INSERT INTO `symptoms` VALUES ('1', 'Berpergian ke Negara Terjangkit', 'Dalam 14-30 hari terakhir, apakah anda bepergian ke kota/negara terjangkit COVID19 ?', '2020-03-22 18:49:22', null);
INSERT INTO `symptoms` VALUES ('2', 'Kontak dengan Pasien Probabel/Konfirmasi', 'Dalam 14-30 hari terakhir, apakah anda melakukan kontak dengan Pasien Probabel/Konfirmasi ?', '2020-03-22 18:49:22', null);
INSERT INTO `symptoms` VALUES ('3', 'Kontak dengan Pasien dalam Pengawasan', 'Dalam 14-30 hari terakhir, apakah anda melakukan kontak dengan Pasien Dalam Pengawasan ?', '2020-03-22 18:49:22', null);
INSERT INTO `symptoms` VALUES ('4', 'Demam atau Batuk', 'Apakah mengalami demam, batuk', '2020-03-22 18:49:22', null);

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `ktp_no` varchar(16) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` enum('Pria','Wanita','Memilih Tidak Menyebutkan') NOT NULL,
  `address` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'rnauv', '3721372137213721', '29', 'Pria', 'bogor', 'rnauv3@gmail.com', '$2b$12$EL1t5EcUKrh4t0CqzZBCyu24XXKbnQDdn8qovPhn.YwxZ/nT0d/um', '2020-03-22 18:46:46', null);

-- ----------------------------
-- Table structure for `user_categories`
-- ----------------------------
DROP TABLE IF EXISTS `user_categories`;
CREATE TABLE `user_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user_categories
-- ----------------------------
INSERT INTO `user_categories` VALUES ('1', 'Self-Monitoring', '2020-03-22 18:54:59', null);
INSERT INTO `user_categories` VALUES ('2', 'Observasi/Karantina Rumah', '2020-03-22 18:54:59', null);
INSERT INTO `user_categories` VALUES ('3', 'Isolasi Diri di Rumah', '2020-03-22 18:54:59', null);
INSERT INTO `user_categories` VALUES ('4', 'Isolasi Diri di RS', '2020-03-22 18:54:59', null);

-- ----------------------------
-- Table structure for `user_responses`
-- ----------------------------
DROP TABLE IF EXISTS `user_responses`;
CREATE TABLE `user_responses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `response_id` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`user_id`,`response_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_responses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user_responses
-- ----------------------------
INSERT INTO `user_responses` VALUES ('1', '1', '1', '2020-03-22 18:55:52', null);
