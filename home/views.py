from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .filehandler import handle_uploaded_file
from .forms import ModelFormWithFileField


def upload_file(request):
    if request.method == 'POST':
        for key in request.FILES:
            if handle_uploaded_file(request.FILES[key]) :
                return HttpResponse('OK')
            else:
                return HttpResponse('FAIL')
    else:
        form = UploadFileForm()
        return render(request, 'httpTest.html', {'form': form})




def index(request):
    if request.method=='POST':
        return upload_file(request)
    elif request.method=='GET':
        return render(request, 'send.html',{'poset':'post check'})
        #return HttpResponse("GET!")
    else:
        return HttpResponse("not POST,GET")
# Create your views here.
