from tensorflow.keras.models import load_model
from PIL import Image

model = load_model('/home/ubuntu/mysite/home/load_model/train_model_2.h5')
img = Image.open('/home/ubnutu/media/squat.jpg')
img = img.convert('RGB')
img = img.resize(400,400)
data = np.array(img)
result = model.predict_classes(data)
if result == 0:
    print('이 사진은 스쿼트 자세가 아닙니다.')
else :
    print('이 사진은 스쿼트 자세가 맞습니다.')

