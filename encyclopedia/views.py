from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from . import util
import markdown2

from .forms import editPage, NewForm

from .models import entries




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    entry_exist = util.get_entry(title)
    
    
    if entry_exist:
  
        return render (request, "encyclopedia/entry.html", {
            "entry": entry_exist,
            "title":title
        })
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')




def search(request):
    # get the string in the field
    query = request.GET.get('q').lower()
    # print(query)
    entry_exist = util.get_entry(query)
    # check if the query is egual to an exeisting entry
    if entry_exist:
        return render (request, "encyclopedia/entry.html", {
            "entry": entry_exist,
            "title":query
        })
    else:
        #get the list of existing entries
        entries = util.list_entries()
        result = []
        for entry in entries:

            if query in entry.lower():
                result.append(entry)
        
        return render(request, "encyclopedia/search.html", {
        "search": result
    })  

def create(request): #create a new page

    if request.method == "POST":
        #store the user data in the class form format
        form = NewForm(request.POST)
       
        
        if form.is_valid():
            title = form.cleaned_data["title"]
            entry = form.cleaned_data["entry"]
            # add in database
            entries = util.get_entry(title)
            # Check for existing content
            if entries:
                return HttpResponseNotFound('<h1>Article already exist</h1>')
            
            # save the new entry as a file.md in entries/title.md

            util.save_entry(title, entry)
            
            # redirect on the new entry
            return redirect("entry", title=title)

    # Propose a new empty form if it's not valid
    return render(request, 'encyclopedia/create.html', {
       "form": NewForm()
        })

def edit(request, name):
    
    print(name)
  
    editForm = editPage()
    editForm = editPage(initial={'title': name, 'textContent': util.get_entry(name)})
    
    return render(request, "encyclopedia/edit.html", {
        "editForm": editPage(),
    })