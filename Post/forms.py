from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['package_name', 'category', 'description', 'image', 'max_budget']


    max_budget = forms.IntegerField(max_value=999999, min_value=0)