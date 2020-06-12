from django.db import models

class Course(models.Model):
  title = models.CharField(max_length=255)
  slug = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=7,decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.title

class Video(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  video_url = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  def __str__(self):
    return self.title