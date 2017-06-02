# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1>This is the Music app homepage</h1>")

def detail(request,album_id):
    return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")