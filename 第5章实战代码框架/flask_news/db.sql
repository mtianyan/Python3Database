/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50612
Source Host           : localhost:3306
Source Database       : flask_test

Target Server Type    : MYSQL
Target Server Version : 50612
File Encoding         : 65001

Date: 2017-04-21 17:58:28
*/




SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `news`
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `img_url` varchar(200) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `is_valid` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `news_type` varchar(200) DEFAULT '百家',
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` (`title`, `img_url`, `content`, `is_valid`, `created_at`, `updated_at`, `news_type`) VALUES ('朝鲜特种部队视频公布 展示士兵身体素质与意志', '/static/img/news/01.png', '新闻内容', 1, now(), now(), '推荐');
INSERT INTO `news` (`title`, `img_url`, `content`, `is_valid`, `created_at`, `updated_at`, `news_type`) VALUES ('男子长得像\"祁同伟\"挨打 打人者:为何加害检察官', '/static/img/news/02.png', '新闻内容', 1, now(), now(), '百家');
INSERT INTO `news` (`title`, `img_url`, `content`, `is_valid`, `created_at`, `updated_at`, `news_type`) VALUES ('导弹来袭怎么办？日本政府呼吁国民躲入地下通道', '/static/img/news/03.png', '新闻内容', 1, now(), now(), '本地');
INSERT INTO `news` (`title`, `img_url`, `content`, `is_valid`, `created_at`, `updated_at`, `news_type`) VALUES ('美媒:朝在建能发射3发以上导弹的3000吨级新潜艇', '/static/img/news/04.png', '新闻内容', 1, now(), now(), '推荐');
INSERT INTO `news` (`title`, `img_url`, `content`, `is_valid`, `created_at`, `updated_at`, `news_type`) VALUES ('证监会:前发审委员冯小树违法买卖股票被罚4.99亿', '/static/img/news/08.png', '新闻内容', 1, now(), now(), '百家');
INSERT INTO `news` (`title`, `img_url`, `content`, `is_valid`, `created_at`, `updated_at`, `news_type`) VALUES ('外交部回应安倍参拜靖国神社:同军国主义划清界限', '/static/img/news/new1.jpg', '新闻内容', 1, now(), now(), '推荐');
INSERT INTO `news` (`title`, `img_url`, `content`, `is_valid`, `created_at`, `updated_at`, `news_type`) VALUES ('外交部回应安倍参拜靖国神社:同军国主义划清界限', '/static/img/news/new1.jpg', '新闻内容', 1, now(), now(), '百家');
INSERT INTO `news` (`title`, `img_url`, `content`, `is_valid`, `created_at`, `updated_at`, `news_type`) VALUES ('\"萨德\"供地违法？韩民众联名起诉要求撤回供地', '/static/img/news/new1.jpg', '新闻内容', 1, now(), now(), '百家');
