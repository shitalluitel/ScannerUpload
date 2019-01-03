from django import forms
from .models import Uploader as UploaderModel

class ScannerUploadForm(forms.ModelForm):
	class Meta:
		model = UploaderModel

		fields = [
			'title'
		]

		labels = {
			'title': "Title",
		}
	# def process(self):
	# 	data = self.cleaned_data
	# 	return data