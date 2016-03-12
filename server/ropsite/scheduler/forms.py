import datetime
from datetime import datetime, date

from django import forms
from scheduler.models import Øvedage, Lokaler, Segmenter

class ØvedagForm(forms.ModelForm):
    dato = forms.DateField(help_text="Vælg venligst en dato for den nye øvedag.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model, as well as hiding unnecesary fields.
        model = Øvedage
        fields = ('dato',)

class LokaleForm(forms.ModelForm):
    lokalenavn = forms.CharField(max_length=128, help_text="Indtast venligst navnet på det nye øvelokale.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Lokaler
        fields = ('lokalenavn',)


class SegmentForm(forms.ModelForm):
    act        = forms.CharField(max_length=128)
#    act        = formsCharField(max_length=128, empty_label="Vælg act til øvelse")
    start      = forms.TimeField()
    slut       = forms.TimeField()
    pre_break  = forms.IntegerField()
    post_break = forms.IntegerField()

    class Meta:
        model = Segmenter
        fields = ('act', 'start', 'slut', 'pre_break', 'post_break')
