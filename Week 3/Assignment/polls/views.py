from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect, reverse
from polls.models import Question,  Choice
from django.views import generic

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def owner(request):
    return HttpResponse("Hello, world. <YOUR_STRING_HERE> is the polls owner.") # replace <YOUR_STRING_HERE> with the string you get when submitting assignment
