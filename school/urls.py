from django.contrib import admin
from django.urls import path, include
from school.views import index, teachers, about_us, admission, news_one, paid_services, departments, requirements, equipment, scholarship

app_name = 'school'

urlpatterns = [
    path('page/<int:page>', index, name='paginator'),
    path('teachers/', teachers, name='teachers'),
    path('about-us/', about_us, name='about_us'),
    path('admission/', admission, name='admission'),
    path('news/<int:news_id>', news_one, name='news_one'),
    path('paid_services/', paid_services, name='paid_services'),
    path('departments/', departments, name='departments'),
    path('requirements/', requirements, name='requirements'),
    path('equipment/', equipment, name='equipment'),
    path('scholarship/', scholarship, name='scholarship'),
]
