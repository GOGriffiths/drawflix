from django import forms
# from django.contrib.auth.models import User
from drawflix.models import Drawing



class DrawingForm(forms.ModelForm):


    film = forms.CharField(max_length=200)
    image = forms.CharField()
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)


    class Meta:
        # Provide an association between the ModelForm and Drawing model
        model = Drawing

        fields = ('image', 'film')
        exclude = ('user', 'date')
