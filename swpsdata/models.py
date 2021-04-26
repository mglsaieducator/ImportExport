from django.db import models

# Create your models here.


class Data(models.Model):
	CourseName 				= models.CharField(max_length=50, blank=True)
	CourseDescription 		= models.TextField(max_length=10000, blank=True)
	Question		 		= models.TextField(max_length=10000, blank=True)
	Answer 					= models.TextField(max_length=10000, blank=True)
	

	def __str__(self):
		return self.CourseName





