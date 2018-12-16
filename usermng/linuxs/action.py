#from logging import info as Info__
from django.contrib import messages
from .events import GroupFunc ,show_all_linux_groups,UserFuncCls,show_all_user_name,get_users_group_name, change_user_directory
from .models import UserGroup,User
from re import match, compile

def add_user_group(modeladmin,request,queryset):
	for group in queryset:
		result = GroupFunc(group.groupGID,group.groupName,group.groupPassword).addGroup()
		messages.info(request,result[0])
		if result[1] == 1:
			group.status = 1
			group.save()
add_user_group.short_description = 'excute in your bindding linux(Add User)'

def del_user_group(modeladmin,request,queryset):
	for group in queryset:
		result = GroupFunc(group.groupGID,group.groupName,group.groupPassword).delGroup()
		messages.info(request,result[0])
		if result[1] == 1:
			group.delete()
del_user_group.short_description = "delete in your bindding linux and delete model from this chart"


def modify_group_GID(modeladmin,request,queryset):
	for group in queryset:
		result = GroupFunc(group.groupGID,group.groupName,group.groupPassword).modGroupGID()
		messages.info(request,result[0])
modify_group_GID.short_description = "update your GID of your group that your selected"

def modify_group_name(modeladmin,request,queryset):
	for group in queryset:
		result = GroupFunc(group.groupGID,group.groupName,group.groupPassword).modGroupName()
		messages.info(request,result[0])
modify_group_name.short_description = "update your groupName that your selected"

def show_all_group_in_linux(modeladmin,request,queryset):
	results = show_all_linux_groups()
	for grp in results:
		if len(UserGroup.objects.filter(groupName__contains=grp['groupName'])) == 0:
			UserGroup.objects.create(groupGID=grp['groupGID'],
				groupName=grp['groupName'],
				groupPassword=grp['groupPassword'],
				status=1)	
show_all_group_in_linux.short_description = "show all your real group on linux there"

def add_user(modeladmin,request,queryset):
	for user in queryset:
		result = UserFuncCls(name=user.name,
			password=user.password,
			group=user.group,
			directory=user.directory,
			).add_user()
	messages.info(request,"%s users have been added"%(str(len(queryset))))
add_user.short_description = "add user that your selected into linux"

def del_user_and_its_dir(modeladmin,request,queryset):
	for user in queryset:
		result  =  result = UserFuncCls(name=user.name,
			password=user.password,
			group=user.group,
			directory=user.directory,
			).del_user(delete_all=True)
	messages.info(request,"%s user have been deleted and deleted its dir "%(str(len(queryset))))
del_user_and_its_dir.short_description = "delete selected user and its directory"

def  del_user(modeladmin,request,queryset):
	for user in queryset:
		result  =  result = UserFuncCls(name=user.name,
			password=user.password,
			group=user.group,
			directory=user.directory,
			).del_user(delete_all=True)
	messages.info(request,"%s user have been deleted "%(str(len(queryset))))
del_user.short_description = "just delete selected user"

def show_all_linux_user(modeladmin,request,queryset):
	results, res_lis = show_all_user_name()
	for li in res_lis:
		if len(User.objects.filter(name__contains=li)) == 0:
			group_name, err = get_users_group_name(li)
			if err!="":
				continue
			else:
				tarsear = UserGroup.objects.filter(groupName__contains=group_name)
				if len(tarsear) == 1:
					User.objects.create(name=li,
						status=1,
						password="-*-",
						group=tarsear[0],
						directory='-*-')
	messages.info(request,"this is all your wanted to see ")
show_all_linux_user.short_description = "show all linux user on here"
def chown_linux_user_to_directory(modeladmin,request,queryset):
	results=[]
	success_num = 0
	for li in queryset:
		pat = compile(li.name)
		tmp = change_user_directory(li)
		if match(pat,tmp):
			success_num = success_num + 1
		else:
			results.append(tmp)
	messages.info(request,"%d finished %d successfully"%(len(queryset),success_num)+"{result}".format(
		result=str("failed reason %s :%s"%("is" if len(queryset)==1 else "are","".join(results))) if len(queryset)>success_num else " all are success")
chown_linux_user_to_directory.short_description = "改变目录的属主"
