from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


from . import util
import markdown2
from .forms import NameForm


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
    print(query)
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

def create(request):
    return render(request, "encyclopedia/create.html")

def validate(request):
        
        #lower case for comparaison
        title = request.GET.get('title').lower()
        entry = request.GET.get('entry').lower()
        
        #get the list of existing entries
        entries = util.get_entry(title)
        if entries:
            return HttpResponseNotFound('<h1>Article already exist</h1>')
    
        util.save_entry(title.upper(), entry)
        
        #return the updated list
        
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def edit(request):
    title = request.GET.get('title')
    entry = request.GET.get('entry')
    
    return render(request, 'encyclopedia/edit.html', {
        'title': title,
        'entry': entry
        })