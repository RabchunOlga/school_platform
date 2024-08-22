from django.contrib import admin
from school.models import News, Questions, Teachers, Licenses, Awards, Admission

# Register your models here.
admin.site.register(News)
admin.site.register(Questions)
admin.site.register(Teachers)
admin.site.register(Licenses)
admin.site.register(Awards)
admin.site.register(Admission)
