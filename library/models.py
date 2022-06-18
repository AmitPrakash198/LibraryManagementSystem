from tkinter.tix import INCREASING
from turtle import mode
from django.db import models

# Create your models here.
class Userregistration(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    useremail = models.CharField(max_length=200, blank=True, null=True)
    userenroll = models.CharField(max_length=200, blank=True, null=True)
    userbranch = models.CharField(max_length=200, blank=True, null=True)
    userid = models.CharField(max_length=200, blank=True, null=True)
    userpass = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'userregistration'

class addbookdetails(models.Model):
    bookname=models.CharField(max_length=200, blank=True, null=True)
    authorname=models.CharField(max_length=200, blank=True, null=True)
    bookcatagory=models.CharField(max_length=200, blank=True, null=True)
    bookisbn=models.CharField(max_length=200, blank=True, null=True)
    bookquantity=models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'addbookdetails'

class Issuedbookdetails(models.Model):
    username=models.CharField(max_length=200, blank=True, null=True)
    bookname=models.CharField(max_length=200, blank=True, null=True)
    bookisbn=models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'Issuedbookdetails'

class Adminlogindata(models.Model):
    adminuserid = models.CharField(primary_key=True, max_length=255)
    adminpassword = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminlogindata'
