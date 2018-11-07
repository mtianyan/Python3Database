import MySQLdb

class MysqlSearch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='',
                db='news',
                port=3308,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def close_conn(self):
        try:
            if self.conn:
                # 关闭链接
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def get_one(self):
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家', ))
        # print(dir(cursor))
        # 拿到结果
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def get_more(self):
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家', ))
        # print(dir(cursor))
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row))
            for row in cursor.fetchall()]
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def get_more_by_page(self, page, page_size):
        ''' 分页查询数据 '''
        offset = (page - 1) * page_size
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC LIMIT %s, %s;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家', offset, page_size))
        # print(dir(cursor))
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row)) 
            for row in cursor.fetchall()]
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        ''' 插入数据 '''
        # 受影响的行数
        row_count = 0
        try:
            # 准备SQL
            sql = (
                "INSERT INTO `news`(`title`,`image`, `content`, `types`, `is_valid`) VALUE"
                "(%s, %s, %s, %s, %s);"
            )
            # 获取链接和cursor
            cursor = self.conn.cursor()
            # 执行sql
            # 提交数据到数据库
            cursor.execute(sql, ('标题11', '/static/img/news/01.png', '新闻内容5', '推荐', 1))
            # cursor.execute(sql, ('标题12', '/static/img/news/01.png', '新闻内容6', '推荐', 1))
            # 提交事务
            self.conn.commit()
        except :
            print('error')
            # 回滚事务
            self.conn.rollback()
        # 执行最后一条SQL影响的行数
        row_count = cursor.rowcount
        # 关闭cursor和链接
        cursor.close()
        self.close_conn()
        # row_count > 0 表示成功
        return row_count > 0



def main():
    obj = MysqlSearch()
    # rest = obj.get_one()
    # print(rest['title'])

    # rest = obj.get_more()
    # for item in rest:
    #     print(item)
    #     print('------')

    # rest = obj.get_more_by_page(2, 3)
    # for item in rest:
    #     print(item)
    #     print('------')

    rest = obj.add_one()
    print(rest)


if __name__ == '__main__':
    main()