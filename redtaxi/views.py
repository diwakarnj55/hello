from django.shortcuts import render, redirect
from . models import FavCars, Department
from . forms import contactForm

def index(request):
    fav=FavCars.objects.all()
    dep=Department.objects.all()
    con=contactForm()
    data ={
        "fav":fav,
        "dep":dep,
        "con":con,
    }
    if request.method=="POST":
        contact=contactForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect("home")
    return render(request,"index.html",data)
