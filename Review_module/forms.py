from django import forms
from Review_module.models import Review


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
