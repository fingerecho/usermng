from os import path
from logging import warn as Warn__
from logging import info as Info__
from .models import MysqlDBSQLAC

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .configure_init import  HOST,PORT,PASSWORD

def get_all_dbs():
	results = None
	Info__(type(PORT))
	Warn__('mysql+pymysql://root:%s@%s:%s/mysql'%(str(PASSWORD),str(HOST),str(PORT)))
	#try:
	#engine = create_engine('dialect+driver://username:password@host:port/database')
	#engine = create_engine('mysql+mysqlconnector://root:%s@%s:%s/mysql'%(PASSWORD,HOST,PORT))
	#engine = create_engine('mysql+pymysql://root:%s@%s:%s/mysql'%(str(PASSWORD),str(HOST),str(PORT)))

	engine = create_engine('mysql+mysqldb://root:%s@%s:%s/mysql'%(str(PASSWORD),str(HOST),str(PORT)))
	
	#Warn__(type(engine))
	# Warning :   Pip3 install pymysql
	#if not engine:
	#	raise Exception
	DB_session = sessionmaker(bind=engine)
	session = DB_session()
	Warn__(type(session))
	#if session:
	results = session.query(MysqlDBSQLAC.Host,MysqlDBSQLAC.Db,MysqlDBSQLAC.User).all()
	session.close()
	return results,HOST,PORT
"""except Exception:
	Warn__("something run error on init dbs")
finally:"""
