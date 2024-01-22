from django.shortcuts import render
from django.views import View

# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

class Popular(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'popularity.html')

class Areas(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'geography.html')

class Skills(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'skills.html')