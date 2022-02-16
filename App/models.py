from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import random

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=100, null=True, blank=True)
    fio = models.CharField(max_length=100, null=True, blank=True)

    status = models.IntegerField(default=0, null=0, blank=True)

class Test(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, null=True, blank=True)
    questions = models.ManyToManyField("Question")
    is_complete = models.BooleanField(default=False)

class Subject(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    teacher = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    chapters = models.ManyToManyField("Chapter", blank=True)
    questions= models.ManyToManyField("Question", blank=True)

class Chapter(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    questions= models.ManyToManyField("Question")

class Result(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    number_test = models.IntegerField(null=True, blank=True)
    all_questions_count = models.IntegerField(null=True, blank=True)
    right_answers = models.IntegerField(null=True, blank=True)
    wrong_answers = models.IntegerField(null=True, blank=True)
    answers = models.TextField()

    def get_answers(self):
        return eval(self.answers)

class Question(models.Model):
    text = models.TextField()
    right_answer = models.TextField()
    wrong_answers = models.TextField()

    def get_answers(self):
        return sorted(eval(self.wrong_answers)+[self.right_answer], key=lambda a: random.random())
