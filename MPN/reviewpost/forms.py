from django.forms import ModelForm
from .models import Reviewpost

class Reviewpostform(ModelForm):
    class Meta:
        model = Reviewpost
        fields = ('content_name', 'content', 'photos')