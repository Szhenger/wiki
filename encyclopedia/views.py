from django.shortcuts import render, redirect
from django.urls import reverse
from markdown2 import Markdown
from random import choice

from . import util


def md_to_html(title):
    """
    Input: Gets a title (string)
    Output: Returns entry content of title from Markdown to HTML or None
    """
    content = util.get_entry(title)
    if not content:
        return None
    markdowner = Markdown()
    return markdowner.convert(content)

def index(request):
    """Returns the CS50 Encyclopedia Homepage"""
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    """
    Inputs: Gets request (dictionary) and title (string)
    Output: Returns the entry corresponding to title
    """
    content = md_to_html(title)
    if not content:
        return render(request, "encyclopedia/error.html", {
            "error": "HTTP 404 Error",
            "message": "This entry does not exist"
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": content
    })

def search(request):
    """
    Input: Gets a request (dictionary)
    Output: Returns exact query entry in the request or substring results
    """
    entries = util.list_entries()
    if request.method == "POST":
        q = request.POST['q'].lower()
        results = []
        for entry in entries:
            if q == entry.lower():
                return render(request, "encyclopedia/entry.html", {
                    "title": entry,
                    "entry": md_to_html(entry)
                })
            elif q in entry.lower():
                results.append(entry)
        return render(request, "encyclopedia/search.html", {
            "results": results
        })
    return redirect("index")

def new(request):
    """
    Input: Gets a request (dictionary) of new title and contents
    Side Effect: Makes a new page of request if it does not already exist
    Output: Returns to the CS50 Encyclopedia Homepage
    """
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if not title or not content:
            return render(request, "encyclopedia/new.html")
        entries = util.list_entries()
        for entry in entries:
            if title.lower() == entry.lower():
                return render(request, "encyclopedia/error.html", {
                    "error": "HTTP 403 Error",
                    "message": "This entry already exists"
                })
        util.save_entry(title, content)
        return redirect("index")
    return render(request, "encyclopedia/new.html")

def edit(request, title):
    """
    Input: Gets request (dictionary) and title (string)
    Side Effect: Edits a page of title
    Output: Returns to the CS50 Encyclopedia Homepage
    """
    if request.method == "POST":
        content = request.POST["content"]
        if not content:
            return render(request, "encyclopedia/error.html", {
                "error": "HTTP 403 Error",
                "message": "There must be contents of the entry"
            })
        util.save_entry(title, content)
        return redirect("index")
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": util.get_entry(title)
    })

def random(request):
    """
    Input: Gets request (dictionary)
    Output: Returns a random entry
    """
    entries = util.list_entries()
    title = choice(entries)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": md_to_html(title)
    })
