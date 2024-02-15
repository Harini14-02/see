from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(blank=False,max_length=50)
    lastname = models.CharField(blank=False,max_length=200)
    country = models.CharField(blank=False,max_length=250)

    
    def _str_(self):
        return str(self.firstname._str_())
    
class addrec(models.Model):
    firstname = models.CharField(blank=False,max_length=50)
    lastname = models.CharField(blank=False,max_length=200)
    country = models.CharField(blank=False,max_length=250)

    
    def _str_(self):
        return str(self.firstname._str_())