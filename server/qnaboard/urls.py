from django.urls import path
from . import views
from django.conf.urls import url
from qnaboard.views import *

# . :햔재폴더 - noticeboard

app_name = 'qnaboard'
urlpatterns = [
    path('', views.index, name='index'),
    # <a class ="cls1" href="{% url 'noticeboard:write_article' $}"></a>
    # 위 코드에서 name = 'write_article'이 호출되면, path 맨앞 아규먼트 'write'의 주소로 보내지는것
    # 이러면 주소가바뀌어도 쉽게고칠수있다.
    path('write', views.write_article, name='write_article'),

    # 글내용보내는기능 링크.
    path('add', views.add_article, name='add_article'),

    # 아이디 번호를 받아오기때문에 <int:article_id>/' 로 받는다.
    path('<int:article_id>/', views.view_article, name='view'),

    # 글수정
    path('update/<int:article_id>/', views.update_article, name='update'),
    path('delete/<int:article_id>/', views.delete_article, name='delete'),

    #글쓰기(안드로이드)
    url('regist_qna', views.RegistQna.as_view(), name='regist_qna'),

]
