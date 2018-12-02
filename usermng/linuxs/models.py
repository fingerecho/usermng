from django.db import models

# Create your models here.

class UserGroup(models.Model):
	STATUS_CHOICES = (
		(0,"not exists"),
		(1,"exists")
		)
	id = models.AutoField(primary_key=True,blank=False)
	status = models.IntegerField(default=0,choices=STATUS_CHOICES)
	groupGID = models.IntegerField(blank=False)
	groupName = models.CharField(max_length=64,
		unique=True,blank=False)
	groupPassword = models.CharField(max_length=128,blank=False)
	def __str__(self):
		return self.groupName

class User(models.Model):
	STATUS_CHOICES = (
		(0,"not exists"),
		(1,"exists")
		)
	id = models.AutoField(primary_key=True,blank=False)
	status = models.IntegerField(default=0,choices=STATUS_CHOICES)
	name = models.CharField(max_length=64,blank=False)
	password = models.CharField(max_length=128,blank=False)
	group = models.ForeignKey(UserGroup,
		to_field='groupName',
		on_delete=models.CASCADE)
	directory = models.CharField(max_length=128,blank=False)
	additiongroup = models.ManyToManyField(UserGroup,related_name='+',blank=True)
	shell = models.CharField(max_length=64,blank=False,default='/bin/bash')
	useruid = models.IntegerField(blank=True,default='-1')
	@classmethod
	def groupname(self):
		return self.group.groupname
	def __str__(self):
		return self.name

