from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Field, Fieldset, HTML
from crispy_forms.bootstrap import FormActions


class PortfolioUpdateForm(forms.Form):

    object_ID = forms.CharField(
        label = "ID of the object you want to update",
        widget= forms.Textarea,
        required = True
    ) 
    color_choices = forms.TypedChoiceField(
        label = "Which Color do you want to change it to?",
        choices = (
            (u'B', 'Blue'),
            (u'R', 'Red'),
  	    (u'G', 'Green')
        ),
        widget = forms.RadioSelect,
        required = True,
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'Object_ID',
        'color_choices',
        FormActions(
            Submit('save_changes', 'update', css_class="btn-primary")
        )
    )
