
from .events import get_all_dbs
from .models import MysqlDB, MySqlNode, DBUser
from django.contrib import messages

def show_all_database_exists_on_node(modeladmin,request,queryset):
	results,host,port = get_all_dbs()
	if results == None:
		messages.info(request,"something error , check log for more info!")
	else:
		node = MySqlNode.objects.create(node_ip_or_host=host,node_port=port)
		#users = []
		#[users.append(DBUser.objects.create(user_name=li.User,user_passwd="--*--")) for li in results]
		for li in range(len(results)):
			user_s = DBUser.objects.filter(user_name=results[li].User)
			db = MysqlDB.objects.create(node=node,
				db_name=results[li].Db,
				allow_host=results[li].Host)
			db.user.add(*user_s)


show_all_database_exists_on_node.short_description = "show all of your dbs in reality!"
