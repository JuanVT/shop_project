from django import forms

from shop_project.shop.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review
        fields = ['review', 'product']

        widgets = {


        }
