from django import forms

class ColorfulContactForm(forms.Form):
    latin = forms.CharField(
	label='Latin (Zarubin dictionary):',
	max_length=2000,
        #widget=forms.Textarea(),
        #help_text='Write here your message!'
	)
    cyrillic = forms.CharField(
	label='Cyrillic (Karamshoev dictionary)',
	max_length=2000,
	#widget=forms.Textarea(),
	#help_text='Write here your message!'
	)
