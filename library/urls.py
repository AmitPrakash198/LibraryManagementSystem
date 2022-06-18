"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path("",views.index, name='home'),
    # path("home/",views.index, name='home'),
    path("myadmin",views.myadmin, name='myadmin'),
    path("login_stud",views.login_stud, name='login_stud'),
    path("stud_reg",views.stud_reg, name='stud_reg'),
    path("admin_base",views.admin_base, name='admin_base'),
    path("student_base",views.student_base, name='student_base'),
    # path("add_book",views.add_book, name='add_book'),
    path("view_book",views.viewbooksprocess, name='viewbooksprocess'),
    # path("issue_book",views.issue_book, name='issue_book'),
    # path("view_issued_book",views.view_issued_book, name='view_issued_book'),
    
    #Backend Code
    path("stud/reg/",views.regprocess, name='regprocess'),
    path("loginadmin/view_stud_details",views.viewstuddetails, name='viewstuddetails'),
    path("loginadmin/delete/<int:id>",views.delprocess, name='delprocess'),
    path("loginadmin/edit/<int:id>",views.editprocess, name='editprocess'),
    path("update/<int:id>",views.updateprocess, name='updateprocess'),
    path("addbook/",views.addbookprocess, name='addbookprocess'),
    path("loginadmin/view_book",views.viewbooksprocess, name='viewbooksprocess'),
    path("deletebook/<int:id>",views.delbookprocess, name='delbookprocess'),
    path("editbook/<int:id>",views.editbookprocess, name='editbookprocess'),
    path("updatebook/<int:id>",views.updatebookprocess, name='updatebookprocess'),
    path("loginadmin/issue_book",views.showbookforissue, name='showbookforissue'),
    path("loginadmin/issuebook/",views.issuebookprocess, name='issuebookprocess'),
    path("loginadmin/deleteissuebook/<int:id>",views.delissuebookprocess, name='delissuebookprocess'),
    path("loginadmin/view_issued_book",views.viewissuebooksprocess, name='viewissuebooksprocess'),
    path("loginadmin/",views.adminlogin, name='adminlogin'),
    path("loginadmin/add_book",views.add_book, name='add_book'),
    path("loginadmin/stud_reg",views.stud_reg, name='stud_reg'),
    path("loginuser/",views.userlogin, name='userlogin'),
    path("student_view_book",views.studentviewbook, name='studentviewbook'),
    path("issue_book/",views.showbookforissue_student, name='showbookforissue_student'),
    path("save_issued_book/",views.issuebookprocess_student, name='issuebookprocess_student'),
    path("view_profile/",views.viewstudent_data, name='viewstudent_data'),
    path("edit_profile/<int:id>",views.editprocess_student, name='editprocess_student'),
    path("delete_profile/<int:id>",views.deleteprocess_student, name='deleteprocess_student'),
]
