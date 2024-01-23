from datetime import datetime

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from Akaka.models import Content

from Akaka.HedHunter_api import HH_api


# Create your views here.

class Home(View):

    def get(self, request):
        context_object = Content.objects.all().first()
        return render(request, 'home.html', context={'content': context_object})

class Popular(View):
    def get(self, request):
        context_object = Content.objects.all().first()

        return render(request, 'popularity.html', context={'content': context_object})

class Areas(View):
    def get(self, request):
        context_object = Content.objects.all().first()

        return render(request, 'geography.html', context={'content': context_object})

class Skills(View):
    def get(self, request):
        return render(request, 'skills.html')

class LastVacancies(ListView):
    def get(self, request):
        vacancies = HH_api.get_full_vacancies(str(datetime.now()).split(' ')[0], 10)
        return render(request, 'last-vacancies.html', context={'vacancies': vacancies})