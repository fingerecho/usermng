from django.db import models

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
class MySqlNode(models.Model):
	id = models.AutoField(primary_key=True)
	#node_ip_or_host = models.GenericIPAddressField(protocol='IPv4')
	node_ip_or_host = models.CharField(max_length=64,blank=False)
	node_port = models.IntegerField(blank=False)

	def __str__(self):
		return "server_node_%d"%self.id

class DBUser(models.Model):
	PRIVILEGES = (
		('N','no'),
		('Y','yes')
	)
	SSL_TYPE = (
		('0',''),
		('1','ANY'),
		('2','X509'),
		('3','SPECIFIED'),
	)
	id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=64,blank=False)
	user_passwd = models.CharField(max_length=128,blank=False)
	select_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	insert_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	update_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	delete_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	create_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	drop_priv   = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	reload_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	shutdown_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	process_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	file_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	grant_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	references_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	index_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	alter_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	show_db_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	super_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	create_tmp_table_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	lock_tables_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	excute_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	repl_slave_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	repl_client_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	create_view_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	show_view_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	create_routine_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	alter_routine_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	create_user_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	event_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	trigger_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	create_tablespace_priv = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	password_expired = models.CharField(max_length=1,choices=PRIVILEGES,default='N')
	ssl_type = models.CharField(max_length=16,choices=SSL_TYPE,default=0)
	ssl_cipher = models.BinaryField(editable=False,blank=True,default=bytes("",encoding="utf-8"))
	x509_issuer = models.BinaryField(editable=False,blank=True,default=bytes("",encoding="utf-8"))
	x509_subject = models.BinaryField(editable=False,blank=True,default=bytes("",encoding="utf-8"))
	max_questions = models.IntegerField(blank=True,default=0)
	max_updates = models.IntegerField(blank=True,default=0)
	max_connections = models.IntegerField(blank=True,default=0)
	max_user_connections = models.IntegerField(blank=True,default=0)
	plugin = models.CharField(max_length=64,blank=True)
	authentication_string = models.TextField(blank=True)
	def __str__(self):
		return self.user_name
class TableField(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128,blank=False)
	type = models.CharField(max_length=64,blank=False)
	null = models.CharField(max_length=8,blank=False,default="NO")		
	key = models.CharField(max_length=8,blank=True,default="")
	default = models.CharField(max_length=256,blank=True,default="N")
	Extra = models.CharField(max_length=128,blank=True,default="")
	def __str__(self):
		return self.name
class DBTable(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64,blank=False)
	tables = models.ManyToManyField('TableField')
	def __str__(self):
		return self.name
class MysqlDB(models.Model):
	id = models.AutoField(primary_key=True)
	node = models.ForeignKey('MySqlNode',to_field='id',on_delete=models.CASCADE)
	db_name = models.CharField(max_length=64,blank=False)
	user = models.ManyToManyField('DBUser')
	tables = models.ManyToManyField('DBTable',blank=True)
	allow_host = models.CharField(max_length=64,blank=False,default='%')
	def __str__(self):
		return self.db_name
		
Base = declarative_base()

class MysqlDBSQLAC(Base):
	__tablename__ = "db"
	id = Column(String(20), primary_key=True)
	Host = Column(String(60))
	Db = Column(String(64))
	User = Column(String(16))