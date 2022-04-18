from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

# Create your views here.
# def register(request):
#     return render(request, 'register.html')

# def login(request):
#     return render(request, 'login.html')

# def logout(request):
#     return render(request, 'logout.html')