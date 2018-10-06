/*
 Navicat Premium Data Transfer

 Source Server         : EzyPay
 Source Server Type    : MySQL
 Source Server Version : 50714
 Source Host           : 35.197.159.11:3306
 Source Schema         : bankService

 Target Server Type    : MySQL
 Target Server Version : 50714
 File Encoding         : 65001

 Date: 06/10/2018 12:04:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id` char(36) NOT NULL,
  `bank_id` char(36) NOT NULL,
  `partner_id` char(36) NOT NULL,
  `account_name` varchar(100) NOT NULL,
  `account_number` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `deleted` int(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fkIdx_9` (`bank_id`),
  CONSTRAINT `FK_9` FOREIGN KEY (`bank_id`) REFERENCES `bank` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for account_meta
-- ----------------------------
DROP TABLE IF EXISTS `account_meta`;
CREATE TABLE `account_meta` (
  `id` char(36) NOT NULL,
  `account_id` char(36) NOT NULL,
  `key` varchar(255) NOT NULL,
  `value` text NOT NULL,
  `deleted` int(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_key` (`account_id`,`key`),
  KEY `fkIdx_19` (`account_id`),
  CONSTRAINT `FK_19` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='predefined meta key:\n- COMPANY\\_ID\n- USER\\_ID\n- PASSWORD';

-- ----------------------------
-- Table structure for account_transaction
-- ----------------------------
DROP TABLE IF EXISTS `account_transaction`;
CREATE TABLE `account_transaction` (
  `id` char(36) NOT NULL,
  `account_id` char(36) NOT NULL,
  `post_date` datetime NOT NULL,
  `debit` double NOT NULL,
  `credit` double NOT NULL,
  `balance` double NOT NULL,
  `note` text NOT NULL,
  `status` varchar(50) NOT NULL,
  `deleted` int(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fkIdx_56` (`account_id`),
  CONSTRAINT `FK_56` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bank
-- ----------------------------
DROP TABLE IF EXISTS `bank`;
CREATE TABLE `bank` (
  `id` char(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  `base_url` varchar(255) NOT NULL,
  `scrapping_period` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `deleted` int(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for system_app
-- ----------------------------
DROP TABLE IF EXISTS `system_app`;
CREATE TABLE `system_app` (
  `id` char(36) NOT NULL,
  `name` varchar(100) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  `type` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `deleted` int(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_key_unique` (`api_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for system_config
-- ----------------------------
DROP TABLE IF EXISTS `system_config`;
CREATE TABLE `system_config` (
  `id` char(36) NOT NULL,
  `key` varchar(255) NOT NULL,
  `value` text NOT NULL,
  `deleted` int(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key_unique` (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for transfer_amount
-- ----------------------------
DROP TABLE IF EXISTS `transfer_amount`;
CREATE TABLE `transfer_amount` (
  `id` char(36) NOT NULL,
  `partner_id` char(36) NOT NULL,
  `amount` double NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `deleted` int(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for transfer_request
-- ----------------------------
DROP TABLE IF EXISTS `transfer_request`;
CREATE TABLE `transfer_request` (
  `id` char(36) NOT NULL,
  `account_id` char(36) NOT NULL,
  `transfer_amount_id` char(36) NOT NULL,
  `status` varchar(50) NOT NULL COMMENT '- unpaid\n- expired\n- paid',
  `real_amount` double NOT NULL,
  `deleted` int(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fkIdx_43` (`account_id`),
  KEY `fkIdx_46` (`transfer_amount_id`),
  CONSTRAINT `FK_43` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`),
  CONSTRAINT `FK_46` FOREIGN KEY (`transfer_amount_id`) REFERENCES `transfer_amount` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
