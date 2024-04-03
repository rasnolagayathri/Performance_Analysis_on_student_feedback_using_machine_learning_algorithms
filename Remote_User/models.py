from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)



class Clientreadings_Model(models.Model):
    userId = models.ForeignKey(ClientRegister_Model, on_delete=CASCADE)
    names = models.CharField(max_length=300)
    regno= models.CharField(max_length=50)
    subject= models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    semester = models.CharField(max_length=300)
    cname = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    ratings = models.IntegerField(default=0)
    usefulcounts = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)



class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    suggestion = models.CharField(max_length=300)

class studentdata_Model(models.Model):

        names = models.CharField(max_length=300)
        Regno = models.CharField(max_length=50)
        Gender = models.CharField(max_length=100)
        Age = models.CharField(max_length=100)
        Height = models.CharField(max_length=300)
        Weight = models.CharField(max_length=300)
        Physical_Fit = models.CharField(max_length=300)
        ratings = models.IntegerField(default=0)
        usefulcounts = models.IntegerField(default=0)
        dislikes = models.IntegerField(default=0)
        Physical_Fit = models.CharField(max_length=300)
        cardio_Fit = models.CharField(max_length=300)
        Aerobic_Fit = models.CharField(max_length=300)
        Stress = models.CharField(max_length=300)
        Intelligent = models.CharField(max_length=300)
        Executive_fun = models.CharField(max_length=300)
        Eating = models.CharField(max_length=300)
        Mental_Health = models.CharField(max_length=300)
        Pyhsical_Activity = models.CharField(max_length=300)
        Sleep_pattern = models.CharField(max_length=300)
        Social_Tie = models.CharField(max_length=300)
        Time_Management = models.CharField(max_length=300)
        Stu_Class = models.CharField(max_length=300)
        Library_Entry = models.CharField(max_length=300)
        Online_learning = models.CharField(max_length=300)
        Semester = models.CharField(max_length=300)
        Attendance = models.IntegerField(default=0)


