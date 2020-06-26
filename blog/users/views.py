from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
            # return HttpResponse("suucessfully registered")
    else:
        form = UserRegisterForm()
    return render(request, 'user_register.html', {'form': form})

@login_required
def SearchView(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        print(search)
        results = User.objects.filter(username__contains=search)
        context = {
            'results':results
        }
        return render(request, 'user_search_result.html', context)

