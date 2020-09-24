from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(max_length=256, label='Отзыв')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')

