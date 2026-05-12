from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



# Global scope which you will get access to the entire application
# Empty Tasks List
# tasks = []

# Create a Form Here with the fields
class NewTaskForm(forms.Form):
    # Task label
    task = forms.CharField(label="New Task")
    # Client side validation: Priority is a new field added
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    # Create a session for each user with its own data
    if "tasks" not in request.session:
        # Create an empty list if the user don't have tasks on his session
        request.session["tasks"] = []
    # Render a template index.html and provide a context {}
    return render(request, "tasks/index.html", {
        # Key on the 
        "tasks": request.session["tasks"]
    })
    
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # form.cleaned_data help me to get all the data 
            # the user submitted and save it in a variable called task 
            task = form.cleaned_data["task"]
            # Append to the list of the Tasks
            # tasks.append(task)
            request.session["tasks"] += [task]
            # Redirect the user to the Task List Page after adding the task
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    # Render an empty form if the user just want to get the page.       
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })