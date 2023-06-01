from django import forms
from django.core.exceptions import ValidationError

from alcohols.models import Comment

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
