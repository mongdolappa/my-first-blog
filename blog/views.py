from django.shortcuts import render
from django.utils import timezone
from .models import Post  #blog.models 로 해도 되나, 동일 디렉토리 내는 .models

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all
    return render(request, 'blog/post_list.html', {'posts': posts})
# 방금 post_list라는 함수(def)를 만들었습니다.
# 이 함수는 요청(request)을 넘겨받아 render메서드를 호출합니다.
# 이 함수는 render 메서드를 호출하여 받은(return) blog/post_list.html 템플릿을 보여줍니다.

