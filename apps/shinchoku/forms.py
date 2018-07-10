from django import forms


class ShinchokuForm(forms.Form):
    text = forms.CharField()
