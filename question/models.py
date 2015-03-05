from django.db import models
from django.utils import timezone

class Question(models.Model):
  text = models.CharField(max_length=1000)
  pub_time = models.DateTimeField(default=timezone.now)
  is_public = models.BooleanField(default=False)
  def __unicode__(self):
    return unicode(self.text)

class Post(models.Model):
  author = models.CharField(max_length=150)
  title = models.CharField(max_length=150)
  text = models.CharField(max_length=1500)
  pub_date = models.DateTimeField(default=timezone.now)
  upd_date = models.DateTimeField(default=timezone.now)
  is_public = models.BooleanField(default=False)
  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'
  def __unicode__(self):
    return unicode(self.title)+" / "+unicode(self.text)

class Comment(models.Model):
  author = models.CharField(max_length=150)
  text = models.CharField(max_length=1000)
  pub_date = models.DateTimeField(default=timezone.now)
  post = models.ForeignKey(Post)
  class Meta:
    verbose_name = 'Comment'
    verbose_name_plural = 'Comments'
  def __unicode__(self):
    return unicode(self.author)+"/"+unicode(self.text)
  
  

    
    


    
