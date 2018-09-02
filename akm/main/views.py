from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from akm.emergency.models import Emergency

@login_required
def index(request):
    list_emergency = Emergency.objects.all()
    return render(request,'mainpage.html',{"emergency":list_emergency})



def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')
