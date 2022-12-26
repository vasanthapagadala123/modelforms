from django import forms
from app.models import *
class Topicform(forms.ModelForm):
     class Meta:
           model=Topic
           fields='__all__'
class webpageform(forms.ModelForm):
     class Meta:
           model=Webpage
           fields='__all__'
class accessform(forms.ModelForm):
     class Meta:
           model=AccessRecords
           fields='__all__'
              