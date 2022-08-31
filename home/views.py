
import email
import imp
from unicodedata import name
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import video
from .models import video_10
from .models import video_11ip
from .models import video_11cs
from .models import video_12ip
from .models import video_12cs

def index(request):
    return render(request,'index.html')
def about(request):
   return render(request,'about.html')
def syllabus(request):
    return render(request,'syllabus.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()

    return render(request,'contact.html')

def class9(request):
    return render(request,'class9.html')
def class10(request):
    return render(request,'class10.html')
def ip_class11(request):
    return render(request,'ip_class11.html')
def ip_class12(request):
    return render(request,'ip_class12.html')
def comp_class11(request):
    return render(request,'comp_class11.html')
def comp_class12(request):
    return render(request,'comp_class12.html')
def class9_book(request):
    return render(request,'class9_book.html')
def class10_book(request):
    return render(request,'class10_book.html')
def ip_11_book(request):
    return render(request,'ip_11_book.html')
def comp11_book(request):
    return render(request,'comp11_book.html')
def ip_12_book(request):
    return render(request,'ip_12_book.html')
def comp12_book(request):
    return render(request,'comp12_book.html')
def class9_video(request):
    videos=video.objects.all()
    return render(request,'videos/class9_video.html',context={'videos':videos} )
def class10_video(request):
    videos=video_10.objects.all()
    return render(request,'videos/class10_video.html',context={'videos':videos} )
def class11_ip_video(request):
    videos=video_11ip.objects.all()
    return render(request,'videos/class11_ip_video.html',context={'videos':videos} )
def class11_cs_video(request):
    videos=video_11cs.objects.all()
    return render(request,'videos/class11_cs_video.html',context={'videos':videos} )
def class12_ip_video(request):
    videos=video_12ip.objects.all()
    return render(request,'videos/class12_ip_video.html',context={'videos':videos} )
def class12_cs_video(request):
    videos=video_12cs.objects.all()
    return render(request,'videos/class12_cs_video.html',context={'videos':videos} )
def pro12_ip(request):
    return render(request,'programs/pro12_ip.html')


# Create your views here.
   