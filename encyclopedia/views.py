from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from . import util
from markdown2 import Markdown

from .forms import editPage, NewForm

from .models import entries

from random import choice



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    entry_exist = util.get_entry(title)
    
    
    if entry_exist:
        #set markdown
        markdowner = Markdown()
        # convert and store the result in HTML
        html = markdowner.convert(entry_exist)
        
        return render (request, "encyclopedia/entry.html", {
            "entry": html,
            "title": title
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
        # redirect on the new entry
        return redirect("entry", title=title)
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
            # get list in database
            entries = util.get_entry(title)
            # Check for existing content
            if entries:
                return HttpResponseNotFound('<h1>Article already exist</h1>')
            
            # save the new entry as a file.md in entries/title.md
            print(title)
            print(entry)
            util.save_entry(title, entry)
            
            # redirect on the new entry
            return redirect("entry", title=title)

    # Propose a new empty form if it's not valid
    return render(request, 'encyclopedia/create.html', {
       "form": NewForm()
        })

def edit(request, name):
    
    if request.method == "POST":
        #store the user data in the class form format
        form = editPage(request.POST)
       
        
        if form.is_valid():
            title = form.cleaned_data["title"]
            textContent = form.cleaned_data["textContent"]
            # add in database
            # entries = util.get_entry(title)
            # save the new entry as a file.md in entries/title.md

            util.save_entry(title, textContent)
            
            # redirect on the new entry
            return redirect("entry", title=title)
  
    form = editPage(initial={'title': name, 'textContent': util.get_entry(name)})
    
    return render(request, "encyclopedia/edit.html", {
        "form": form,
    })

def random(request):
    entriesList = util.list_entries()
    choice_e = choice(entriesList)
    
    return redirect("entry", title=choice_e)