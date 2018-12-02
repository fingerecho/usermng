from os import path


HOST = 'localhost'
PASSWORD = ''
PORT = ''

def init_db_cofigure():
	global HOST, PASSWORD,PORT
	def config():
		global HOST, PASSWORD, PORT
		f = open(path.join(path.dirname(__file__),"conf","db.conf"))
		res = f.readlines()
		f.close()
		for i in res:
			tmp = i.split("=")
			if tmp[0] == "HOST":
				HOST = tmp[1].strip("\n")
			if tmp[0] == "PASSWORD":
				PASSWORD = tmp[1].strip("\n")
			if tmp[0] == "PORT":
				PORT = tmp[1].strip("\n")
	config()
	pass
init_db_cofigure()