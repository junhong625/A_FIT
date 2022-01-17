
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .filehandler import handle_uploaded_file
from .forms import ModelFormWithFileField
from .form_check import form_check
from django.http import JsonResponse
import glob
import os, shutil

def upload_file(request):

    for key in request.FILES:
        if handle_uploaded_file(request.FILES[key]) :
            filepath = glob.glob('/home/ubuntu/testpj/media/*')
            return form_check(filepath)
            #return image_upload_view(request)
            #return HttpResponse(simplejson.dumps(image()))
        else:
            return HttpResponse('FAIL')



def index(request):
    if request.method=='POST':
        
        resultdict = upload_file(request)
        
        files = glob.glob('/home/ubuntu/testpj/media/*')
        for i in files:
            os.remove(i)
       
        if os.path.exists('/home/ubuntu/testpj/AIPT'):
            shutil.rmtree('/home/ubuntu/testpj/AIPT')
        
        return JsonResponse(resultdict, json_dumps_params={'ensure_ascii': False})
        #return upload_file(request)
    elif request.method=='GET':
        return JsonResponse({'get':'get!'})
        #return render(request, 'send.html',{'POST':'POST CHECK'})
    else:
        return HttpResponse("not POST,GET")
