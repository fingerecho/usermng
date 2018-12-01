#!/usr/bin/python
from logging import info as Info__
from subprocess import run , PIPE
from sys import getdefaultencoding
#import shlex
DEFAULT_ENCODING = getdefaultencoding()

EXCEPTION_REASON = "execute exception bacause authtication is not enough, or other linux reasons!"

cmds = [
	'groupadd',#0
	'groupdel',#1
	'groupmod',#2
	'newgrp',#3
	'useradd',#4
	'userdel',#5
	'usermod',#6
	'passwd',#7
]

class GroupFunc(object):
	def __init__(self,gid,name,passwd):
		self.gid = str(gid)
		self.name = name
		self.passwd = passwd
	def addGroup(self):
		result =["",0]
		try:
			res = run([cmds[0],'-g',self.gid,self.name],stderr=PIPE,stdout=PIPE)
			if res.returncode==0:
				result[0] = "%s, group %s has been added in linux "%(res.stdout.decode(encoding=DEFAULT_ENCODING),self.name)
				result[1] = 1			
			else:
				result[0] = "group %s adding  failed , %s, please check log for more infomations"%(self.name,res.stderr.decode(encoding=DEFAULT_ENCODING))
		except Exception:
			result[0] = EXCEPTION_REASON
		finally:
			return result
	def delGroup(self):
		result = ""
		result = ["",0]
		try:
			res = run([cmds[1],self.name],stdout=PIPE)
			if res.returncode==0:
				result[0] = "%s, group %s has been added in linux "%(res.stdout.decode(encoding=DEFAULT_ENCODING),self.name)
				result[1] = 1
			else:
				result[0] = "group %s adding  failed , %s, please check log for more infomations"%(self.name,res.stderr.decode(encoding=DEFAULT_ENCODING))
		except Exception:
				result[0] = EXCEPTION_REASON	
		finally:
			return result
	def modGroupGID(self):
		result = ""
		result = ["",0]
		try:
			res = run([cmds[2],'-g',self.gid,self.name],stdout=PIPE)
			if res.returncode==0:
				result[0] = "%s, group %s has been modified in linux "%(res.stdout.decode(encoding=DEFAULT_ENCODING),self.name)
				result[1] = 1
			else:
				result[0] = "group %s adding  failed , %s, please check log for more infomations"%(self.name,res.stderr.decode(encoding=DEFAULT_ENCODING))
		except Exception:
			result[0] = EXCEPTION_REASON
		finally:
			return result
	def modGroupName(self):
		result = ""
		result = ["error in init",0]
		#args = shlex.split('cat /etc/group | grep " %s "'%self.gid)
		tar = ""
		try:
			tar_res = run(['cat','/etc/group'],stdout=PIPE)
			tar_res = tar_res.stdout.decode(encoding=DEFAULT_ENCODING).split("\n")
			for itar in tar_res:
				if str(itar.split(":")[2:3]).strip("[").strip("]").strip("'").strip() == self.gid.strip():
					tar = str(itar.split(":")[0]).strip("[").strip("]").strip("'").strip()
		except Exception:
			result[1] = 1
			results[0] = EXCEPTION_REASON
		finally:
			if result[1] == 1 or tar=="":
				return [result[0],0]
			try:
				res = run([cmds[2],'-n',self.name,tar],stdout=PIPE)
				if res.returncode==0:
					result[0] = "%s group %s has been modified in linux "%(res.stdout.decode(encoding=DEFAULT_ENCODING),self.name)
					result[1] = 1
				else:
					result[0] = "group %s adding  failed , %s, please check log for more infomations"%(self.name,res.stderr.decode(encoding=DEFAULT_ENCODING))
			except Exception:
				result[0] = EXCEPTION_REASON
			finally:
				return result

def show_all_linux_groups():
	res = run(['cat','/etc/group'],stdout=PIPE)
	res = res.stdout.decode(encoding=DEFAULT_ENCODING).split("\n")
	results = []
	[results.append({'groupName':res[i].split(":")[0].strip("[").strip("]").strip("'").strip(),
		'groupGID':str(res[i].split(":")[2:3]).strip("[").strip("]").strip("'").strip(),
		'groupPassword':'--*--'}) for i in range(len(res)) ]
	return results


class UserFuncCls(object):
	def __init__(self,name,password,group,directory,shell="/bin/bash",useruid="-1",additiongroup=None):
		self.name = name
		self.password = password
		self.group = group
		self.directory = directory
		self.shell = shell
		self.useruid = useruid
		self.additiongroup = additiongroup
	def add_user(self):
		results = ["",0]
		try:
			res = run([cmds[4],'-d',self.directory,'-m',self.name,'-s',self.shell,'-g',self.group.groupName],stderr=PIPE,stdout=PIPE)
			if res.returncode == 0:
				results[0] = "user added successfully %s"%res.stdout.decode(encoding=DEFAULT_ENCODING)
				results[1] = 1
			else:
				results[0] = "user adding failed %s"%res.stderr.decode(encoding=DEFAULT_ENCODING)
		except Exception:
			results[0] = EXCEPTION_REASON
		finally:
			return results
	def del_user(self,delete_all=True):
		da = ""
		results = ["",0]
		if delete_all == True:
			da = "-r"
		try:
			res = run([cmd[5],da,self.name],stdout=PIPE,stderr=PIPE)
			if res.returncode == 0:
				results[0] = 'user deleted successfully %s'%res.stdout.decode(encoding=DEFAULT_ENCODING)
				results[1] = 1
			else:
				results[0] = "execute failed %s"%res.stderr.decode(encoding=DEFAULT_ENCODING)
		except Exception:
			results[0] = EXCEPTION_REASON
		finally:
			return results

def show_all_user_name():
	res_li = None
	results = ["",0]
	try:
		res = run(['cat','/etc/shadow'],stdout=PIPE,stderr=PIPE)
		if res.returncode == 0:
			res_lis = res.stdout.decode(encoding=DEFAULT_ENCODING).split("\n")
			res_li = [li.split(":")[0] for li in res_lis]
			results[1] = 1
		else:
			results[0] = "show all user failed %s"%stderr
	except Exception:
		results[0] = EXCEPTION_REASON
	finally:
		return results , res_li
def get_users_group_name(username):
	result = ""
	err = ""
	try:
		res = run(['groups',username],stdout=PIPE,stderr=PIPE)
		if res.returncode == 0:
			result = res.stdout.decode(encoding=DEFAULT_ENCODING).split(":")[1].strip()
	except Exception:
		err = EXCEPTION_REASON
	finally:
		return result,err


