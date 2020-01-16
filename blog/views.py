from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Blogpost

# Create your views here

class Bloglist(ListView):
    queryset = Blogpost.objects.all()
    template_name = 'BOLG.html'

class Blogdetail(DetailView):
    queryset = Blogpost.objects.all()
    template_name = 'detail.html'