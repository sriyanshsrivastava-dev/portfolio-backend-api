from django import forms
from project.models import Media


class MediaAdminForm(forms.ModelForm):
    upload = forms.FileField(required=False,label="Upload Media")
    class Meta:
        model = Media
        fields = '__all__'