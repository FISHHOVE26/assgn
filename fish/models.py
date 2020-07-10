from django.db import models



class Inquiry(models.Model):
 name = models.CharField(max_length=60, null=True)
 number = models.IntegerField( null=True)
 email = models.CharField(max_length=100, null=True)
 inquiry = models.TextField(null=True)
