-- ID: 新闻的唯一标示
-- title: 新闻的标题
-- content： 新闻的内容
-- created_at: 新闻添加的时间
-- types: 新闻的类型
-- image: 新闻的缩略图
-- author： 作者
-- view_count: 浏览量 默认值 0
-- is_valid: 删除标记 默认值 1(有效) 0 无效


CREATE TABLE `news`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(200) NOT NULL,
	`content` VARCHAR(2000) NOT NULL,
  `types` VARCHAR(10) NOT NULL,
	`image` VARCHAR(300) NULL,
	`author` VARCHAR(20) NULL,
	`view_count` INT DEFAULT 0,
	`created_at` DATETIME NULL,
	`is_valid` SMALLINT DEFAULT 1,
	 PRIMARY KEY(`id`)
) DEFAULT CHARSET = 'UTF8'

-- 插入单条数据
INSERT INTO `news`(`title`,`image`, `content`, `types`) VALUE ('标题1', '/static/img/news/01.png', '新闻内容1', '推荐');

-- 使用SQL语句向数据表写入八条不同的数据
INSERT INTO `news`(`title`,`image`, `content`, `types`,`created_at`) VALUES
	('朝鲜特种部队视频公布 展示士兵身体素质与意志', '/static/img/news/01.png', '新闻内容', '推荐', now()),
	('男子长得像\"祁同伟\"挨打 打人者:为何加害检察官', '/static/img/news/02.png', '新闻内容', '百家', now()),
	('导弹来袭怎么办？日本政府呼吁国民躲入地下通道', '/static/img/news/03.png', '新闻内容', '本地', now()),
	('美媒:朝在建能发射3发以上导弹的3000吨级新潜艇', '/static/img/news/04.png', '新闻内容', '推荐', now()),
	('证监会:前发审委员冯小树违法买卖股票被罚4.99亿', '/static/img/news/08.png', '新闻内容', '百家', now()),
	('外交部回应安倍参拜靖国神社:同军国主义划清界限', '/static/img/news/new1.jpg', '新闻内容', '推荐', now()),
	('外交部回应安倍参拜靖国神社:同军国主义划清界限', '/static/img/news/new1.jpg', '新闻内容', '百家', now()),
	('\"萨德\"供地违法？韩民众联名起诉要求撤回供地', '/static/img/news/new1.jpg', '新闻内容', '百家', now());

-- 使用SQL语句查询类别为“百家”的新闻数据
SELECT `title`, `content`,`types` FROM `news` WHERE `types` = '百家';

-- 使用SQL语句删除一条新闻数据
UPDATE `news` SET `is_valid` = 0 WHERE `id`= 1;
DELETE FROM `news` WHERE `is_valid` = 0;
DELETE FROM `news` WHERE `id` < 10;

-- 使用SQL语句查询所有的新闻，以添加时间的倒序进行排列,查询最新新闻
SELECT * FROM `news` ORDER BY `created_at` DESC;

-- 使用SQL语句查询第二页数据（每一页5条数据）
SELECT * FROM `news` LIMIT 5, 5;
