from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Standard(models.Model):
    className=models.CharField(max_length=5)

    def __str__(self):
        return str(self.className)

class Category(models.Model):
    categoryName=models.CharField(max_length=20)

    def __str__(self):
        return str(self.categoryName)

class Subject(models.Model):
    subjectName=models.CharField(max_length=20)

    def __str__(self):
        return str(self.subjectName)



class Question(models.Model):
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    standard=models.ForeignKey('Standard', on_delete=models.CASCADE)
    subject=models.ForeignKey('Subject',on_delete=models.CASCADE)
    word=models.CharField(max_length=30)
    desc = models.CharField(max_length=100, default="NOT Available")
    problemNo = models.CharField(max_length=20, default="NOT Available")

    def __str__(self):
        return str(self.word)

class Question2(models.Model):
    id=models.IntegerField(primary_key=True)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    standard=models.ForeignKey('Standard', on_delete=models.CASCADE)
    subject=models.ForeignKey('Subject',on_delete=models.CASCADE)
    que=models.CharField(max_length=500)
    opt1=models.CharField(max_length=500)
    opt2=models.CharField(max_length=500)
    opt3=models.CharField(max_length=500)
    opt4=models.CharField(max_length=500)
    Answer=models.CharField(max_length=1,null=True)
    # def __str__(self):
    #     return str(self.word)

class UserDetails(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True)
    standard=models.CharField(max_length=5)
    points=models.IntegerField(default=0)

    # def __str__(self):
    #     return self.first_name
    
class LeaderBoard(models.Model):
    email=models.EmailField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    standard=models.CharField(max_length=5)
    points=models.IntegerField(default=0)

    def __str__(self):
        return self.first_name