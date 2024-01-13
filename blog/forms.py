from django import forms

from blog.models import Blog
from catalog.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields["is_published"].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Blog
        fields = ('title', 'content', 'preview', 'is_published',)
