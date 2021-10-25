from django.shortcuts import render
from .models import Host, OpenPort
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.forms import forms
from datetime import datetime
import glob

from .models import Host
from users.models import User
from .forms import LoginForm
# Create your views here.


class IndexView(generic.ListView):
    template_name = "hosts/index.html"
    def get_queryset(self):
        """Return the last five published questions."""
        return HttpResponseRedirect('/hosts/login/')

class LoginView(generic.FormView):
    form_class = LoginForm
    #success_url = reverse('host')
    template_name = 'hosts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            print("yes")
            #return super(LoginView, self).form_valid(form)
            return HttpResponseRedirect('/hosts/hostTable/')
        else:
            return self.form_invalid(form)           
@login_required()  
def hostTable(request):
    Host.objects.all().delete()
    HostTable = []
    for file in glob.glob("/home/jfouch/djangoProjects/ois_asset_inventory/*.txt"):
        # newfile = open('test.txt', 'r')
        with open(file, "r") as i:
            fileLines = i.readlines()
        # for file in glob.glob('~/test.txt'):

        #    print(i.readLines())
        for j in range(len(fileLines)):
            HostTable.append(fileLines[j].split())

    for k in range(len(HostTable)):
        HostTable[k][2] = HostTable[k][2] + " " + HostTable[k][3]

        HostTable[k].insert(3, HostTable[k].pop(1))
        HostTable[k].pop(2)
        
    HostTable.sort()
    for m in range(len(HostTable)):
        (newHost, created) = Host.objects.get_or_create(
            ip=HostTable[m][0],
            time=datetime.strptime(HostTable[m][1], "%Y-%m-%d %H:%M:%S"),
            port=HostTable[m][2],
        )
        newHost.save()

    hostItem = Host.objects.all()
    context = {"host": hostItem}
    return render(request, "hosts/hostTable.html", context)