from importlib._common import _

from django.db import models


# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=264, verbose_name='Name')
    picture = models.ImageField(upload_to='book_image', )
    author = models.CharField(max_length=264, )
    email = models.EmailField(max_length=264, blank=True)
    describe = models.TextField(verbose_name="Describe")

    def __str__(self):
        return self.name
