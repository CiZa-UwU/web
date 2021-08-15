from django.http import HttpResponse 
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from qa.models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')  

def question(request,num,title,text):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    return render(request,'question.html',
    {
    'question':q, 
    'title':title,
    'text':text
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
    return render(request,'list.html',{
        'title':'latest',
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
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request,'list.html',{
        'title':'popular',
        'paginator': paginator,
        'questions': page.object_list,
        'page': page,
    }) 