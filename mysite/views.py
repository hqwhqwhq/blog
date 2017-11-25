# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from models import Post
from datetime import datetime

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    context_dict = {}
    context_dict["posts"] = posts
    context_dict["now"] = now
    return render(request, "index.html", context_dict)

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, "post.html", {"post": post})
    except:
        return redirect("/")