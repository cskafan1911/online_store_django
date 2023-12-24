from django import forms


from version.models import Version


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
