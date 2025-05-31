from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from department.models import Department


# Create your views here.
def index(request):
    return HttpResponse('<h1>Departments Home page</h1>')


def int_param_view(request, pk):
    return HttpResponse(f'<h1>Department Index: {pk}</h1>')


def string_param_view(request, name):
    return HttpResponse(f'<h1>Department Name: {name}</h1>')


def slug_param_view(request, slug):
    # Option 1
    # department = Department.objects.filter(slug=slug).first()
    # if not department:
    #     raise Http404
    # Option 2
    department = get_object_or_404(Department, slug=slug)

    return render(request, 'slug_tamplates.html', {'department': department})


def file_path_param_view(request, path_to_file):
    return HttpResponse(f'<h1>The file is located at: {path_to_file}</h1>')


def uuid_param_view(request, id):
    return HttpResponse(f'<h1>The id is: {id}</h1>')


def regex_view(request, archive_year):
    return HttpResponse(f'<h1>The year is {archive_year}</h1>')


# def redirect_view(request):
#     return redirect('https://softuni.bg', permanent=True)
def contacts_view(request):
    # print(reverse_lazy('contacts'))
    return HttpResponse(f'<h1>We are department</h1>')


def about_view(request):
    return redirect('contacts', permanent=True)



