from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext

@login_required
def index(request):
    return render(request,'mainpage.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')
