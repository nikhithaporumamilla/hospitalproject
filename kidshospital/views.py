from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, your on kids hospital page")


def about(request):
    data = {"About": "Childrens hospital caring to all needs of children in a child friendly environment"}

    return render(request, "kidshospital/about.html", data)


def contactus(request):
    if request.method == "GET":
        return render(request, "kidshospital/contactus.html")
    elif request.method == "POST":
        print(request.POST)
        return HttpResponse("Your appointment booked successfully")

    return render(request, "kidshospital/contactus.html")


def details(request):

    return render(request, "kidshospital/details.html")
