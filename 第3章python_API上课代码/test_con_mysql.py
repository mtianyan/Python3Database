import MySQLdb

con = MySQLdb.connect(
	host='127.0.0.1',
	user='root',
	passwd='',
	port=3308,
	db='news',
	charset='utf8'
	)

cursor = con.cursor()
cursor.execute('SELECT * FROM `news`')
rest = cursor.fetchone()
print(rest)