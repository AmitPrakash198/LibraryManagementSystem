from email import message
from pickle import NONE
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from matplotlib.style import context
from .models import Userregistration
from .models import addbookdetails
from .models import Issuedbookdetails
from .models import Adminlogindata
from .forms import StudRegisterForm
from .forms import AddBookForm
from django.contrib import messages
# import mysql.connector as mc
# conn = mc.connect(host="localhost", user="root", passwd="Mohit198@", database='librarymanagementsystem')
# print('Successfully connected to database')
# cur = conn.cursor()

# Create your views here.
def index(request):
    return render(request,'home.html')
    #return HttpResponse("This is Home Page.")

def myadmin(request):
    return render(request,'login_admin.html')

def login_stud(request):
    return render(request,'login_stud.html')

def stud_reg(request):
    return render(request,'stud_reg.html')

def admin_base(request):
    return render(request,'admin_base.html')

def student_base(request):
    return render(request,'student_base.html')

def add_book(request):
    return render(request,'add_book.html')

# def view_book(request):
#     return render(request,'view_book.html')

# def issue_book(request):
#     return render(request,'issue_book.html')

def view_issued_book(request):
    return render(request,'view_issued_book.html')

# def view_stud_details(request):
#     return render(request,'view_stud_details.html')

#Backend Code
def regprocess(request):
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('useremail') and request.POST.get('userenroll') and request.POST.get('userbranch') and request.POST.get('userid') and request.POST.get('userpass'):
            saverecord=Userregistration()
            saverecord.username=request.POST.get('username')
            saverecord.useremail=request.POST.get('useremail')
            saverecord.userenroll=request.POST.get('userenroll')
            saverecord.userbranch=request.POST.get('userbranch')
            saverecord.userid=request.POST.get('userid')
            saverecord.userpass=request.POST.get('userpass')
            saverecord.save()
            messages.success(request,'Record saved successfully...!!!')
            return render(request,'login_stud.html')
    else:
        return render(request,'login_stud')

def viewstuddetails(request):
    students=Userregistration.objects.all()
    return render(request,'view_stud_details.html',{'students':students})

def delprocess(request,userid):
    delstud=Userregistration.objects.get(userid=userid)
    delstud.delete()
    students=Userregistration.objects.all()
    return render(request,'view_stud_details.html',{'students':students})

def editprocess(request,id):
    student=Userregistration.objects.get(id=id)
    return render(request,'edit_stud.html',{"Userregistration":student})

def updateprocess(request,id):
    updatestud=Userregistration.objects.get(id=id)
    form=StudRegisterForm(request.POST,instance=updatestud)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfully..!!")
        return render(request,'edit_stud.html',{"Userregistration":updatestud})

def addbookprocess(request):
    if request.method=='POST':
        if request.POST.get('bookname') and request.POST.get('authorname') and request.POST.get('bookcatagory') and request.POST.get('bookisbn') and request.POST.get('bookquantity'):
            saverecord=addbookdetails()
            saverecord.bookname=request.POST.get('bookname')
            saverecord.authorname=request.POST.get('authorname')
            saverecord.bookcatagory=request.POST.get('bookcatagory')
            saverecord.bookisbn=request.POST.get('bookisbn')
            saverecord.bookquantity=request.POST.get('bookquantity')
            saverecord.save()
            messages.success(request,'Record saved successfully...!!!')
            return render(request,'/view_book.html')
    else:
        return render(request,'view_book.html')

def viewbooksprocess(request):
    books=addbookdetails.objects.all()
    return render(request,'view_book.html',{'books':books})

def studentviewbook(request):
    books=addbookdetails.objects.all()
    return render(request,'student_view_book.html',{'books':books})

def delbookprocess(request,id):
    delbook=addbookdetails.objects.get(id=id)
    delbook.delete()
    books=addbookdetails.objects.all()
    return render(request,'view_book.html',{'books':books})

def editbookprocess(request,id):
    editbook=addbookdetails.objects.get(id=id)
    return render(request,'edit_book.html',{"addbookdetails":editbook})

def updatebookprocess(request,id):
    updatebook=addbookdetails.objects.get(id=id)
    form=AddBookForm(request.POST,instance=updatebook)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfully..!!")
        return render(request,'edit_book.html',{"addbookdetails":updatebook})

def showbookforissue(request):
    student=Userregistration.objects.all()
    books=addbookdetails.objects.all()
    return render(request,'issue_book.html',{'books':books, 'student':student})

def issuebookprocess(request):
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('bookname') and request.POST.get('bookisbn'):
            saverecord=Issuedbookdetails()
            saverecord.username=request.POST.get('username')
            saverecord.bookname=request.POST.get('bookname')
            saverecord.bookisbn=request.POST.get('bookisbn')
            saverecord.save()
            messages.success(request,'Record saved successfully...!!!')
            return render(request,'view_issued_book.html')
    else:
        return render(request,'admin_base.html')

def viewissuebooksprocess(request):
    issuebook=Issuedbookdetails.objects.all()
    return render(request,'view_issued_book.html',{'issuebook':issuebook})

def delissuebookprocess(request,id):
    delissuebook=Issuedbookdetails.objects.get(id=id)
    delissuebook.delete()
    issuebook=Issuedbookdetails.objects.all()
    return render(request,'view_issued_book.html',{'issuebook':issuebook})

def adminlogin(request):
        if request.method == 'POST':
            username = request.POST.get('user')
            password = request.POST.get('password')
            try:
                user = Adminlogindata.objects.get(adminuserid=username,adminpassword=password)
                if user is not None:               
                    return render(request, 'admin_base.html', {})
                else:
                    print("Someone tried to login and failed.")
                    print("They used username: {} and password: {}".format(username,password))
                    return render(request,'/admin_base.html')
            except Exception as identifier:
                return render(request,'login_admin.html')
        else:
            return render(request, 'login_admin.html')

def userlogin(request):
        if request.method == 'POST':
            username = request.POST.get('user')
            password = request.POST.get('password')
            try:
                user = Userregistration.objects.get(userid=username,userpass=password)
                if user is not None: 
                    return render(request, 'student_base.html',{'username':username})
                else:
                    print("Someone tried to login and failed.")
                    print("They used username: {} and password: {}".format(username,password))
                    return render(request,'/login_stud.html')
            except Exception as identifier:
                return render(request,'login_stud.html')
        else:
            return render(request, 'login_stud.html')


def showbookforissue_student(request):
    student=Userregistration.objects.all()
    books=addbookdetails.objects.all()
    return render(request,'student_issue_book.html',{'books':books, 'student':student})

def issuebookprocess_student(request):
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('bookname') and request.POST.get('bookisbn'):
            saverecord=Issuedbookdetails()
            saverecord.username=request.POST.get('username')
            saverecord.bookname=request.POST.get('bookname')
            saverecord.bookisbn=request.POST.get('bookisbn')
            saverecord.save()
            messages.success(request,'Record saved successfully...!!!')
            return render(request,'student_base.html')
    else:
        return render(request,'student_base.html')

def viewstudent_data(request):
    student=Userregistration.objects.all()
    return render(request,'view_profile.html',{'student':student})

def editprocess_student(request,id):
    student=Userregistration.objects.get(id=id)
    return render(request,'edit_student_data.html',{"Userregistration":student})

def deleteprocess_student(request,userid):
    delstud=Userregistration.objects.get(userid=userid)
    delstud.delete()
    return render(request,'/')

def updateprocess(request,id):
    updatestud=Userregistration.objects.get(id=id)
    form=StudRegisterForm(request.POST,instance=updatestud)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfully..!!")
        return render(request,'edit_stud.html',{"Userregistration":updatestud})