from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic_name']


class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url','email']


class AccessrecordForm(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields=['date']
