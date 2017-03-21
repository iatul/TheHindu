import MySQLdb

class Query:
	def __init__(self):
		self.connect()	


	def connect(self):
		self.db = MySQLdb.connect("localhost","root","","hindu_db" )
		self.cursor = self.db.cursor()

	def search(self, sql):
		try:
			self.cursor.execute(sql)	
			results = self.cursor.fetchall()
			return results
		except:
			return "Error: unable to fetch data"	


	def close(self):
		self.db.close()