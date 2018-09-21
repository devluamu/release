# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.core.urlresolvers import reverse

from .models import NoticePost

def index(request):
    latest_post_list = NoticePost.objects.order_by('-pub_date')[:4]
    template = loader.get_template('muorigin/index.html') 
    context = {'latest_post_list': latest_post_list}
    return render(request, 'muorigin/index.html', context)

def payment(request):
    return render(request, 'muorigin/payment.html')

def event(request):
    return render(request, 'muorigin/event.html')

def notice(request):
    post_list = NoticePost.objects.order_by('-pub_date')[:]
    context = {'latest_post_list': post_list}
    return render(request, 'muorigin/notice.html', context)

# Create your views here.
