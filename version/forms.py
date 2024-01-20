from django import forms

from catalog.forms import StyleFormMixin
from version.models import Version


class VersionForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для форм приложения Version.
    """

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Инициализация класса VersionForm.
        """
        super().__init__(*args, **kwargs)
        self.fields["version_status"].widget.attrs['class'] = 'form-check-input'
