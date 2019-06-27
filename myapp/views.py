from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from myapp.models import Employee


class createviews(CreateView):
    model =Employee
    fields = ['eid','ename','eemail','econtact','uplode_images']
    template_name = 'cretae.html'


class listlsviews(ListView):
    model = Employee
    fields = ['eid', 'ename', 'eemail', 'econtact']
    template_name = 'list.html'


class deleteviw(DeleteView):
    model = Employee
    template_name ='delete.html'
    success_url = reverse_lazy(list)






