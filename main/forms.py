from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag', 'author', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={ 'class' : 'user-box'}),
            'title_tag' : forms.TextInput(attrs={ 'class' : 'user-box'}),
            'author' : forms.Select(attrs={ 'class' : 'user-box'}),
            'body' : forms.Textarea(attrs  ={ 'class' : 'user-box'}),
        }