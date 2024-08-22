from django import forms
from school.models import Questions, Admission


class QuestionsForm(forms.ModelForm):
    question = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Напишите вопрос'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите адрес эл. почты'
    }))

    class Meta:
        model = Questions
        fields = ('question', 'email')

class AdmissionForm(forms.ModelForm):
    student_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Имя ученика'
    }))
    parent_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Имя родителя'
    }))
    class_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Класс'
    }))
    student_pd = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'ПД ученика'
    }))
    parent_pd = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'ПД родителя'
    }))

    class Meta:
        model = Admission
        fields = ('student_name', 'parent_name', 'class_number', 'student_pd', 'parent_pd')