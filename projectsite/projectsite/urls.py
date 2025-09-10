"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView, StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    #ORGANIZATION
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    #ORGMEMBER
    path('OrgMember_List', OrgMemberList.as_view(), name='OrgMember-list'),
    path('OrgMember_List/add', OrgMemberCreateView.as_view(), name='OrgMember-add'),
    path('OrgMember_List/<pk>',OrgMemberUpdateView.as_view(), name='OrgMember-update'),
    path('OrgMember_List/<pk>/delete', OrgMemberDeleteView.as_view(), name='OrgMember-delete'),
    #STUDENT
    path('student_list', StudentList.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>',StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
]


