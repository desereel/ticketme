from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def index(request):
	
	context = {}
	return render(request, 'index.html', context=context)

def register(request):

	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()


			messages.success(request, f'Your account has been created. You may login now!')
			return redirect('login')

	else:
		form = UserRegistrationForm()


	context = {'form': form}

	return render(request, 'registration/register.html', context)
