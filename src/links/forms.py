from django import forms
from links.models import Link


class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url', )
