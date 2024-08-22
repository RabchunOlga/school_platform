from django.shortcuts import render
from school.models import News, Teachers, Licenses, Awards
from django.core.paginator import Paginator
from school.forms import QuestionsForm, AdmissionForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


def index(request, page=1):
    news = News.objects.all()
    per_page = 3
    paginator = Paginator(news, per_page)
    news_paginator = paginator.page(page)

    if request.method == 'POST':
        form = QuestionsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = QuestionsForm()

    context = {
        'news': news_paginator,
        'form': form
    }
    return render(request, 'school.html', context)

def teachers(request):
    context = {
        'teachers': Teachers.objects.all()
    }
    return render(request, 'teachers.html', context)

def about_us(request):
    context = {
        'licenses': Licenses.objects.all(),
        'awards': Awards.objects.all()
    }
    return render(request, 'about_us.html', context)

def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('school:admission'))
    else:
        form = AdmissionForm()

    context = {
        'form': form
    }
    return render(request, 'admission.html', context)

def news_one(request, news_id):
    context = {
        'news_one': News.objects.get(id=news_id),
    }
    return render(request, 'news_one.html', context)

def paid_services(request):
    return render(request, 'paid_services.html')

def departments(request):
    return render(request, 'departments.html')

def requirements(request):
    return render(request, 'requirements.html')

def equipment(request):
    return render(request, 'equipment.html')

def scholarship(request):
    return render(request, 'scholarship.html')