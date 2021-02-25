from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello world')


def detail(request, question_id):
    return HttpResponse('you are looking at question %s' % question_id)


def results(request, question_id):
    return HttpResponse('you are looking at resualt of question %s' % question_id)


def vote(request,question_id):
    return HttpResponse('you are voting on question %s' % question_id)

