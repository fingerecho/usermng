from django.contrib import admin

from .models import MySqlNode, DBUser,MysqlDB
from .actions import show_all_database_exists_on_node

class MySqlNodeAdmin(admin.ModelAdmin):
	list_display = ['id','node_ip_or_host','node_port']
	exclude = []
class DBUserAdmin(admin.ModelAdmin):
	list_display = ['id','user_name','user_passwd','max_connections','max_user_connections']
	exclude = []

class MysqlDBAdmin(admin.ModelAdmin):
	list_display = ['id','node','db_name']
	exclude = []
	actions = [show_all_database_exists_on_node]

admin.site.register(MysqlDB,MysqlDBAdmin)
admin.site.register(DBUser,DBUserAdmin)
admin.site.register(MySqlNode,MySqlNodeAdmin)