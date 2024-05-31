from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Note

# Create your views here.

def signup(request):

    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        ps = request.POST.get("ps")
        

        new_user = User.objects.create(
            username = username,
            first_name= first_name,
            last_name= last_name

        )

        new_user.set_password(ps)

        new_user.save()
        return redirect("dashboard")




    

    return render(request, "signup.html")

def login(request):
     if request.method == "POST":
        username = request.POST.get("username")
        ps = request.POST.get("ps")

        user=auth.authenticate(username=username, password=ps)

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            return redirect("invalid")



     return render(request, "login.html")
def success(request):
    return render(request, "success.html")
def invalid(request):
    return render(request, "invalid.html")
def dashboard(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")

        new_note = Note.objects.create(
            title=title,
            desc=desc,
        )

        new_note.save()
        return redirect("notes")
    return render(request, "dashboard.html")
    
       
def notes(request):

    user=request.user
    notes=Note.objects.all()
    parameter={
        "user":user,
        "notes":notes
    }
    return render(request, "notes.html", parameter)
    

def edit_note(request, id):
    note = Note.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")

        note.title = title
        note.desc = desc

        note.save()

    return render(request, "edit_note.html")
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()

    return redirect("notes")
