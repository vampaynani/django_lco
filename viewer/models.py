from django.db import models

class Course(models.Model):
  title = models.CharField(max_length=255)
  slug = models.CharField(max_length=50)
  price = models.DecimalField(decimal_places=2)
  created_at = models.DateTimeField()

class Video(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  video_url = models.CharField(max_length=255)
  created_at = models.DateTimeField()
  course = models.ForeignKey(Course, on_delete=models.CASCADE)