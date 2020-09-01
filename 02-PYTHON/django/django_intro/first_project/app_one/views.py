from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
   return HttpResponse("Placeholder to later display a list of all blogs!")

def new(request):
   return HttpResponse("Placeholder to dispaly a new form to create a new blog")

def create(request):
   return redirect("/")

def show(request, num):
   return HttpResponse(f"Placeholder to display blog number: {num}")

def edit(request, num):
   return HttpResponse(f"Placeholder to edit blog number: {num}")

def destroy(request, num):
   return redirect("/")