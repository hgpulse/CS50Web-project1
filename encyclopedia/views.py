from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    entry_exist = util.get_entry(title)
    titleMd = re.compile('#.*', re.MULTILINE)
    if entry_exist:
        titleHtml = titleMd.fullmatch(entry_exist)
        return render (request, "encyclopedia/entry.html", {
            "entry": entry_exist,
            "titleHtml" : titleMd.findall(entry_exist)
        })
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    


