from django.contrib.auth.models import User
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=500, widget=forms.Textarea)

    def clean(self):
        pass

    def save(self): 
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save
        return question
    

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean(self):
        pass

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput,required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Не задано имя пользователя')
        try:
            User.object.get(username=username)
            raise forms.ValidationError('Такой пользователь уже существует') 
        except User.DoesNotExist:
            pass
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Не указан адрес электронной почты')
        return email

    def clean_passwod(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Не указан пароль')
        self.raw_password = password
        return make_password(password)
    
    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,required=False)
    password = forms.CharField(widget=forms.PasswordInput,required=False)

    def clean_username(self):
        usename = self.cleaned_data.get('username')
        if not usename:
            raise forms.ValidationError('Не задано имя пользователя')
        return usename

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Не указан пароль')
        return password
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Неверное имя пользователя или пароль')
        if not user.check_password(password):
            raise forms.ValidationError('Неверное имя пользователя или пароль')