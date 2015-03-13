from django import forms
from converter_core import converter


class TabConverterForm(forms.Form):

    guitar_tab = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 12, 'cols': 100}))

    def clean_guitar_tab(self):

        guitar_tab_file = self.cleaned_data.get('guitar_tab', '')
        return converter.to_piano_tab(guitar_tab_file)
