from django.forms import ModelForm
from info.models import GetInTouch


class GetInTouchForm(ModelForm):
    class Meta:
        model = GetInTouch
        fields = '__all__'
