from django import forms


from version.models import Version


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["version_status"].widget.attrs['class'] = 'form-check-input'
