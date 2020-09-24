from django import forms
from .models import Review, Car

from ckeditor.widgets import CKEditorWidget


class ReviewAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    # car = Car.objects.order_by('id').reverse()  # сортировка: от самого большого id к меньшему

    class Meta:
        model = Review
        fields = ['car', 'title', 'text']
