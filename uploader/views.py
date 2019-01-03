from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ScannerUploadForm
from .models import File

# Create your views here.
def scan(request):
	return render(request, 'scan.html')

def scan_pdf_to_form(request):
	context = {}
	form = ScannerUploadForm(request.POST or None)
	if request.method == "POST":
		files = request.FILES.getlist('com_asprise_scannerjs_images[]')
		if form.is_valid() and len(files) <= 5:
			form_data = form.save(commit=False)
			form_data.save()
			for chunk in files:
				file = File()
				file.uploader = form_data
				file.image = chunk
				file.save()

	context['form'] = form
	return render(request, 'scan_pdf_to_form.html', context)
