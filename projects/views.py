# projects/views.py
from django.shortcuts import render
from projects.models import Project


# query to retrieve all objects in the projects table
# define a dictionary named context
# the dictionary has only one entry; projects,
# which we assign our queryset containing all the projects
# Django uses context dictionary to send info to the template.
# Adding context as an argument to render(). this makes any entries
# in the context available in the template
# We will need to create a context dictionary and pass it to
# render() in each view function that we create
# we also add path to the html template to render() .

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)


# project_detail()
# this function has the primary key of the project that is being viewed
# .

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)
