from django.db import models

# Create your models here.
#book relation that has 2 foreign key author language
#book relation can contain multiple genre so we have used manytomanyfield
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13)
   

    def __str__(self):
        return self.title   