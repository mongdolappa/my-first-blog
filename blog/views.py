from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post  #blog.models 로 해도 되나, 동일 디렉토리 내는 .models
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
# 방금 post_list라는 함수(def)를 만들었습니다.
# 이 함수는 요청(request)을 넘겨받아 render메서드를 호출합니다.
# 이 함수는 render 메서드를 호출하여 받은(return) blog/post_list.html 템플릿을 보여줍니다.

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk) # pk 번호 해당 Post를 불러와서 post에 저장
    return render(request, 'blog/post_detail.html', {'post':post}) # post글을 가지고서, post_detail.html 로딩.

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) # 새 Post 폼을 추가하기 위해 PostForm() 함수를 호출하도록 하여 템플릿에 넘깁니다. (render)
        # request.POST에 입력한 데이타 가지고 있음.POST는 GET반대. 글 post 아님.
        # 만약 method가 POST라면, 폼에서 받은 데이터를 PostForm으로 넘겨줘야겠죠? 이렇게 작성하면 됩니다.
        if form.is_valid(): # 폼에 들어있는 값들이 올바른지를 확인해야합니다.
            post = form.save(commit=False) # 넘겨진 데이터를 바로 Post 모델에 저장하지는 말라.
            # 왜냐하면, 작성자를 추가한 다음 저장해야 하니까요.
            post.author = request.user # user를 author에 저장
            #post.published_date = timezone.now()
            post.save() # 이제 post 모델에 바로 저장해.
            return redirect('post_detail', pk=post.pk) # 다 작성했으면 여기 뷰로 이동.
            # 뷰 이름. pk 번호를 가지고 위의 post_detail 뷰로 이동. pk 필요하니까..
    else: # form에 값이 없으면... 비어 있을때.
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk): # url로부터 추가로 pk 매개변수를 받아서 처리합니다.
    post = get_object_or_404(Post, pk=pk) # pk 번호를 가진 post를 가져온다. 해당 pk 없으면 404 에러 띄워줌.
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now() # 이렇게 하면, 새로 작성한 글이 바로 게시되지 않고 미리 볼 수 있는 초안으로 저장이 됩니다.
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post) # 수정하려니 글을 가져와 보여줘야...(POST요청은 없었고..)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete() # 장고 모델을 삭제할 때는 단순히.delete()를 호출하면 됩니다. 내장.
    return redirect('post_list')