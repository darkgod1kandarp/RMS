from django import forms
from .models import check,teach
class form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = check
        fields = "__all__"
class teacherForm(forms.ModelForm):
    
    class Meta:
        model = teach
        fields = '__all__'

       