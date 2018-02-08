from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, reverse


# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('poll/index.html')
	context = {
		'latest_question_list':latest_question_list
	}

	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'poll/detail.html', {'question':question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'poll/results.html', {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'poll/detail.html', {'question':question, 'error_message':"선택하라고..."})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))