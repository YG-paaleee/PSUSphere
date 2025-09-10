from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from studentorg.forms import OrganizationForm, OrgMemberForm
from django.urls import reverse_lazy
from studentorg.models import Organization, OrgMember, Student, College, Program

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

#ORGANIZATION
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

#ORG MEMBER
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'OrgMember_list.html'
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'OrgMemberform.html'
    success_url = reverse_lazy('OrgMember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'OrgMemberform.html'
    success_url = reverse_lazy('OrgMember-list')

class OrgMemberDeleteView(DeleteView):  
    model = OrgMember
    template_name = 'OrgMember_del.html'
    success_url = reverse_lazy('OrgMember-list')