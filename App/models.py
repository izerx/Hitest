from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=100, null=True, blank=True)

class Test(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    questions= models.ManyToManyField("Question")

class Question(models.Model):
    text = models.TextField()
    right_answer = models.TextField()
    wrong_answers = models.TextField()
