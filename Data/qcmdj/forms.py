# qcm/forms.py
from django import forms

class AnswerForm(forms.Form):
    choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
