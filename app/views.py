from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse




def insert_user_data(request):
    d={'to':TopicForm(),'wo':WebpageForm(),'ao':AccessrecordForm()}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessrecordForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():

            NSTO=tfd.save(commit=False)
            NSTO.save()


            NSWO=wfd.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()

            NSAO=afd.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()

            return HttpResponse('data inserted successfull')
        else:
            return HttpResponse('data is not valid')

    return render(request,'insert_user_data.html',d)