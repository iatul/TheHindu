import MySQLdb

class Query:
	def __init__(self):
		self.connect()	


	def connect(self):
		self.db = MySQLdb.connect("localhost","root","","hindu_db" )
		self.cursor = self.db.cursor()

		
	def create(self):	
		sql = """CREATE TABLE IF NOT EXISTS `hindu` (
				`id` INT NOT NULL AUTO_INCREMENT,
				`title` TEXT NOT NULL,
				`link` TEXT NOT NULL,
				`date` DATE NOT NULL,
				PRIMARY KEY (`id`),
				FULLTEXT (`title`),
				FULLTEXT (`link`)
				)ENGINE=InnoDB;"""

		self.cursor.execute(sql)


	def execute(self, sql):
		try:
			self.cursor.execute(sql)
			self.db.commit()	
		except:
			self.db.rollback()
			return False
		return True	


	def close(self):
		self.db.close()