from django.contrib import admin

from .models import UserGroup , User
from .action import  add_user_group ,del_user_group, modify_group_GID,modify_group_name, show_all_group_in_linux,add_user,del_user_and_its_dir,del_user,show_all_linux_user

class UserGroupAdmin(admin.ModelAdmin):
	list_display = ['id','status','groupGID','groupName','groupPassword']
	exclude = []
	actions = [add_user_group,del_user_group, modify_group_GID,modify_group_name, show_all_group_in_linux]


class UserAdmin(admin.ModelAdmin):
	list_display = ['id','status','name','directory','password']
	exclude = []
	actions = [add_user,del_user_and_its_dir,del_user,show_all_linux_user]


admin.site.register(User,UserAdmin)
admin.site.register(UserGroup,UserGroupAdmin)