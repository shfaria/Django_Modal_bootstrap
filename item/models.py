from django.db import models

def testfile():
    files.objects.create()


class Demo(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    file = testfile()

class Demo2(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    file = testfile()

class files(models.Model):
    file = models.FileField(upload_to='static/files/')
