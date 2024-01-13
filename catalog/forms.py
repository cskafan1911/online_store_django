from django import forms

from catalog.models import Products


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductsForm(StyleFormMixin, forms.ModelForm):
    forbidden_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields["is_published"].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Products
        exclude = ('creator',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in self.forbidden_list:
            raise forms.ValidationError('Данный продукт находится в списке запрещенных')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if set([word.upper() for word in cleaned_data.split()]) & set([word.upper() for word in self.forbidden_list]):
            raise forms.ValidationError('Данный продукт находится в списке запрещенных')

        return cleaned_data


class ModeratorForm(ProductsForm):

    class Meta:
        model = Products
        fields = ('is_published', 'description', 'category',)
