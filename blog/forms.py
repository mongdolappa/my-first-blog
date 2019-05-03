from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm): # 우리가 만들 폼이 ModelForm이라는 것을 장고에 알려준다.

    class Meta:
        model = Post # 이 폼을 만들기 위해서 Post라는 모델을 써라.
        fields = ('title', 'text') # 이 폼에서는 타이틀과 텍스트만 보이게..
        #fields = ('__all__') 모든 필드를 다 하려면.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)