from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length = 32, default = 'TITLE')
	content = models.TextField(null = True)   #允许为空
	pub_time = models.DateTimeField(auto_now = True, null = True)

	def __str__(self):
		return self.title


