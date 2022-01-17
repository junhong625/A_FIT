from django.shortcuts import render, get_object_or_404
from qnaboard.models import Qna
from login.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

# 사용자가 요구한 리퀘스트객체받음.
def index(request):
    article_list = Qna.objects.all().order_by('-writeDate')
    # Notice.object 안에 있는 걸 모두갖고옴
    # select all 같은거임.
    # 그런데 writeDate를 기준으로 -(디센딩)해서 정렬해서 갖고와라.

    # 받아온 데이터를 컨텍스트에 딕셔너리 형태로저장
    context = {'article_list': article_list}

    return render(request, 'qnaboard/index.html', context)


# 글쓰기함수
def write_article(request):
    # 별 기능 없고 글쓰기쪽으로 쏴주기만하는기능
    return render(request, 'qnaboard/writeArticle.html')


# 글내용보내는함수
def add_article(request):
    print(request.session.get('user_id', 'unknown'))
    qna = Qna()
    user = User()
    # 매개변수 request 에서 POST로 받아온것중 '키값'인것
    qna.title = request.POST['title']
    qna.content=request.POST['content']
    qna.writeID=request.session.get('user_id', 'unknown')
    qna.receiveEmail=request.POST['email']

    # 위에서 받아온 값 저장.
    qna.save()

    # 특정 사이트로 호출하라고 보내는것이 리다이렉트임.(현재앱에서 다른앱으로가는거
    # 탬플릿 랭기지에잇는 url을 파이썬으로만들어놓은것이 reverse
    return HttpResponseRedirect(reverse('qnaboard:index'))


# get_object_or_404 : 있으면 Notice가져옴, 없으면 404 낫파운드 화면을 사용자에게 뿌려줌
def view_article(request, article_id):
    qna= get_object_or_404(Qna,pk=article_id)
    #항상 딕셔너리 타입으로 보내줘야해서 즉석에서만듬
    return render(request, 'qnaboard/detail.html', {'article':qna} )


# 글수정
def update_article(request, article_id):
    # notice= get_object_or_404(Notice,pk=article_id) 하지않은이유:
    # 당연히 있는 걸 가져왔기 때문에 굳이하지않는다.
    qna = Qna.objects.get(id=article_id)
    if request.method == 'POST':
        # 주소창에 수동타이핑으로 입력해서 들어온경우를 방지하기 위함
        qna.title = request.POST['title']
        # title : name의 값임. (name='title')
        qna.content = request.POST['content']
        qna.title = request.POST['title']
        qna.writeDate = timezone.datetime.now()
        qna.save()
        return HttpResponseRedirect(reverse('qnaboard:view', args=(article_id,)))
        # 파이썬의 튜플은 원소가 하나인경우에는 반드시 콤마를 붙여줘야 튜플로 인식이된다. (article_id,)
    else:
        return render(request, 'qnaboard/detail.html', {'article': qna})


def delete_article(request, article_id):
    qna = Qna.objects.get(id=article_id)
    qna.delete()
    # 전체리스트 보여줌.
    return HttpResponseRedirect(reverse('qnaboard:index'))

class RegistQna(APIView):
    def post(self, request):

        title = request.data['title']
        email = request.data['email']
        content = request.data['content']
        # 공백 체크
        if (email == '' or None) or (title == '' or None) or (content == '' or None):
            return Response(status=200, data=dict(msg="제목,이메일,내용을 채워주세요"))
        writeID = request.session.get('user_id', 'UNKNOWN')

        # 집어넣기
        qna = Qna.objects.create(title=title, receiveEmail =email , content=content, writeID=writeID)

        return Response(status=200, data=dict(msg="등록 성공"))
