from django import forms
from django.forms import ModelForm
from .models import FileUpload

class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'imgfile', 'content']

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()


class ModelFormWithFileField(forms.Form):
    file = forms.FileField()
