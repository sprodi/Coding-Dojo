from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def index(request):
   return redirect('/shows')

def new_show(request):
   context = {
      'shows': Show.objects.all()
   }
   return render(request, 'new_show.html', context)

def create_show(request):
      Show.objects.create(
         title = request.POST['title'],
         network = request.POST['network'],
         release_date = request.POST['release_date'],
         desc = request.POST['desc']
         )
      return redirect(f'/shows')

def view_show(request, show_id):
   context = {
      'show': Show.objects.get(id = show_id)
   }
   return render(request, 'view_show.html', context)

def all_shows(request):
   context = {
      'shows': Show.objects.all()
   }
   return render(request, 'all_shows.html', context)

def edit_show(request, show_id):
   show_to_edit = Show.objects.get(id = show_id)
   context = {
      'show': show_to_edit
   }
   return render(request, 'edit_show.html', context)

def update_show(request, show_id):
   show_to_update = Show.objects.get(id = show_id)
   show_to_update.title = request.POST["title"]
   show_to_update.network = request.POST["network"]
   show_to_update.release_date = request.POST["release_date"]
   show_to_update.desc = request.POST["desc"]
   show_to_update.save()
   return redirect('/shows')

def delete_show(request, show_id):
   show_to_delete = Show.objects.get(id = show_id)
   show_to_delete.delete()
   return redirect('/')