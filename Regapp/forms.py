from django import forms
from Regapp.models import Church


class ChurchForm(forms.ModelForm):
	class Meta:
		model = Church
		fields = '__all__'