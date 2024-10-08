from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
'''def insert_topic(request):
    tn=input('Enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        return HttpResponse('New object is created')
    else:
        return HttpResponse('Already exists')

def insert_webpage(request):
    tn=input('enter topic_name: ')
    n=input('enter name: ')
    u=input('enter url: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)
    if WO[1]:
        return HttpResponse('New object is created')
    else:
        return HttpResponse('Already exists')

def insert_webpage(request):
    tn=input('enter topic_name: ')
    n=input('enter name: ')
    u=input('enter url: ')
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic=TO,name=n,url=u)
    return HttpResponse('Webpage is created')

def insert_AccessRecord(request):
    n=input('enter name: ')
    a=input('Enter author: ')
    d=input('Enter date: ')
    i=input('enter id: ')
    WO=Webpage.objects.get(id=i) 
    AC=AccessRecord.objects.get_or_create(id=i,name=WO,author=a,date=d)
    return HttpResponse('AccessRecord is created')

    # WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]

    # AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)
    # if AO[1]:
    #     return HttpResponse('New object is created')
    # else:
    #     return HttpResponse('Already object is there')'''
def insert_topic(request):
    tn=input('Enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        topics=Topic.objects.all()
        d={'topics':topics}
        return render(request,'display_topics.html',d)
    else:
        return HttpResponse('Topic is already exists') 
    
def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')

    QLTO=Topic.objects.filter(topic_name=tn)
    if QLTO:
        TO=QLTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)
        
        d={'webpages':Webpage.objects.all()}
        return render(request,'display_webpages.html',d)
        #return HttpResponse('Webpage is Created')
    else:
        return HttpResponse('Dear User Given Topic is Not Avaialble')

def insert_AccessRecord(request):
    i=int(input('enter id: '))
    a=input('enter author: ')
    d=input('enter date: ') 
    WO=Webpage.objects.get(id=i)
    if WO:
        # OBJ=WO[0]
        AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)
        d={'Access' : AccessRecord.objects.all()}
        return render(request,'display_accessrecords.html',d)
    else:
        return HttpResponse('data not created')


def display_topics(request):
    topics=Topic.objects.all().order_by(Length('topic_name'))
    topics=Topic.objects.filter(topic_name='koko').order_by('topic_name')
    topics=Topic.objects.exclude(topic_name='Ball')
    topics=Topic.objects.filter(topic_name__startswith='b')
    topics=Topic.objects.filter(topic_name__endswith='t')
    topics=Topic.objects.filter(topic_name__contains='t')
    topics=Topic.objects.filter(topic_name__regex='^C')
    d={'topics':topics}
    return render(request,'display_topics.html',d)
# display_accessrecords
def display_webpages(request):
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.filter(topic_name = 'Cricket').order_by(Length('name').desc())
    webpages=Webpage.objects.exclude(topic_name='Cricket')
    webpages=Webpage.objects.exclude(topic_name='cricket')
    webpages=Webpage.objects.filter(name__startswith='P')
    webpages=Webpage.objects.filter(name__endswith='z')
    webpages=Webpage.objects.filter(url__startswith='h')
    webpages=Webpage.objects.filter(url__endswith='in')
    webpages=Webpage.objects.filter(name__regex='^j')

    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    accessrecords=AccessRecord.objects.all().order_by('-date')
    accessrecords=AccessRecord.objects.filter().order_by(Length('name').desc())
    accessrecords=AccessRecord.objects.exclude(id='2').order_by(Length('id').desc())
    accessrecords=AccessRecord.objects.filter(date__lte='2024-12-12')
    accessrecords=AccessRecord.objects.filter(author__startswith='P')
    accessrecords=AccessRecord.objects.filter(author__regex='^P')
    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)


def topicweb(request):
    TWO=Topic.objects.prefetch_related('webpage_set').all()
    d={'TWO':TWO}
    return render(request,'topicweb.html',d)

def webaccess(request):
    WAO=Webpage.objects.prefetch_related('accessrecord_set').all()
    WAO=Webpage.objects.prefetch_related('accessrecord_set').filter(name='roshan')
    WAO=Webpage.objects.prefetch_related('accessrecord_set').filter(url='https://parvez.in')
    d={'WAO':WAO}
    return render(request,'webaccess.html',d)
