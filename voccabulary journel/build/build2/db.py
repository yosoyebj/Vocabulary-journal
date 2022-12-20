import sqlite3


class Database:
	def __init__(self,db):
		self.con= sqlite3.Connection(db)
		self.cur= self.con.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS words(id INTEGER PRIMARY KEY,voc text,defe varchar(255))")
		self.con.commit()



	def fetch(self):
		self.cur.execute("SELECT voc FROM words")
		data1=self.cur.fetchall()
		print(data1)
		return data1

	def fetchdef(self,vocc):
		self.cur.execute("SELECT defe FROM words where voc=?",vocc)
		data2=self.cur.fetchone()
		# print(data2)
		return data2



	def insert(self,word,defenition):
		self.cur.execute("INSERT INTO words VALUES(NULL,?,?)",(word,defenition))
		self.con.commit()

		