import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tqdm import tqdm
import time, random

class_name=['squat', 'plank', 'stand']
lst_dir=[]
lst_im=[]
for name in class_name:
    lst_dir=os.listdir('D:/skel/%s'%name)
    for j in lst_dir:
        b=cv2.imread('D:/skel/%s/%s'%(name, j))
        b=cv2.resize(b,(400,400))
        lst_im.append(np.array(b))

squat_size = len(os.listdir('D:/skel/squat'))
stand_size = len(glob.glob('D:/skel/stand/*.*'))

lst_label=[]
for i in range(len(lst_im)):
    if i < squat_size:
        lst_label.append([1,0,0])
    elif squat_size <= i < len(lst_im) - stand_size:
        lst_label.append([0,1,0])
    else :
        lst_label.append([0,0,1])

lst_im=np.array(lst_im)
lst_label=np.array(lst_label)

lst_im, x_test,lst_label,y_test=train_test_split(lst_im,lst_label,test_size=0.2,random_state=42)
lst_im, x_val,lst_label,y_val=train_test_split(lst_im,lst_label,test_size=0.2,random_state=42)

x_val=np.array(x_val)
y_val=np.array(y_val)
x_test=np.array(x_test)
y_test=np.array(y_test)

x_val.shape
x_test.shape
y_val.shape


# plt.figure(figsize=(12,12))
# for i in range(9):
#     b=np.argmax(lst_label[i])
#     plt.subplot(3,3,i+1)
#     plt.imshow(lst_im[i])
# plt.show()

# In[12]:


model=Sequential()
model.add(Conv2D(filters=50,kernel_size=3,padding='same',activation='LeakyReLU',input_shape=(400,400,3)))
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

history=model.fit(lst_im,lst_label,epochs=5,
                 batch_size=64,
                 validation_data=(x_val,y_val))
                 
history.history
model.evaluate(x_val, y_val, batch_size=8)
model.save('D:/train_model(3_pose).h5')
predictions = model.predict(x_test[:3])

print('predictions shape:', predictions.shape)

predictions
x_test[2]
predic = model.predict(x_test)
predic[0]
files

caltech_dir = "D:/image_test"
image_w = 600
image_h = 600
pixels = image_h * image_w * 3
X = []
filenames = []
files = glob.glob(caltech_dir+"/*.*")
for f in files:
    img = Image.open(f)
    img = img.convert("RGB")
    img = img.resize((image_w, image_h))
    data = np.asarray(img)
    filenames.append(f)
    X.append(data)
X = np.array(X)
# X = X/255

len(X)
model = load_model('D:/pose_3_model.h5')
prediction = model.predict(X)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
cnt = 0
r_list = 0
#이 비교는 그냥 파일들이 있으면 해당 파일과 비교. 카테고리와 함께 비교해서 진행하는 것은 _4 파일.
for i in prediction:
    pre_ans = i.argmax()  # 예측 레이블
    print(i)
    print(pre_ans)
#     if i[0] >= 0.6 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 squat로 추정됩니다.")
#     if i[1] >= 0.6: print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 plank로 추정됩니다.")
#     if i[2] >= 0.6: print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 stand로 추정됩니다.")
    if pre_ans == 0 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 squat로 추정됩니다.")
    if pre_ans == 1 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 plank로 추정됩니다.")
    if pre_ans == 2 : print("해당 "+filenames[cnt].split("\\")[1]+"이미지는 stand로 추정됩니다.")
    cnt += 1
    # print(i.argmax()) #얘가 레이블 [1. 0. 0.] 이런식으로 되어 있는 것을 숫자로 바꿔주는 것.
    # 즉 얘랑, 나중에 카테고리 데이터 불러와서 카테고리랑 비교를 해서 같으면 맞는거고, 아니면 틀린거로 취급하면 된다.
    # 이걸 한 것은 _4.py에.
datagen = ImageDataGenerator(
        rotation_range=2,
        width_shift_range=0.05,
        height_shift_range=0.05,
        shear_range=0.05,
        zoom_range = 0.1,
        horizontal_flip=False,
        fill_mode="nearest")

folder = "C:/Users/bit/FinalProject/rotation_image/Squat/stand/"
file_list = [x for x in os.listdir(folder)]

for i in tqdm(range(len(file_list))):
    image = load_img("C:/Users/bit/FinalProject/rotation_image/Squat/stand/" + file_list[i])  # PIL 이미지
    x = img_to_array(image)  # (3, 400, 400) 크기의 NumPy 배열
    x = x.reshape((1,) + x.shape)  # (1, 3, 400, 400) 크기의 NumPy 배열

#     아래 .flow() 함수는 임의 변환된 이미지를 배치 단위로 생성해서
#     지정된 `preview/` 폴더에 저장합니다.
    i = 0
    for batch in datagen.flow(x, batch_size=5,
                              save_to_dir="C:/Users/bit/FinalProject/rotation_image/Squat/stand/", save_prefix="stand_image", save_format="jpg"):
        i += 1
        time.sleep(0.01)
        if i > 5:
            break  # 이미지 10장을 생성하고 마칩니다

model.evaluate(x_test,y_test)[1]