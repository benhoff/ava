from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    last_updated = models.DateField(auto_now=True)

    # showing blog as an example
    #blog = models.ForeignKey(Blog)
