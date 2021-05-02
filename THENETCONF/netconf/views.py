from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Participant, Program, Partner, CommitteeMember, Contact
# Create your views here.


class Intro(ListView):

    model = Participant
    template_name ="home/index.html"
    

def index(request):
    researcher = Participant.objects.all()
    partner = Partner.objects.all()
    # presenters = Researcher.objects.get(presenter='Presenter')

    # print(partner.name)
    context= {'researchers':researcher, 'partners':partner}
    return render(request,'home/index.html',context)

def program(request):

    progi = Program.objects.filter(day=1)
    progi2 = Program.objects.filter(day=2)
    progi3 = Program.objects.filter(day=3)
    progi4 = Program.objects.filter(day=4)
    
    context= {
        'progi1':progi,
        'progi2':progi2,
        'progi3':progi3,
        'progi4':progi4,
            }

    return render(request,'home/program.html',context)

def committee(request):
    committee = CommitteeMember.objects.all()
    context= {
        'comm':committee,}
    return render(request,'home/committee.html',context)

def contact(request):

    if "send" in request.POST:
        mname = request.POST["name"]
        memail = request.POST["email"]
        msg = request.POST["message"] 
        
        contact = Contact(name=mname,email=memail,message=msg)

        contact.save()

        print("Inserrrteedddd............")
        messages.success(request,"Success: Your Message has been delivered successfully")
        return render(request, "home/contact.html")
    
    return render(request,'home/contact.html')

def register(request):

    if "register" in request.POST:
        name = request.POST["name"]
        title = request.POST["title"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        presenter = request.POST["presenter"]
        topic_to_Present = request.POST["topictopresent"]
        topic_description = request.POST["description"]
        picture = request.POST["pic"]
        
        participant = Participant(
            name              =name,
            title             =title,
            email             =email,
            phone             =phone,
            address           =address,
            presenter         =presenter,
            topic_to_Present  =topic_to_Present,
            topic_description =topic_description,
            picture           =picture,
)

        participant.save()

        print("Inserrrteedddd............")
        messages.success(request,"Success: You have successfully been Registered!!! ")
        return render(request, "home/register.html")
    
    return render(request,'home/register.html')