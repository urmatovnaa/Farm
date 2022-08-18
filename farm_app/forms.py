from django.forms import ModelForm
from farm_app.models import AboutUs


class AboutUsForm(ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
