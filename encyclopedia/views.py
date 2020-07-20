from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    entry_exist = util.get_entry(title)
    
    
    if entry_exist:
  
        return render (request, "encyclopedia/entry.html", {
            "entry": entry_exist
        })
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    


