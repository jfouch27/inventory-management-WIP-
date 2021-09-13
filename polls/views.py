from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from datetime import datetime
import glob

from .models import Choice, Question, Host


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class HostView(TemplateView):
    template_name = "polls/dataTable.html"
    Host.objects.all().delete()
    HostTable = []
    for file in glob.glob("/home/jfouch/djangoProjects/mysiteOne/*.txt"):
        # newfile = open('test.txt', 'r')
        with open(file, "r") as i:
            fileLines = i.readlines()
        # for file in glob.glob('~/test.txt'):

        #    print(i.readLines())
        for j in range(len(fileLines)):
            HostTable.append(fileLines[j].split())

    for k in range(len(HostTable)):
        HostTable[k][2] = HostTable[k][2] + " " + HostTable[k][3]

        HostTable[k].insert(3, HostTable[k].pop(1))
        HostTable[k].pop(2)
        print(HostTable[k][1])
    HostTable.sort()
    for m in range(len(HostTable)):
        (newHost, created) = Host.objects.get_or_create(
            Ip_address=HostTable[m][0],
            inci_time=datetime.strptime(HostTable[m][1], "%Y-%m-%d %H:%M:%S"),
            port=HostTable[m][2],
        )
        newHost.save()

    def get_context_data(self, **kwargs):
        context = self.get_context_data(**kwargs)

        context["hosts"] = (
            Host.objects.all()
            .values("Ip_address", "inci_time", "port")
            .order_by(
                "-Ip_address",
            )
        )

        return context


def hostTable(request):
    # username = request.POST['username']
    # password = request.POST['password']
    Host.objects.all().delete()
    HostTable = []
    for file in glob.glob("/home/jfouch/djangoProjects/mysiteOne/*.txt"):
        # newfile = open('test.txt', 'r')
        with open(file, "r") as i:
            fileLines = i.readlines()
        # for file in glob.glob('~/test.txt'):

        #    print(i.readLines())
        for j in range(len(fileLines)):
            HostTable.append(fileLines[j].split())

    for k in range(len(HostTable)):
        HostTable[k][2] = HostTable[k][2] + " " + HostTable[k][3]

        HostTable[k].insert(3, HostTable[k].pop(1))
        HostTable[k].pop(2)
        print(HostTable[k][1])
    HostTable.sort()
    for m in range(len(HostTable)):
        (newHost, created) = Host.objects.get_or_create(
            Ip_address=HostTable[m][0],
            inci_time=datetime.strptime(HostTable[m][1], "%Y-%m-%d %H:%M:%S"),
            port=HostTable[m][2],
        )
        newHost.save()

    hostItem = Host.objects.all()
    context = {"host": hostItem}
    # host= Host.objects.all()
    return render(request, "polls/hostTable.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
