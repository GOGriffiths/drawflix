from django import forms
# from django.contrib.auth.models import User
from drawflix.models import Drawing
 # ,UserProfile


class DrawingForm(forms.ModelForm):


    film = forms.CharField(max_length=200)
    image = forms.CharField()
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    # views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Drawing
        fields = ('image', 'film')

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        # exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

        exclude = ('user', 'date')
