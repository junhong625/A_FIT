from django.db import models
from django.utils.timezone import now


# Create your models here.
class Qna(models.Model):

    # models.Model 을 무조건 상속하게해야함
    # 요소가 컬럼이된다

    # title varchar(100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    writeDate = models.DateTimeField(default=now, editable=False)
    writeID = models.CharField(max_length=50)
    receiveEmail = models.CharField(max_length=100)
    # 별도로 프라이머리키 생성하지않으면 ID 라는 이름으로 자동으로 키 생성해줌

    def __str__(self):
        return self.title


    #class Meta:
     #   db_table = 'Qna'