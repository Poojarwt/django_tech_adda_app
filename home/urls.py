from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.index, name='home'),
    path("about",views.about, name='about'),
    path("syllabus",views.syllabus, name='syllabus'),
    path("contact",views.contact, name='contact'),
    path("class9",views.class9, name='class9'),
    path("class10",views.class10, name='class10'), 
    path("ip_class11",views.ip_class11, name='ip_class11'), 
    path("ip_class12",views.ip_class12, name='ip_class12'),
    path("comp_class11",views.comp_class11, name='comp_class11'),
    path("comp_class12",views.comp_class12, name='comp_class12'),
    path("class9_book",views.class9_book, name='class9_book'),
    path("class10_book",views.class10_book, name='class10_book'),
    path("ip_11_book",views.ip_11_book,name='ip_11_book'),
    path("ip_12_book",views.ip_12_book,name='ip_12_book'),
    path("comp11_book",views.comp11_book, name='comp11_book'),
    path("comp12_book",views.comp12_book, name='comp12_book'),
    path("videos/class9_video",views.class9_video, name='class9_video'),
    path("videos/class10_video",views.class10_video, name='class10_video'),
    path("videos/class11_ip_video",views.class11_ip_video, name='class11_ip_video'),
    path("videos/class11_cs_video",views.class11_cs_video, name='class11_cs_video'),
    path("videos/class12_ip_video",views.class12_ip_video, name='class12_ip_video'),
    path("videos/class12_cs_video",views.class12_cs_video, name='class12_cs_video'),
    path("programs/pro12_ip",views.pro12_ip, name='pro12_ip'),
]