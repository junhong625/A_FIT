import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
import matplotlib.pyplot as plt # pip install matplotlib
import numpy as np # pip install numpy
import os
import glob


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tqdm import tqdm # pip install tqdm
import time, random

class_name=['squat', 'plank', 'stand'] # 분류할 자세 이름 설정
lst_dir=[] # 이미지 파일이 들어있는 폴더이름 목록이 들어갈 리스트
lst_im=[] # 이미지 파일들이 들어갈 리스트

for name in class_name: # for문을 거쳐 squat, plank, stand 폴더에 들어있는 이미지 파일들의 사이즈를 width=400, height=400으로 변경
    lst_dir=os.listdir('D:/skel/%s'%name)
    for j in lst_dir:
        b=cv2.imread('D:/skel/%s/%s'%(name, j))
        b=cv2.resize(b,(600,600))
        lst_im.append(np.array(b))

squat_size = len(os.listdir('D:/skel/squat')) # squat 폴더에 들어있는 이미지 개수
stand_size = len(glob.glob('D:/skel/stand/*.*')) # stand 폴더에 들어있는 이미지 개수

lst_label=[] # lst_im에 들어있는 모든 자세의 이미지들마다의 라벨을 설정해주기 위해 리스트에 저장

for i in range(len(lst_im)): # for문을 통해 각 자세 폴더에 들어있는 이미지 개수만큼 해당 자세의 라벨들을 lst_label에 입력
    if i < squat_size:
        lst_label.append([1,0,0])
    elif squat_size <= i < len(lst_im) - stand_size:
        lst_label.append([0,1,0])
    else :
        lst_label.append([0,0,1])
# 이미지와 라벨 둘 다 배열로 변환
lst_im=np.array(lst_im) 
lst_label=np.array(lst_label) 

# train_test_split함수를 통해 train할 이미지와 test할 이미지 분류
lst_im, x_test,lst_label,y_test=train_test_split(lst_im,lst_label,test_size=0.2,random_state=42)
lst_im, x_val,lst_label,y_val=train_test_split(lst_im,lst_label,test_size=0.2,random_state=42)

# 배열로 변환
x_val=np.array(x_val)
y_val=np.array(y_val)
x_test=np.array(x_test)
y_test=np.array(y_test)

# .shape 함수로 배열 점검
x_val.shape
x_test.shape
y_val.shape

# 이 주석은 총 9개의 이미지를 보여주는 코드
# plt.figure(figsize=(12,12))
# for i in range(9):
#     b=np.argmax(lst_label[i])
#     plt.subplot(3,3,i+1)
#     plt.imshow(lst_im[i])
# plt.show()

# 직접 실험을 해보며 최적의 결과물을 뽑아낼 수 있도록 argument나 세팅값을 잘 설정해야함 
#------------------------------------------------------------------------------------------------------
model=Sequential()
model.add(Conv2D(filters=50,kernel_size=3,padding='same',activation='LeakyReLU',input_shape=(600,600,3)))
model.add(Conv2D(filters=40,kernel_size=3,padding='same',activation='LeakyReLU'))
model.add(MaxPool2D(pool_size=(4,4)))
model.add(Conv2D(filters=40,kernel_size=3,padding='same',activation='LeakyReLU'))
model.add(Conv2D(filters=30,kernel_size=3,padding='same',activation='LeakyReLU'))
model.add(Conv2D(filters=20,kernel_size=3,padding='same',activation='LeakyReLU'))
model.add(Conv2D(filters=10,kernel_size=3,padding='same',activation='LeakyReLU'))
model.add(MaxPool2D(pool_size=(4,4)))
model.add(Flatten())
model.add(Dense(50,activation='LeakyReLU'))
model.add(Dense(20,activation='LeakyReLU'))
model.add(Dense(10,activation='LeakyReLU'))
model.add(Dropout(0.5))
model.add(Dense(3,activation='softmax'))
model.compile(optimizer='adam', 
             loss='categorical_crossentropy',
             metrics=['acc'])
model.summary()

history=model.fit(lst_im,lst_label,epochs=20,
                 batch_size=64,
                 validation_data=(x_val,y_val))
#-------------------------------------------------------------------------------------------------------                 
history.history # 학습 과정 출력
model.evaluate(x_val, y_val, batch_size=8) # 학습 검증
model.save('D:/train_model(3_pose).h5') # 학습 모델 저장
predictions = model.predict(x_test[:3]) # 학습 검증

print('predictions shape:', predictions.shape) # 
predictions

caltech_dir = "D:/image_test" # 학습에 사용되지 않은 새로운 이미지이 저장된 디렉토리
image_w = 600 # 변경할 이미지 사이즈
image_h = 600
pixels = image_h * image_w * 3 
X = [] # 전처리한 이미지를 집어넣을 리스트
filenames = [] # 분류할 자세 이름 리스트
files = glob.glob(caltech_dir+"/*.*") # glob함수를 통해 파일의 절대경로들을 files에 저장
for f in files: # for문을 통해 폴더 안의 이미지들을 모두 전처리하고 X 리스트에 추가
    img = Image.open(f)
    img = img.convert("RGB")
    img = img.resize((image_w, image_h))
    data = np.asarray(img)
    filenames.append(f)
    X.append(data)
X = np.array(X) # 배열로 변환
# X = X/255
len(X)

model = load_model('D:/pose_3_model.h5') # 학습 모델 불러오기
prediction = model.predict(X) # 새로운 이미지로 학습 검증

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)}) # 인쇄옵션 설정
cnt = 0
r_list = 0

for i in prediction: # for 문을 통해 예측 결과를 텍스트로 
    pre_ans = i.argmax()  # .argmax 함수를 통해 가장 큰 값의 인덱스르 반환 => 레이블 [1. 0. 0.] 이런식으로 되어 있는 것을 숫자로 바꿔주는 것.
    print(i) # 예측 수치 출력
    print(pre_ans) # 예측 인덱스 출력
#     if i[0] >= 0.6 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 squat로 추정됩니다.") # 예측 수치가 0.6 이상인 자세로 추정된다는 텍스트 출력(argmax를 사용 X)
#     if i[1] >= 0.6: print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 plank로 추정됩니다.")
#     if i[2] >= 0.6: print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 stand로 추정됩니다.")
    if pre_ans == 0 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 squat로 추정됩니다.") # 출력된 값을 인덱스로 받아 filenames 해당 인덱스의 자세로 추정된다는 텍스트 출력(argmax를 사용 O)
    if pre_ans == 1 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 plank로 추정됩니다.")
    if pre_ans == 2 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 stand로 추정됩니다.")
    cnt += 1
    # 레이블 [1. 0. 0.] 이런식으로 되어 있는 것을 숫자로 바꿔주는 것.
