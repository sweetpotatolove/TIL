from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)

    # print 방법 바꾸는법
    def __str__(self):
        return self.name