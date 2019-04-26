from django.urls import path
from . import views
#blog 애플리케이션에서 사용할 모든 views를 가져왔어요.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
]
# 이제 post_list라는 view가 루트 URL에 할당되었습니다. ''
# 루트 디렉토리에 View의 post_list함수가 (이 안에 가르키는 html실행) 할당됨.
# 이 패턴은 장고에게 누군가 웹사이트에 'http://127.0.0.1:8000/' 주소로 들어왔을 때
# views.post_list를 보여주라고 말해줍니다.
# 마지막 부분인 name='post_list'는 URL에 이름을 붙인 것으로 뷰를 식별합니다.
# 뷰의 이름과 같을 수도 완전히 다를 수도 있습니다.

# 브라우저에 http://127.0.0.1:8000/post/5/라고 입력하면,
# 장고는 post_detail 뷰를 찾아 매개변수 pk가 5인 값을 찾아 뷰로 전달합니다.