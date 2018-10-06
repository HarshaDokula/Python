import cx_Oracle
con = cx_Oracle.connect('taz1826/mydb321@127.0.0.1/Oracle8')
print(con.version)
cur = con.cursor()
cur.execute('select * from boats')
for result in cur:
	print(result)
cur.close()
con.close()
