from django.db import models


class Blog(models.Model):

    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
