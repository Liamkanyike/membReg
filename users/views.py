from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from Regapp.models import Church
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound


@login_required
def dashboard(request):
	church_count=Church.objects.all().count()
	member_count=Church.objects.order_by().count()


	church = Church.objects.order_by('-id')[0:10]
	return render(request, "users/dashboard.html",{'church':church, 'church_count':church_count, 'member_count':member_count})




def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! Your are now able to Log In')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request,'users/registration.html',{'form':form})



