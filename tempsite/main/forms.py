from django import forms


class NewToDolist(forms.Form):
    name = forms.CharField(label="Name of the list", max_length=200)
    complete = forms.BooleanField(required=False)
