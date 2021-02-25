from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect    #,Http404
#from django.template import loader
from .models import Question, Choice

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template= loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list, }
    #output = ','.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse('you are looking at question %s' % question_id)


def results(request, question_id):
    return HttpResponse('you are looking at result of question %s' % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html' ,{'question':question, error_message:'You didnt selsect a choice',})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reversed('polls:results', args=(question.id )))

