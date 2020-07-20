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
            "entry": entry_exist,
            "title":title
        })
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def get_entry(request):
    search = request
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.GET)
        return render(request, 'search_result.html')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'search_result.html')



