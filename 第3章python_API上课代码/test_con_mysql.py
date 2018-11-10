import MySQLdb

try:
	con = MySQLdb.connect(
	host='127.0.0.1x',
	user='root',
	passwd='Zyy180926.',
	port=3306,
	db='school',
	charset='utf8'
	)
	# 获取数据
	cursor = con.cursor()
	cursor.execute('SELECT * FROM `news`')
	rest = cursor.fetchone()
	print(rest)

	# 关闭连接
	con.close()
except MySQLdb.Error as e:
	print("MysqlError: %s" %e)
