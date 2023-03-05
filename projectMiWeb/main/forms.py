from django.forms import ModelForm,DateInput, Textarea, Select, FileInput
from .models import Posts, Category


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['description','cat','date_posted', 'file']

        widgets = {
            "description": Textarea(attrs={'class': 'form-control'}),
            "cat": Select(attrs={'class': 'form-control'}),
            "date_posted": DateInput(attrs={'class': 'form-control','type':'date'}),
            "file": FileInput(attrs={'class': 'form-control', 'type': 'file'})

        }