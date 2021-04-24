from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.models import *
# Create your views here.
@login_required(login_url="/accounts/signin/")
def list(request):
	task=Task.objects.all()
	context={'tasks':task}
	return render(request, 'frontend/list.html',context)