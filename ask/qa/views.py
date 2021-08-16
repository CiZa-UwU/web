from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator

from qa.models import Question, Answer

# Create your views here.

def question(request, num,):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question.html', {'question': q,
                                              })


def index(request,**args):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-addet_at')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'index.html',
                  {'title': 'Latest',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
				  })

def popular(request,**args):
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
