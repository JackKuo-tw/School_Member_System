from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import datetime
from .models import Member

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=250)
    file = forms.FileField()

def import_uploaded_file(f):
    filename = f.name
    filename = filename + datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    text = "<h1>List of failed import</h1><br>"
    suc_counter = 0
    fail_counter = 0
    with open('uploads/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with open('uploads/' + filename, 'r') as destination:
        for line in destination:
            try:
                lineData = line.split()
                if(len(lineData)>3):        # 有些職稱跟在職狀況中間會有空白，所以將之合併
                    lineData[2] = lineData[2] + lineData[3]
                if(len(lineData)==3):
                    Member.objects.create(school_id=lineData[0], name=lineData[1], remark=lineData[2])
                elif(len(lineData)==2):
                    Member.objects.create(school_id=lineData[0], name=lineData[1])
                suc_counter = suc_counter + 1
            except:
                text = text + line + '<br>'
                fail_counter = fail_counter + 1
    text = 'Success: ' + str(suc_counter) + ' Failure: ' + str(fail_counter) + '<br>' + text
    return text

def check_uploaded_file(f):
    filename = f.name
    filename = filename + datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    text = "<h1>List of failed import</h1><br>"
    suc_counter = 0
    fail_counter = 0
    with open('uploads/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with open('uploads/' + filename, 'r') as destination:
        for line in destination:
            try:
                lineData = line.split()
                Member.objects.get(school_id=lineData[0])
                suc_counter = suc_counter + 1
            except:
                text = text + line + '<br>'
                fail_counter = fail_counter + 1
    text = 'Success: ' + str(suc_counter) + ' Failure: ' + str(fail_counter) + '<br>' + text
    return text

# Create your views here.
def importData(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():      
            text = import_uploaded_file(request.FILES['file'])
            return HttpResponse(text)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def checkData(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():      
            text = check_uploaded_file(request.FILES['file'])
            return HttpResponse(text)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

# def importData(request):
#     if 'user' in request.GET:
#         user = request.GET['user']
#         return render_to_response('importData.html',locals())
#     else:
#         return render_to_response('importData.html',locals())


'''
查詢特定長度
Member.objects.extra(where=['LENGTH(school_id)=5'])
ref = https://stackoverflow.com/questions/12314168/django-filter-on-the-basis-of-text-length

'''