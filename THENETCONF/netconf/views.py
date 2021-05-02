from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Participant, Program, Partner
# Create your views here.


class Intro(ListView):

    model = Participant
    template_name ="home/index.html"
    

def index(request):
    researcher = Participant.objects.filter(presenter='Presenter').all()
    partner = Partner.objects.all()
    # presenters = Researcher.objects.get(presenter='Presenter')

    print(partner.name)
    context= {'researchers':researcher, 'partners':partner}
    return render(request,'home/index.html',context)

def program(request):

    return render(request,'home/program.html')

def committee(request):

    return render(request,'home/committee.html')