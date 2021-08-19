
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models.expressions import F
from ask.qa.forms import LoginForm, SignupForm
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.urls import reverse
from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm

# Create your views here.

def question(request,num):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            q = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': q.id})
    return render(request, 'question.html', {'question': q,
                                             'form': form,
                                             'user': request.user,
                                              })


def index(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'index.html',
                  {'title': 'Latest',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
				  })

def popular(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-rating')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'index.html',
                  {'title': 'Popular',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                    })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request,'ask.html',{'form': form,
                                      'user':request.user,
                                      })

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username,password)
            user = authenticate(username=username,password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form,
                                        'user':request.user,
                                        'session':request.session})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid:
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.raw_password
            user = authenticate(username=username,password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm
    return render(request,'signup.html',{'form':form,
                                         'user':request.user,
                                         'session':request.session})