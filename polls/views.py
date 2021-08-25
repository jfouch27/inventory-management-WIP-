from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from datetime import datetime
import glob

from .models import Choice, Question, Host


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def hostTable(request):
    HostTable=[]
    
    newfile = open('test.txt', 'r')
    with open('test.txt','r') as i:
        fileLines = i.readlines()
    #for file in glob.glob('~/test.txt'):
    
        #    print(i.readLines())
    for j in range(len(fileLines)):
        HostTable.append(fileLines[j].split())
    
    for k in range(len(HostTable)):
        HostTable[k].insert(3,HostTable[k].pop(1))
        print(HostTable[0][1])
    HostTable.sort()
    (newHost, created) = Host.objects.get_or_create(
    Ip_address=HostTable[0][0],
    inci_date=datetime.strptime(HostTable[0][1], '%Y-%m-%d').date(),
    inci_time=datetime.strptime(HostTable[0][2], '%H:%M:%S'),
    port=HostTable[0][3],)
    newHost.save()
    #host= Host.objects.all()
    return render(request,'polls/hostTable.html', {'host': newHost})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))