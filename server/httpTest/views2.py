from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .filehandler import handle_uploaded_file
from .forms import ModelFormWithFileField
from .hello import hello
from .form_check import form_check

import cv2, sys
#import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance, ImageChops
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.models import Sequential, load_model
import os
from django.http import JsonResponse
#import simplejson

result = ''
model = load_model('/home/ubuntu/testpj/models/train_model.h5')

def upload_file(request):
        for key in request.FILES:
            if handle_uploaded_file(request.FILES[key]) :
                #return HttpResponse(hello())
                return image_upload_view(request)
                #return HttpResponse('OK')
            else:
                return HttpResponse('FAIL')



def index(request):
    
    if request.method=='POST':
        return upload_file(request)
    elif request.method=='GET':
        return JsonResponse({'get':'get!'})
        #return HttpResponse('GET!')
        #return render(request, 'test.html',{'POST':'POST CHECK'})

def image_upload_view(request):
    global result

    folder = "/home/ubuntu/testpj/media"
    file_list = [x for x in os.listdir(folder)]

   #  file = r'/home/ubuntu/bigdata-final/ImgProcessing/media/media/images/testFile.jpg'
    file = folder + '/' + file_list[-1]

    X = []
    img = Image.open(file)
    img = img.resize((400, 400))
    img = img.convert("RGB")
    data = np.asarray(img)
    X.append(data)

    X = np.array(X)
    new_prediction = model.predict(X)
    pre_ans = new_prediction[0].argmax()  # 예측  레이블


    # 임시로 기준값 정하기(나중에 필히 수정)
    if pre_ans==0:
       result = 'squat'
       test = form_check(file)
    else:
       result = 'stand'

    #print(test.items())
    
    # 어디까지나 3개월 프로젝트이고 귀찮아서 쓴것 뿐, 현업에서는 절대 쓰지 말아야 하는 코드
    # if os.path.exists(file):
        # os.remove(r'/home/ubuntu/bigdata-final/ImgProcessing/media/media/images/testFile.jpg')

    # else:
        # pass
    #awb_dict = {'result':result}
    awb_dict = test
    
    #return render(request,folder+'/'+file_list[-1],{'POST':'POST IMG'})
    #return HttpResponse(simplejson.dumps(awb_dict))
    return JsonResponse(awb_dict , json_dumps_params={'ensure_ascii': False})
    #return HttpResponse(result)
