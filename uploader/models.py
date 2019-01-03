from django.db import models

# Create your models here.
class Uploader(models.Model):	
	title = models.CharField(max_length=100, null=True, blank=True)


class File(models.Model):
	uploader = models.ForeignKey(Uploader, related_name="uploaders", on_delete=models.CASCADE)
	image = models.FileField(upload_to='uploads/', null=True, blank=True)
	
