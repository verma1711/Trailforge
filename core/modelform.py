from .models import usermodel
from django.forms import ModelForm

class userform(ModelForm):
    class Meta:
        model = usermodel
        fields = '__all__'